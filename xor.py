import itertools


def bXor(*, msg: str, key: str) -> str:
    result = ""
    for m, k in zip(msg, itertools.cycle(key)):
        if m == k:
            result += "0"
        else:
            result += "1"
    return result


msg = str(input("Message? "))

key = str(input("Key? "))

print(bXor(msg=msg, key=key))