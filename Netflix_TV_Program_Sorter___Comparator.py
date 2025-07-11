import time
from typing import List, Dict, Callable

tv_shows = [
    {"title": "Stranger Things", "rating": 8.7, "episodes": 34, "runtime": 50},
    {"title": "Breaking Bad", "rating": 9.5, "episodes": 62, "runtime": 47},
    {"title": "The Crown", "rating": 8.6, "episodes": 40, "runtime": 58},
    {"title": "Money Heist", "rating": 8.2, "episodes": 41, "runtime": 45},
    {"title": "The Witcher", "rating": 8.1, "episodes": 16, "runtime": 59},
    {"title": "Wednesday", "rating": 8.1, "episodes": 8, "runtime": 48},
    {"title": "Dark", "rating": 8.8, "episodes": 26, "runtime": 53},
]

def bubble_sort(arr: List[Dict], key: str, reverse=False) -> List[Dict]:
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (a[j][key] > a[j + 1][key]) ^ reverse:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def merge_sort(arr: List[Dict], key: str, reverse=False) -> List[Dict]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, reverse)
    right = merge_sort(arr[mid:], key, reverse)
    return merge(left, right, key, reverse)

def merge(left: List[Dict], right: List[Dict], key: str, reverse=False) -> List[Dict]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if (left[i][key] < right[j][key]) ^ reverse:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr: List[Dict], key: str, reverse=False) -> List[Dict]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if (x[key] < pivot[key]) ^ reverse]
    right = [x for x in arr[1:] if (x[key] >= pivot[key]) ^ reverse]
    return quick_sort(left, key, reverse) + [pivot] + quick_sort(right, key, reverse)

def time_algorithm(algorithm: Callable, arr: List[Dict], key: str, reverse=False) -> (float, List[Dict]):
    start = time.time()
    result = algorithm(arr, key, reverse)
    end = time.time()
    return round(end - start, 6), result

def print_shows(title: str, shows: List[Dict]) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    for s in shows:
        print(f"{s['title']:<16} | Rating: {s['rating']:<3} | Episodes: {s['episodes']:<2} | Runtime: {s['runtime']} min")

def main():
    sort_key = input("Sort shows by (rating / episodes / runtime): ").strip().lower()
    if sort_key not in {"rating", "episodes", "runtime"}:
        print("Invalid sort key.")
        return

    order = input("Sort order? (asc / desc): ").strip().lower()
    reverse = order == "desc"

    algorithms = {
        'Bubble Sort': bubble_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort
    }

    times = {}
    sorted_results = {}

    for name, func in algorithms.items():
        duration, sorted_list = time_algorithm(func, tv_shows, sort_key, reverse)
        times[name] = duration
        sorted_results[name] = sorted_list
        print(f"{name} took {duration} seconds.")

    for name, result in sorted_results.items():
        print_shows(f"{name} Result (Sorted by {sort_key.title()}, {'Descending' if reverse else 'Ascending'})", result)

    try:
        import matplotlib.pyplot as plt
        plt.bar(times.keys(), times.values(), color='cornflowerblue')
        plt.title(f"Sort Time Comparison - Key: {sort_key}")
        plt.ylabel("Time (seconds)")
        plt.tight_layout()
        plt.show()
    except ImportError:
        print("Install matplotlib to see a time comparison chart: pip install matplotlib")

if __name__ == "__main__":
    main()


