import nw.align as align


def test_nw_1():
    aln1, aln2, score = align.NW("ACGT", "ACGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "ACGT"
    assert score == 20


def test_nw_2():
    aln1, aln2, score = align.NW("ACG", "ACGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "ACG-"
    assert aln2 == "ACGT"
    assert score == 10


def test_nw_3():
    aln1, aln2, score = align.NW("ACGT", "ACG")
    assert len(aln1) == len(aln2)
    assert aln1 == "ACGT"
    assert aln2 == "ACG-"
    assert score == 10


def test_nw_4():
    aln1, aln2, score = align.NW("ACAGT", "ACGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "ACAGT"
    assert aln2 == "AC-GT"
    assert score == 15


def test_nw_5():
    aln1, aln2, score = align.NW("ACGT", "ACAGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "AC-GT"
    assert aln2 == "ACAGT"
    assert score == 15


def test_nw_6():
    aln1, aln2, score = align.NW("CAGT", "ACAGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "-CAGT"
    assert aln2 == "ACAGT"
    assert score == 15


def test_nw_7():
    aln1, aln2, score = align.NW("ACAGT", "CAGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "ACAGT"
    assert aln2 == "-CAGT"
    assert score == 15


def test_nw_8():
    aln1, aln2, score = align.NW("ACGT", "A")
    assert len(aln1) == len(aln2)
    assert aln1 == "ACGT"
    assert aln2 == "A---"
    assert score == -10


def test_nw_9():
    aln1, aln2, score = align.NW("ACGT", "")
    assert len(aln1) == len(aln2)
    assert aln1 == "ACGT"
    assert aln2 == "----"
    assert score == -20


def test_nw_10():
    aln1, aln2, score = align.NW("A", "ACGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "A---"
    assert aln2 == "ACGT"
    assert score == -10


def test_nw_11():
    aln1, aln2, score = align.NW("", "ACGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "----"
    assert aln2 == "ACGT"
    assert score == -20


def test_nw_12():
    aln1, aln2, score = align.NW("", "")
    assert aln1 == ""
    assert aln2 == ""
    assert score == 0


def test_nw_13():
    aln1, aln2, score = align.NW("TACGT", "ATGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "TACGT"
    assert aln2 == "-ATGT"
    assert score == 6


def test_nw_14():
    aln1, aln2, score = align.NW("TACGT", "ACTGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "TAC-GT"
    assert aln2 == "-ACTGT"
    assert score == 10


def test_nw_15():
    aln1, aln2, score = align.NW("ACGT", "TAGTA")
    assert len(aln1) == len(aln2)
    assert aln1 == "-ACGT-"
    assert aln2 == "TA-GTA"
    assert score == 0


def test_nw_16():
    aln1, aln2, score = align.NW("TAGTA", "ACGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "TA-GTA"
    assert aln2 == "-ACGT-"
    assert score == 0


def test_nw_17():
    aln1, aln2, score = align.NW("ACGT", "TAGT", gap=0)
    assert len(aln1) == len(aln2)
    assert aln1 == "-ACGT"
    assert aln2 == "TA-GT"
    assert score == 15


def test_nw_18():
    aln1, aln2, score = align.NW("TAGT", "ACGT", gap=10)
    assert len(aln1) == len(aln2)
    assert len(aln1) == 8
    assert score == 80


def test_nw_19():
    aln1, aln2, score = align.NW("GGAGCCAAGGTGAAGTTGTAGCAGTGTGTCC", "GACTTGTGGAACCTCTGTCCTCCGAGCTCTC",
                                         gap=-5)
    assert len(aln1) == len(aln2)
    assert len(aln1) == 36
    assert score == 8


def test_nw_20():
    aln1, aln2, score = align.NW("AAAAAAATTTTTTT", "TTTTTTTAAAAAAA", gap=-5)
    assert len(aln1) == len(aln2)
    assert len(aln1) == 21
    assert score == -35


for i in range(1, 21):
    eval(f'test_nw_{i}()')