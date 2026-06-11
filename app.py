from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()

    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Merge Sort
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Linear Search
def linear_search(arr, target):

    for index, value in enumerate(arr):

        if value == target:
            return index

    return -1


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    numbers = data.get("numbers", [])

    if not numbers:
        return jsonify({"error": "Please enter numbers."})

    # Statistics
    minimum = min(numbers)
    maximum = max(numbers)
    average = round(sum(numbers) / len(numbers), 2)

    # Bubble Sort Timing
    start = time.perf_counter()
    bubble_sorted = bubble_sort(numbers)
    bubble_time = round((time.perf_counter() - start) * 1000, 6)

    # Merge Sort Timing
    start = time.perf_counter()
    merge_sorted = merge_sort(numbers)
    merge_time = round((time.perf_counter() - start) * 1000, 6)

    # Winner
    if merge_time < bubble_time:
        winner = "Merge Sort is faster"
    elif bubble_time < merge_time:
        winner = "Bubble Sort is faster"
    else:
        winner = "Both algorithms performed equally"

    search_result = ""
    search_position = -1

    search_value = data.get("search")

    if search_value != "" and search_value is not None:

        target = int(search_value)

        # Search in ORIGINAL ARRAY
        search_position = linear_search(numbers, target)

        if search_position != -1:
            search_result = f"{target} found"
        else:
            search_result = f"{target} not found"

    return jsonify({

        "count": len(numbers),
        "minimum": minimum,
        "maximum": maximum,
        "average": average,

        "bubble_sorted": bubble_sorted,
        "bubble_time": bubble_time,
        "bubble_complexity": "O(n²)",

        "merge_sorted": merge_sorted,
        "merge_time": merge_time,
        "merge_complexity": "O(n log n)",

        "winner": winner,

        "search_result": search_result,
        "search_position": search_position

    })


if __name__ == "__main__":
    app.run(debug=True)
