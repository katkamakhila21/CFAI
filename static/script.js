async function analyzeSort() {

    const input = document.getElementById("numbers").value;

    if(input.trim() === ""){
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

    if(data.error){
        resultDiv.innerHTML =
        `<p class="error">${data.error}</p>`;
        return;
    }

    let winner =
        data.bubble_time < data.merge_time
        ? "Bubble Sort 🚀"
        : "Merge Sort 🚀";

    resultDiv.innerHTML = `

    <div class="card winner-card">
        <h2>Faster Algorithm</h2>
        <p><strong>${winner}</strong></p>
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

    `;
}