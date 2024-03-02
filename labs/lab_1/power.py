# O(N) == log y
def power(x, y):
    if x == 0:
        return 0

    if y == 0:
        return 1

    if y > 0:
        return x * power(x, y - 1)
    else:
        return 1 / power(x, y * -1)


def betterPower(x, y):
    if y < 0:
        return 1 / betterPower(x, y * -1)
    if y == 0:
        return 1

    buffer = betterPower(x, y // 2)
    if y % 2 == 0:
        return buffer * buffer
    else:
        return buffer * buffer * x


sol = betterPower(2, 3)
print(sol)
