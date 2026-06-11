let historyList = [];

async function analyzeSort() {

    const input = document.getElementById("numbers").value;

    if (input.trim() === "") {
        alert("Please enter some numbers");
        return;
    }

    const numbers = input.split(",").map(num => num.trim());

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            numbers: numbers
        })
    });

    const data = await response.json();

    const resultDiv = document.getElementById("result");

    if (data.error) {
        resultDiv.innerHTML = `
            <p class="error">${data.error}</p>
        `;
        return;
    }

    let winner =
        data.bubble_time < data.merge_time
            ? "Bubble Sort 🚀"
            : "Merge Sort 🚀";

    const currentTime = new Date().toLocaleTimeString();

    historyList.push({
        input: input,
        winner: winner,
        time: currentTime
    });

    resultDiv.innerHTML = `

    <div class="card stats-card">
        <h2>Input Statistics</h2>
        <p><strong>Total Numbers:</strong> ${data.count}</p>
        <p><strong>Minimum:</strong> ${data.minimum}</p>
        <p><strong>Maximum:</strong> ${data.maximum}</p>
        <p><strong>Average:</strong> ${data.average}</p>
    </div>

    <div class="card winner-card">
        <h2>Faster Algorithm</h2>
        <p><strong>${winner}</strong></p>
    </div>

    <div class="card insight-card">
        <h2>Performance Insight</h2>
        <p>${data.insight}</p>
    </div>

    <div class="card">
        <h2>Bubble Sort Results</h2>

        <p><strong>Sorted Array:</strong>
        ${data.bubble_sorted.join(", ")}</p>

        <p><strong>Execution Time:</strong>
        ${data.bubble_time} ms</p>

        <p><strong>Time Complexity:</strong>
        ${data.bubble_complexity}</p>
    </div>

    <div class="card">
        <h2>Merge Sort Results</h2>

        <p><strong>Sorted Array:</strong>
        ${data.merge_sorted.join(", ")}</p>

        <p><strong>Execution Time:</strong>
        ${data.merge_time} ms</p>

        <p><strong>Time Complexity:</strong>
        ${data.merge_complexity}</p>
    </div>

    ${getHistoryHTML()}
    `;
}

function getHistoryHTML() {

    if (historyList.length === 0) {
        return "";
    }

    let html = `
    <div class="card history-card">
        <h2>Sorting History</h2>
        <ul>
    `;

    historyList.forEach(item => {
        html += `
        <li>
            <strong>${item.time}</strong> |
            Winner: ${item.winner}
            <br>
            Input: ${item.input}
        </li>
        `;
    });

    html += `
        </ul>
    </div>
    `;

    return html;
}

function resetFields() {
    document.getElementById("numbers").value = "";
    document.getElementById("result").innerHTML = "";
}