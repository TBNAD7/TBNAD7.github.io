async function submitData() {
    const textInput = document.getElementById("textInput").value;
    const response = await fetch("http://3.35.48.249:8000/generate_quiz", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: textInput })
    });
    const result = await response.json();
    document.getElementById("quizOutput").innerText = result.quiz_question;
}
