def main():
    lines = open("01.txt").read().splitlines()

    firsts = []
    seconds = []
    for line in lines:
        pair = line.split()
        firsts.append(int(pair[0]))
        seconds.append(int(pair[1]))
    # p1(firsts, seconds)
    p2(firsts, seconds)


def p1(l1, l2):
    res = 0
    l1.sort()
    l2.sort()
    for i, v in enumerate(l1):
        res += abs(l1[i] - l2[i])
        print("current result:" + str(res))


def p2(l1, l2):
    res = 0

    for first in l1:
        loop_score = 0
        for second in l2:
            if first == second:
                loop_score += first
        res += loop_score

    print("result: " + str(res))


main()
