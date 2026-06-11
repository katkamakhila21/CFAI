async function analyzeSort() {

    const input = document.getElementById("numbers").value.trim();

    if (input === "") {
        alert("Please enter some numbers");
        return;
    }

    try {

        const numbers = input
            .split(",")
            .map(num => Number(num.trim()));

        if (numbers.some(isNaN)) {
            throw new Error();
        }

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
            resultDiv.innerHTML =
                `<div class="error">${data.error}</div>`;
            return;
        }

        resultDiv.innerHTML = `

            <div class="card">

                <h2>Statistics</h2>

                <p><strong>Count:</strong> ${data.count}</p>
                <p><strong>Minimum:</strong> ${data.minimum}</p>
                <p><strong>Maximum:</strong> ${data.maximum}</p>
                <p><strong>Average:</strong> ${data.average}</p>

            </div>

            <div class="card winner-card">

                <h2>Faster Algorithm</h2>

                <p>${data.winner}</p>

            </div>

            <div class="card">

                <h2>Bubble Sort</h2>

                <p><strong>Time Complexity:</strong>
                ${data.bubble_complexity}</p>

                <p><strong>Execution Time:</strong>
                ${data.bubble_time} ms</p>

                <p><strong>Sorted Array:</strong>
                [${data.bubble_sorted.join(", ")}]</p>

            </div>

            <div class="card">

                <h2>Merge Sort</h2>

                <p><strong>Time Complexity:</strong>
                ${data.merge_complexity}</p>

                <p><strong>Execution Time:</strong>
                ${data.merge_time} ms</p>

                <p><strong>Sorted Array:</strong>
                [${data.merge_sorted.join(", ")}]</p>

            </div>

        `;
    }

    catch {

        document.getElementById("result").innerHTML =
            `<div class="error">
                Please enter valid numbers separated by commas.
             </div>`;
    }
}


function resetFields() {

    document.getElementById("numbers").value = "";

    document.getElementById("result").innerHTML = "";
}