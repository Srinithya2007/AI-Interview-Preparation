
document.addEventListener("DOMContentLoaded", function () {

    // Answer character counter
    const answerBox = document.getElementById("answer");
    const charCount = document.getElementById("charCount");

    if (answerBox && charCount) {
        answerBox.addEventListener("input", function () {
            charCount.textContent =
                answerBox.value.length + " / 5000";
        });
    }

    // Prevent empty answer submission
    const answerForm = document.getElementById("answerForm");
    const submitBtn = document.getElementById("submitBtn");

    if (answerForm) {
        answerForm.addEventListener("submit", function (event) {

            if (answerBox.value.trim().length < 10) {
                event.preventDefault();
                alert("Please enter a detailed answer.");
                return;
            }

            if (answerBox.value.length > 5000) {
                event.preventDefault();
                alert("Your answer must be under 5000 characters.");
                return;
            }

            submitBtn.textContent = "AI is evaluating your answer...";
            submitBtn.disabled = true;
        });
    }

});
