
from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import init_db, save_interview, get_history
from ai_service import generate_question, evaluate_answer
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "development-secret-change-me")

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    history = get_history()

    total = len(history)
    average = round(
        sum(item["score"] for item in history) / total, 1
    ) if total else 0

    return render_template(
        "dashboard.html",
        history=history,
        total=total,
        average=average
    )


@app.route("/start", methods=["POST"])
def start_interview():
    category = request.form.get("category", "Python")
    difficulty = request.form.get("difficulty", "Intermediate")

    allowed_categories = [
        "Python", "Java", "JavaScript", "SQL",
        "HTML & CSS", "HR", "Machine Learning"
    ]

    allowed_difficulties = [
        "Beginner", "Intermediate", "Advanced"
    ]

    if category not in allowed_categories:
        flash("Please select a valid category.")
        return redirect(url_for("home"))

    if difficulty not in allowed_difficulties:
        flash("Please select a valid difficulty.")
        return redirect(url_for("home"))

    try:
        question = generate_question(category, difficulty)

        session["category"] = category
        session["difficulty"] = difficulty
        session["question"] = question

        return render_template(
            "interview.html",
            category=category,
            difficulty=difficulty,
            question=question
        )

    except Exception as error:
        flash(f"Question generation failed: {error}")
        return redirect(url_for("home"))


@app.route("/submit", methods=["POST"])
def submit_answer():
    question = session.get("question")
    category = session.get("category")
    difficulty = session.get("difficulty")
    answer = request.form.get("answer", "").strip()

    if not question or not category:
        flash("Please start a new interview.")
        return redirect(url_for("home"))

    if len(answer) < 10:
        flash("Please enter a more detailed answer (at least 10 characters).")
        return redirect(url_for("home"))

    if len(answer) > 5000:
        flash("Your answer is too long. Please keep it under 5000 characters.")
        return redirect(url_for("home"))

    try:
        evaluation = evaluate_answer(question, answer, category)

        data = {
            "category": category,
            "difficulty": difficulty,
            "question": question,
            "answer": answer,
            "score": evaluation["score"],
            "feedback": evaluation["feedback"],
            "suggestions": evaluation["suggestions"]
        }

        save_interview(data)

        session.pop("question", None)

        return render_template("result.html", result=data)

    except Exception as error:
        flash(f"Evaluation failed: {error}")
        return redirect(url_for("home"))


@app.route("/history")
def history():
    return render_template("dashboard.html",
                           history=get_history(),
                           total=len(get_history()),
                           average=0)


if __name__ == "__main__":
    app.run(debug=True)
