def generate_series(a):
    series = []
    num = 1
    while len(series) < a:
        series.append(num)
        num += 2
    return series

# Test the function
a = int(input("Enter a number: "))
print(*generate_series(a))
