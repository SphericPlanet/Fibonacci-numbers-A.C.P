def fibonacci_series(n):
    series = [0, 1]
    for i in range(2, n):
        next_term = series[i-1] + series[i-2]
        series.append(next_term)
    return series[:n]

n = int(input("Enter the number of terms in the Fibonacci series: "))

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci series up to {n} terms: [0]")
else:
    print(f"Fibonacci series up to {n} terms: {fibonacci_series(n)}")
