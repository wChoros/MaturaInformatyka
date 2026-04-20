with open('dane/prostokaty_przyklad.txt') as f:
    prostokaty = [[int(prostokat.split()[0]), int(prostokat.split()[1])] for prostokat in f.read().splitlines()]

print("4.1\n")
smallest = prostokaty[0][0] * prostokaty[0][1]
biggest = prostokaty[0][1] * prostokaty[0][1]

for h, w in prostokaty:
    if h * w > biggest:
        biggest = h * w
    if h * w < smallest:
        smallest = h * w

print(f"Najmniejsze pole: {smallest}\nNajwieksze pole: {biggest}")

print("4.2\n")
current_streak_length = 0
biggest_streak = 0
biggest_streak_w = None
biggest_streak_h = None


for i, prostokat in enumerate(prostokaty):
    if current_streak_length == 0:
        current_streak_length += 1
        continue
    if prostokat[0]<=prostokaty[i-1][0] and prostokat[1]<=prostokaty[i-1][1]:
        current_streak_length += 1
    else:
        if current_streak_length > biggest_streak:
            biggest_streak = current_streak_length
            biggest_streak_w = prostokaty[i-1][0]
            biggest_streak_h = prostokaty[i-1][1]
        current_streak_length = 0
print(biggest_streak)
print(biggest_streak_w)
print(biggest_streak_h)