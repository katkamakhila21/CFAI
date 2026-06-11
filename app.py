from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)


# Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()

    start = time.perf_counter()

    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    end = time.perf_counter()

    return arr, round((end - start) * 1000, 6)


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        numbers = list(map(int, data["numbers"]))

        # Bubble Sort
        bubble_sorted, bubble_time = bubble_sort(numbers)

        # Merge Sort
        start = time.perf_counter()
        merge_sorted = merge_sort(numbers)
        end = time.perf_counter()

        merge_time = round((end - start) * 1000, 6)

        # Statistics
        count = len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        average = round(sum(numbers) / count, 2)

        # Faster Algorithm
        if bubble_time < merge_time:
            winner = "Bubble Sort"
        elif merge_time < bubble_time:
            winner = "Merge Sort"
        else:
            winner = "Both performed similarly"

        return jsonify({
            "bubble_sorted": bubble_sorted,
            "bubble_time": bubble_time,
            "bubble_complexity": "O(n²)",

            "merge_sorted": merge_sorted,
            "merge_time": merge_time,
            "merge_complexity": "O(n log n)",

            "count": count,
            "minimum": minimum,
            "maximum": maximum,
            "average": average,

            "winner": winner
        })

    except:
        return jsonify({
            "error": "Please enter valid numbers separated by commas."
        })


if __name__ == "__main__":
    app.run(debug=True)