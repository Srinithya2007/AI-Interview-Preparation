
import os
import json
import re

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
print("API KEY LOADED:", bool(API_KEY))
print("MODEL:", MODEL)

client = genai.Client(api_key=API_KEY) if API_KEY else None


# --------------------------------
# 3. CHECK API CONNECTION
# --------------------------------

def check_api():

    if not API_KEY:
        raise ValueError(
            "GEMINI_API_KEY not found. Check your .env file."
        )

    if client is None:
        raise ValueError(
            "Gemini client initialization failed."
        )

    return True


# --------------------------------
# 4. COMMON AI GENERATION FUNCTION
# --------------------------------

def ask_ai(prompt):

    check_api()

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        if not response or not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response.text.strip()

    except Exception as error:

        print("GEMINI API ERROR:", repr(error))

        raise RuntimeError(
            f"Gemini API failed: {error}"
        ) from error


# --------------------------------
# 5. GENERATE INTERVIEW QUESTION
# --------------------------------

def generate_question(category, difficulty):

    prompt = f"""
    You are a professional technical interviewer.

    Generate ONE original interview question.

    Interview Category: {category}

    Difficulty Level: {difficulty}

    Requirements:

    1. Generate only one question.
    2. Question must match the selected category.
    3. Question must match the difficulty level.
    4. Avoid duplicate or overly generic questions.
    5. Do not provide the answer.
    6. Return only the interview question.

    Generate the question now.
    """

    try:

        question = ask_ai(prompt)

        # Remove unnecessary quotation marks
        question = question.strip().strip('"').strip("'")

        if not question:
            raise ValueError(
                "Question generation returned empty text."
            )

        print("GENERATED QUESTION:", question)

        return question

    except Exception as error:

        print("QUESTION GENERATION ERROR:", repr(error))

        raise RuntimeError(
            f"Unable to generate interview question: {error}"
        ) from error


# --------------------------------
# 6. EVALUATE STUDENT ANSWER
# --------------------------------

def evaluate_answer(question, answer, category):

    prompt = f"""
    You are an expert interview evaluator.

    Evaluate the candidate's interview answer.

    Category: {category}

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate based on:

    1. Technical accuracy
    2. Relevance
    3. Clarity
    4. Completeness

    Give an honest evaluation.

    Return ONLY valid JSON.

    Required format:

    {{
        "score": 75,
        "feedback": "Explain the answer quality.",
        "suggestions": "Explain how to improve the answer."
    }}

    Score must be an integer between 0 and 100.
    """

    try:

        result = ask_ai(prompt)

        # Extract JSON from AI response
        match = re.search(
            r"\{.*\}",
            result,
            re.DOTALL
        )

        if not match:
            raise ValueError(
                "AI returned invalid JSON."
            )

        data = json.loads(match.group())

        score = int(data["score"])

        score = max(0, min(100, score))

        feedback = str(data["feedback"])

        suggestions = str(data["suggestions"])

        return {
            "score": score,
            "feedback": feedback,
            "suggestions": suggestions
        }

    except Exception as error:

        print("ANSWER EVALUATION ERROR:", repr(error))

        raise RuntimeError(
            f"Answer evaluation failed: {error}"
        ) from error
