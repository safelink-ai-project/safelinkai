document.getElementById("scanBtn").addEventListener("click", async () => {

    const url = document.getElementById("urlInput").value;

    if (!url) {
        alert("Please enter a URL");
        return;
    }

    document.getElementById("result").classList.add("hidden");

    const response = await fetch(`http://127.0.0.1:8000/scan?url=${encodeURIComponent(url)}`);

    const data = await response.json();

    document.getElementById("status").textContent = data.status;
    document.getElementById("riskScore").textContent = data.risk_score;

    const heuristicList = document.getElementById("heuristicFlags");
    heuristicList.innerHTML = "";
    data.heuristic_flags.forEach(flag => {
        const li = document.createElement("li");
        li.textContent = flag;
        heuristicList.appendChild(li);
    });

    const behaviourList = document.getElementById("behaviourFlags");
    behaviourList.innerHTML = "";
    data.behaviour_flags.forEach(flag => {
        const li = document.createElement("li");
        li.textContent = flag;
        behaviourList.appendChild(li);
    });

    document.getElementById("pageTitle").textContent = data.page_info.title || "N/A";
    document.getElementById("formsCount").textContent = data.page_info.forms || 0;
    document.getElementById("passwordFields").textContent = data.page_info.password_fields || 0;
    document.getElementById("scriptsCount").textContent = data.page_info.scripts || 0;

    // Show screenshot if available
    if (data.page_info.error) {
        document.getElementById("screenshot").style.display = "none";
    } else {
        document.getElementById("screenshot").src = "scan.png";
        document.getElementById("screenshot").style.display = "block";
    }

    document.getElementById("result").classList.remove("hidden");
});