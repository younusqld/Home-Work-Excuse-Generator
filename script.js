const clickSound = new Audio('click.mp3');

async function speak(text) {
    clickSound.currentTime = 0;
    clickSound.play();

    try {
        // Encode text for URL
        const encodedText = encodeURIComponent(text);

        // Google TTS URL (Malayalam)
        const ttsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodedText}&tl=ml&client=tw-ob`;

        const audio = new Audio(ttsUrl);
        audio.play();
    } catch (err) {
        console.error("TTS error:", err);
    }
}

async function generateExcuse() {
    try {
        const res = await fetch(`http://127.0.0.1:5000/generate-excuse`);
        const data = await res.json();

        if (data.excuse) {
            const emojis = ["😂", "😅", "🙈", "🤦‍♂️"];
            const excuseText = data.excuse + " " + emojis[Math.floor(Math.random() * emojis.length)];

            document.getElementById("excuse").innerText = excuseText;
            speak(data.excuse); // speak Malayalam
        } else {
            document.getElementById("excuse").innerText = "Error: " + (data.error || "Unknown error");
        }
    } catch (error) {
        document.getElementById("excuse").innerText = "Error connecting to API";
    }
}
