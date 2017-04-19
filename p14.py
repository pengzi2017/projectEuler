def calc(n):
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1


def count_item(n):
    count = 0
    n = 2
    while n != 1:
        calc(n)
        count += 1
    return count


def main():
    m = 1
    for i in range(1000000):
        m1 = count_item()
        if m < m1:
            m = m1
    print m
