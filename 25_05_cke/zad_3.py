import math

with open("25_05_cke/dane/dron.txt") as file:
    moves = [(int(cord.split(' ')[0]), int(cord.split(' ')[1])) for cord in file.read().split("\n")[:-1]]

print(moves)

print('\n\n3.1')
count = 0
for move in moves:
    x, y = move
    if math.gcd(x, y) > 1:
        count += 1
print(count)

print("\n\n3.2\na)")
coordinates = [(0, 0)]
count = 0
for move in moves:
    x, y = move
    last_x, last_y = coordinates[-1]

    curr_x = last_x + x
    curr_y = last_y + y

    if (
            curr_x in range(0, 5000) and
            curr_y in range(0, 5000)
    ):
        count += 1
    coordinates.append((curr_x, curr_y))
print(count)


print("b)")
for i, first_cord in enumerate(coordinates):
    for second_cord in coordinates[i:]:
        if first_cord == second_cord:
            continue
        first_x, first_y = first_cord
        second_x, second_y = second_cord

        middle_cord = ((first_x + second_x) / 2, (first_y + second_y) / 2)
        if middle_cord in coordinates:
            print(f"{first_cord}, {middle_cord}, {second_cord}")
