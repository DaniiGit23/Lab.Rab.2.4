#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.

    A = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    sum1 = 0
    count = 0
    for item in A:
        if item > 2 and item < 20 and item % 8 == 0:
            sum1 += item
            count += 1
    print("Сумма {0}".format(sum1))
    print("Количество {0}".format(count))
