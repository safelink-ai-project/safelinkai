document.getElementById("scanBtn").addEventListener("click", async () => {

    let url = document.getElementById("urlInput").value;

    if (!url) {
        // Get current tab URL
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        url = tab.url;
    }

    if (!url) return alert("No URL detected");

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Scanning...";

    try {
        const response = await fetch(`http://safelinkai-production.up.railway.app/scan?url=${encodeURIComponent(url)}`);
        const data = await response.json();

        resultDiv.innerHTML = `
            <strong>Status:</strong> ${data.status}<br>
            <strong>Risk Score:</strong> ${data.risk_score}<br>
            <strong>Heuristic Flags:</strong> ${data.heuristic_flags.join(", ") || "None"}<br>
            <strong>Behaviour Flags:</strong> ${data.behaviour_flags.join(", ") || "None"}
        `;
    } catch (error) {
        resultDiv.innerHTML = "Error connecting to SafeLink AI API.";
        console.error(error);
    }
});
