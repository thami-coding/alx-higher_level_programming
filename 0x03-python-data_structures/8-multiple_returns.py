#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = str(sentence or None)
    return (len(sentence), sentence[0:1])
