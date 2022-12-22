import copy
import itertools
from sys import stdout
import time
import argparse

class Fasta:
    def __init__(self):
        self.name = ""
        self.sequence = ""


def read_fasta(file):
    name, seq = None, []
    for line in file:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield name, ''.join(seq)
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield name, ''.join(seq)


def parse(file_name):
    res = []
    with open(file_name) as f:
        for name, seq in read_fasta(f):
            record = Fasta()
            record.name = name
            record.sequence = seq
            res.append(record)
    return res


def sigma(a, b):
    return 5 if a == b else -4


def write_to_file(name, sequence, file):
    stream = file or stdout
    print(name, file=stream)
    print(sequence, file=stream)


def NW(a, b, gap=-5):
    n = len(a)
    m = len(b)

    D = [[0] * (m + 1) for _ in range(n + 1)]
    Ptr = [[0] * (m + 1) for _ in range(n + 1)]

    D[0][0] = 0
    Ptr[0][0] = 0

    for j in range(1, n + 1):
        D[j][0] = gap * j
        Ptr[j][0] = 2

    for i in range(1, m + 1):
        D[0][i] = gap * i
        Ptr[0][i] = 1

    for i, j in itertools.product(range(1, n + 1), range(1, m + 1)):
        delete = D[i - 1][j] + gap
        insert = D[i][j - 1] + gap
        match = D[i - 1][j - 1] + sigma(a[i - 1], b[j - 1])

        score_max = max(delete, insert, match)
        D[i][j] = score_max

        if score_max == insert:
            Ptr[i][j] = 1
        elif score_max == delete:
            Ptr[i][j] = 2
        elif score_max == match:
            Ptr[i][j] = 3

    counter = 0
    i = n
    j = m
    align_a = ['*'] * (n + m)
    align_b = ['*'] * (n + m)

    while i > 0 or j > 0:
        align_a[counter] = '-'
        align_b[counter] = '-'
        if j > 0 and Ptr[i][j] == 1:
            align_b[counter] = b[j - 1]
            j -= 1
            counter += 1
        elif i > 0 and Ptr[i][j] == 2:
            align_a[counter] = a[i - 1]
            i -= 1
            counter += 1
        elif i > 0 and j > 0 and Ptr[i][j] == 3:
            align_a[counter] = a[i - 1]
            align_b[counter] = b[j - 1]
            i -= 1
            j -= 1
            counter += 1

    align_a = align_a[::-1]
    align_b = align_b[::-1]

    score_num = D[n][m]

    return "".join(align_a).rstrip('*').strip('*'), "".join(align_b).rstrip('*').strip('*'), score_num


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', nargs='+', type=str)
    parser.add_argument('-o', type=str)
    parser.add_argument('-g', type=int)
    args = parser.parse_args()

    if len(args.i) == 1:
        records = parse(args.i[0])
        start = time.time()
        a, b, s = NW(records[0].sequence, records[1].sequence, args.g)
        end = time.time()
        print(end - start)
        with open(args.o, "w") as f:
            print(s, file=f)
            write_to_file("> out sequence 1", a, f)
            write_to_file("> out sequence 2", b, f)
    elif len(args.i) == 2:
        records = parse(args.i[0]) + parse(args.i[1])
        start = time.time()
        a, b, s = NW(records[0].sequence, records[1].sequence, args.g)
        end = time.time()
        print(end - start)

        with open(args.o, "w") as f:
            print(s, file=f)
            write_to_file("> out sequence 1", a, f)
            write_to_file("> out sequence 2", b, f)
    else:
        print('Too many files!')
