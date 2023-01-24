#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        max = [0, None]
        return max
    else:
        max = [len(sentence), sentence[0]]
        return max
