# 🔍 SortScope

An interactive web application to compare the performance of **Bubble Sort** and **Merge Sort** algorithms.

## ✨ Features

- **Algorithm Comparison**: Real-time execution time comparison
- **Performance Metrics**: View execution times in milliseconds
- **Input Statistics**: Get min, max, average, and count of numbers
- **Complexity Analysis**: See theoretical and practical time complexities
- **History Tracking**: Keep track of all analyses
- **CSV Export**: Export sorting history as CSV file
- **Clean UI**: Modern, responsive design

## 🛠️ Technologies

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Algorithms**: Bubble Sort, Merge Sort

## 🚀 Quick Start

### Requirements
- Python 3.7+
- Flask

### Installation

```bash
pip install flask
```

### Run

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## 📊 How It Works

1. Enter a list of numbers separated by commas
2. Click "Analyze" to compare sorting algorithms
3. View real-time execution times and statistics
4. Export history as CSV for records

## 📈 Algorithm Complexity

| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |

