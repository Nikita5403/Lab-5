numbers = list(map(int, input("Enter a space-separated list of numbers:").split()))
unique_sorted = sorted(set(numbers))
print(f"Second smallest element: {unique_sorted[1]}")