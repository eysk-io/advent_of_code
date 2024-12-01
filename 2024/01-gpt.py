import os
from collections import Counter


def main():
    lines = open(os.path.join(os.path.dirname(__file__),
                 "01.txt"), "r").read().splitlines()

    firsts = []
    seconds = []
    for line in lines:
        pair = line.split()
        firsts.append(int(pair[0]))
        seconds.append(int(pair[1]))
    p1(firsts, seconds)
    # p2(firsts, seconds)


def p1(l1, l2):
    left_sorted = sorted(l1)
    right_sorted = sorted(l2)

    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

    print(f"Total Distance: {total_distance}")


def p2(l1, l2):
    right_counts = Counter(l2)

    similarity_score = sum(num * right_counts[num] for num in l1)

    print(f"Similarity Score: {similarity_score}")


main()
