import re

lookup_table = {
    "1": [1],
    "2": [2],
    "3": [3],
    "4": [4],
    "5": [5],
    "6": [6],
    "7": [7],
    "8": [8],
    "9": [9],
    "threeight": [3, 8],
    "eighthree": [8, 3],
    "eightwo": [8, 2],
    "sevenine": [7, 9],
    "nineight": [9, 8],
    "fiveight": [5, 8],
    "oneight": [1, 8],
    "twone": [2, 1],
    "three": [3],
    "eight": [8],
    "seven": [7],
    "four": [4],
    "five": [5],
    "nine": [9],
    "one": [1],
    "two": [2],
    "six": [6],
}

matcher = re.compile(f"(?:{'|'.join(lookup_table.keys())})")
# Initially I used the following and no lookup table, but it felt like a hack as it makes use
# of a quirk in python's regexp parsing of positive lookaheads, and I wasn't sure how fair that was.
# matcher = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
result_sum = 0
with open("input.txt") as f:
    for line in f:
        matches = matcher.findall(line)
        first, last = (lookup_table[matches[0]][0], lookup_table[matches[-1]][-1])
        if matches:
            result_sum += first * 10 + last

print(result_sum)
