def separate_squares(start, end):
    squares = [num ** 2 for num in range(start, end + 1)]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    return even_squares, odd_squares

# User input for range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

even_squares, odd_squares = separate_squares(start, end)

print(f"Even square values: {even_squares}")
print(f"Odd square values: {odd_squares}")
