with open("dane/symbole.txt") as file:
    symbols = file.read().split("\n")
symbols.pop()


def is_palindrome(text: str):
    for i in range(len(text)):
        left = text[i]
        right = text[-(i + 1)]
        if left != right:
            return False
    return True


def base_3_to_10(text: str):
    value = 0
    for i, symbol in enumerate(reversed(text)):
        match symbol:
            case '+':
                value += 1 * (3 ** i)
            case '*':
                value += 2 * (3 ** i)
    return value


def base_10_to_3(number: int):
    base_3_value = ""
    while number != 0:
        base_3_value += str(number % 3)
        number = number // 3

    return "".join(reversed(base_3_value.replace('0', 'o').replace('1', '+').replace('2', '*')))


print(symbols)

print("2.1")
for symbol in symbols:
    if is_palindrome(symbol):
        print(symbol)

print("\n\n2.2")

for i, line in enumerate(symbols):
    for j, symbol in enumerate(line):
        try:
            if (
                    symbol == symbols[i - 1][j - 1] and
                    symbol == symbols[i - 1][j] and
                    symbol == symbols[i - 1][j + 1] and
                    symbol == symbols[i][j - 1] and
                    symbol == symbols[i][j + 1] and
                    symbol == symbols[i + 1][j - 1] and
                    symbol == symbols[i + 1][j] and
                    symbol == symbols[i + 1][j + 1]
            ):
                print(i + 1, j + 1)
        except IndexError:
            pass

print("\n\n2.3")

converted_symbols = [base_3_to_10(symbol) for symbol in symbols]

print(max(converted_symbols))

print("\n\n2.4")
print(base_10_to_3(9))
print(sum(converted_symbols), base_10_to_3(sum(converted_symbols)))
