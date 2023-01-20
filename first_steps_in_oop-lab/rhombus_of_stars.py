def rhombus_of_stars(star_row, size):
    print(" " * (size - star_row), end="")
    for col in range(1, star_row + 1):
        print("* ", end="")
    print()


n = int(input())

for row in range(n + 1):
    rhombus_of_stars(row, n)

for row in range(n - 1, -1, -1):
    rhombus_of_stars(row, n)
