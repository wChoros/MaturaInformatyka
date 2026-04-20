with open("./dane/liczby.txt") as file:
    liczby = [int(liczba) for liczba in file.read().splitlines()]


def is_sqrt(number):
    for i in range(1, number):
        if i ** 2 == number:
            return True
    return False


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_num_of_dividers(liczba):
    c = 0
    for i in range(2, liczba):
        if not is_prime(i):
            continue
        if liczba % i == 0:
            c += 1
    return c


def get_smallest_from_num(liczba):
    l = list(str(liczba))
    l.sort()
    return int("".join(l))


def get_biggest_from_num(liczba):
    l = list(str(liczba))
    l.sort()
    l.reverse()
    return int("".join(l))


print("3.1\n")
count = 0
for liczba in liczby:
    if is_sqrt(liczba) and count == 0:
        print(f"Pierwsza liczba to: {liczba}")
        count += 1
    elif is_sqrt(liczba):
        count += 1
print(f"Są {count} kwadraty")

print("\n\n3.2\n")
for liczba in liczby:
    if get_num_of_dividers(liczba) >= 5:
        print(liczba)

print("\n\n3.3\n")
bigger_count = 0
smaller_count = 0
equal_count = 0
for liczba in liczby:
    x = get_biggest_from_num(liczba) - get_smallest_from_num(liczba)
    if x > liczba:
        bigger_count += 1
    elif x < liczba:
        smaller_count += 1
    else:
        equal_count += 1
        print(liczba)
print(f"Mniejsza: {smaller_count}, wieksza: {bigger_count}, rowna: {equal_count}")
