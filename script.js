async function submitData() {
    const textInput = document.getElementById("textInput").value;
    
    // 입력이 비어있지 않은지 확인
    if (!textInput) {
        alert("입력란이 비어 있습니다.");
        return;
    }

    console.log("입력한 텍스트:", textInput); // 디버깅을 위한 로그

    // API 요청
    try {
        const response = await fetch("http://3.35.48.249:8000/generate_quiz", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: textInput })
        });

        if (!response.ok) {
            console.error("API 오류:", response.status, response.statusText);
            return;
        }

        const result = await response.json();
        console.log("서버 응답:", result); // 응답 내용 확인

        // 퀴즈 질문을 화면에 출력
        if (result.quiz_question) {
            document.getElementById("quizOutput").innerText = result.quiz_question;
        } else {
            console.error("퀴즈 질문을 받지 못했습니다.");
        }
    } catch (error) {
        console.error("API 요청 중 오류:", error);
    }
}
