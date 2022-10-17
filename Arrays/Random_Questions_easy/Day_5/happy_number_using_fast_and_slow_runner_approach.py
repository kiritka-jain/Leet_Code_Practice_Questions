n = int(input())


def isHAppy(n):
    def get_next_num(n):
        digits_sum = 0
        while n > 0:
            for digit in str(n):
                digits_sum += int(digit) * int(digit)
            return digits_sum

    slow_pointer = n
    fast_pointer = get_next_num(n)
    while fast_pointer != 1 and slow_pointer != fast_pointer:
        slow_pointer = get_next_num(slow_pointer)
        fast_pointer = get_next_num(get_next_num(fast_pointer))
    return fast_pointer


if isHAppy(n) == 1:
    print(True)
else:
    print(False)
