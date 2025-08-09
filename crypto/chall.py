import os
import secrets
import struct

from secret import flag


def rotl(x, r):
    return ((x << r) | (x >> (32 - r))) & 0xFFFFFFFF


def rotr(x, r):
    return ((x >> r) | (x << (32 - r))) & 0xFFFFFFFF


def speck64_encrypt(pt, key_words, rounds=2):
    x, y = (pt >> 32) & 0xFFFFFFFF, pt & 0xFFFFFFFF
    k = expand_key(key_words, rounds)

    for i in range(rounds):
        x = (rotr(x, 8) + y) & 0xFFFFFFFF
        x ^= k[i]
        y = rotl(y, 3) ^ x
    return (x << 32) | y


def expand_key(key_words, rounds=2):
    l = [key_words[1], key_words[2]]
    k = [key_words[0]]
    for i in range(rounds - 1):
        l.append((rotr(l[i], 8) + k[i]) ^ i)
        k.append(rotl(k[i], 3) ^ l[-1])
    return k


def main():
    keys = [secrets.randbits(32) for _ in range(3)]

    pairs = []
    for _ in range(2):
        pt = secrets.randbits(64)
        ct = speck64_encrypt(pt, keys, rounds=2)
        pairs.append((pt, ct))
    pt3 = secrets.randbits(64)
    ct3 = speck64_encrypt(pt3, keys, rounds=3)
    pairs.append((pt3, ct3))

    print(pairs)

    for idx in range(3):
        assert int(input()) == keys[idx]

    print(flag)


if __name__ == "__main__":
    main()
