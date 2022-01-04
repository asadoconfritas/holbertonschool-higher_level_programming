#!/usr/bin/python3
def multiple_returns(sentence):
    lar = len(sentence)
    return lar, sentence[0] if lar > 0 else None
