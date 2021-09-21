#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List


def get_num_letters(text: str) -> int:
    return sum(c.isalnum() for c in text)


def get_word_length_histogram(text: str) -> List[int]:
    num_letters = [get_num_letters(word) for word in text.split()]
    histogram = [0] * (max(num_letters) + 1)
    for n in num_letters:
        histogram[n] += 1
    return histogram


def format_histogram(histogram: List[int]) -> str:
    ROW_CHAR = "*"
    text = ""

    for i, n in enumerate(histogram[1:]):
        text += f"{i+1: >2} {ROW_CHAR * n}\n"

    return text


def format_horizontal_histogram(histogram: List[int]) -> str:
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"

    histogram = histogram[1:]
    text = ""

    for i in range(max(histogram), 0, -1):
        for n in histogram:
            text += BLOCK_CHAR if i <= n else " "
        text += "\n"

    return text + LINE_CHAR * (len(histogram) + 1)


if __name__ == "__main__":
    spam = "Stop right there criminal scum! shouted the guard confidently."
    eggs = get_word_length_histogram(spam)
    print(eggs, "\n")
    print(format_histogram(eggs), "\n")
    print(format_horizontal_histogram(eggs))
