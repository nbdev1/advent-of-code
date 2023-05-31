"""
https://adventofcode.com/2022/day/1
"""
from typing import List


def calorie_count(values: List[str]) -> int:
    cal = []
    for value in values:
        cal.append(sum(map(int, value.splitlines())))
    return sorted(cal)


if __name__ == '__main__':
    with open('input-1.txt', 'r') as f:
        input1 = f.read().split(sep='\n\n')

    print(f'Answer 1: {calorie_count(values=input1)[-1]}')
    print(f'Answer 2: {sum(calorie_count(values=input1)[-3:])}')