"""
https://adventofcode.com/2022/day/1
"""
from typing import List


def calorie_count(values: List[str]) -> int:
    a, b = 0, 0

    for line in values:
        if line != '':
            b += int(line)
        else:
            if b > a:
                a = b
            b = 0
    return a


def top_3_calorie_count(values: List[str]) -> int:
    a = [0]
    i = 0
    for line in values:
        if line != '':
            a[i] += int(line)
        else:
            a.append(0)
            i += 1
    a.sort()
    return sum(a[-3:])


if __name__ == '__main__':
    with open('input-1.txt', 'r') as f:
        input1 = f.read().split(sep='\n')

    print(f'Answer 1: {calorie_count(input1)}')
    print(f'Answer 2: {top_3_calorie_count(input1)}')