import random
import secrets
from collections import Counter

def rotl(x, r):
    return ((x << r) | (x >> (32 - r))) & 0xFFFFFFFF

def rotr(x, r):
    return ((x >> r) | (x << (32 - r))) & 0xFFFFFFFF

def expand_key(key_words, rounds=5):
    l = [key_words[1], key_words[2]]
    k = [key_words[0]]
    for i in range(rounds - 1):
        l.append((rotr(l[i], 8) + k[i]) ^ i)
        k.append(rotl(k[i], 3) ^ l[-1])
    return k

def speck64_encrypt(pt, key_words, rounds=5):
    x, y = (pt >> 32) & 0xFFFFFFFF, pt & 0xFFFFFFFF
    round_keys = expand_key(key_words, rounds)
    for i in range(rounds):
        x = (rotr(x, 8) + y) & 0xFFFFFFFF
        x ^= round_keys[i]
        y = rotl(y, 3) ^ x
    return (x << 32) | y

def partial_decrypt_last_round(ct, last_round_key):
    x, y = (ct >> 32) & 0xFFFFFFFF, ct & 0xFFFFFFFF
    y ^= x
    y = rotr(y, 3)
    x ^= last_round_key
    x = ((x - y) & 0xFFFFFFFF)
    x = rotl(x, 8)
    return (x << 32) | y

# Step 1: 키 생성 및 round 수 설정
rounds = 5
key = [secrets.randbits(32) for _ in range(3)]
round_keys = expand_key(key, rounds)
true_last_round_key = round_keys[-1]

# Step 2: input difference 선택 (잘 알려진 ΔP)
input_diff = 0x8080000000000000

# Step 3: 쌍 생성 및 차분 통계 분석
def generate_diff_pairs_and_stats(input_diff, num_pairs=10000):
    counter = Counter()
    pairs = []
    for _ in range(num_pairs):
        pt1 = secrets.randbits(64)
        pt2 = pt1 ^ input_diff
        ct1 = speck64_encrypt(pt1, key, rounds)
        ct2 = speck64_encrypt(pt2, key, rounds)
        output_diff = ct1 ^ ct2
        counter[output_diff] += 1
        pairs.append((ct1, ct2))
    return pairs, counter

pairs, diff_counter = generate_diff_pairs_and_stats(input_diff)

# Step 4: 가장 자주 나오는 ΔC 선택
expected_output_diff = diff_counter.most_common(1)[0][0]
print(f"[+] Most frequent ΔC: {hex(expected_output_diff)}")

# Step 5: 마지막 라운드 키 후보 평가
def score_key_candidate(pairs, candidate_key, expected_output_diff):
    score = 0
    for ct1, ct2 in pairs:
        u1 = partial_decrypt_last_round(ct1, candidate_key)
        u2 = partial_decrypt_last_round(ct2, candidate_key)
        if (u1 ^ u2) == expected_output_diff:
            score += 1
    return score

def recover_last_round_key(pairs, expected_output_diff):
    best_score = -1
    best_key = None
    for k in range(0x00000000, 0x00010000):  # 16비트 후보 (속도 위해)
        score = score_key_candidate(pairs, k, expected_output_diff)
        if score > best_score:
            best_score = score
            best_key = k
    return best_key, best_score

recovered_key, score = recover_last_round_key(pairs, expected_output_diff)
print(f"[+] Recovered last round key: {hex(recovered_key)} (score={score})")
print(f"[✔] True last round key: {hex(true_last_round_key)}")
