from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    start_time = time.perf_counter()

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.perf_counter()

    return arr, round((end_time - start_time) * 1000, 6)


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


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    data = request.get_json()

    try:
        numbers = list(map(int, data['numbers']))

        bubble_sorted, bubble_time = bubble_sort(numbers)

        start = time.perf_counter()
        merge_sorted = merge_sort(numbers)
        end = time.perf_counter()

        merge_time = round((end - start) * 1000, 6)

        return jsonify({
            "bubble_sorted": bubble_sorted,
            "bubble_time": bubble_time,
            "bubble_complexity": "O(n²)",

            "merge_sorted": merge_sorted,
            "merge_time": merge_time,
            "merge_complexity": "O(n log n)"
        })

    except:
        return jsonify({
            "error": "Please enter valid numbers."
        })


if __name__ == "__main__":
    app.run(debug=True)