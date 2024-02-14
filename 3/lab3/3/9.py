matrix = [
    [1, 3, 3, 8],
    [4, 5, 6, 7],
    [7, 9, 10, 1]
]

max_sum = 0
row = 0
for i in range(len(matrix)):
    summary = sum(matrix[i])
    print(summary)
    if summary > max_sum:
        max_sum = summary
        row = i
print("Max sum is: ", max_sum, " in row: ", row)

