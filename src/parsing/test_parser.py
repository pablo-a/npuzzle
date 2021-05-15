import parsing.parser as parser


def test_line_is_comment():
    assert (parser.line_is_comment("  # hello you")) is True
    assert (parser.line_is_comment(" - hello you")) is True
    assert (parser.line_is_comment("# hello you")) is True
    assert (parser.line_is_comment("  123 # hello you")) is False
    assert (parser.line_is_comment("  12- hello you")) is False


def test_line_is_puzzle_size():
    assert (parser.line_is_puzzle_size("3")) is True
    assert (parser.line_is_puzzle_size("42 # whatever")) is True
    assert (parser.line_is_puzzle_size("#123123")) is False
    assert (parser.line_is_puzzle_size("   42 #comment")) is True
    assert (parser.line_is_puzzle_size("   asd123")) is False


def test_line_is_puzzle_content():
    assert (parser.line_is_puzzle_content(" 1 2 3 ", 3)) is True
    assert (parser.line_is_puzzle_content(" 1 2   3   4", 4)) is True
    assert (parser.line_is_puzzle_content(" 1 2 3 4 5", 5)) is True
    assert (parser.line_is_puzzle_content(" 1 a 3 ", 3)) is False
    assert (parser.line_is_puzzle_content(" 1 2 3 4", 3)) is False
    assert (parser.line_is_puzzle_content("", 3)) is False


def test_get_puzzle_row():
    assert (parser.get_puzzle_row(3, "1 2 3 # comment")) == [1, 2, 3]
    assert (parser.get_puzzle_row(3, "11 12 13")) == [11, 12, 13]
    assert (parser.get_puzzle_row(4, "1 2 3 4")) == [1, 2, 3, 4]
    assert (parser.get_puzzle_row(3, "1    2    3 # 44")) == [1, 2, 3]


def test_get_puzzle_size():
    assert (parser.get_puzzle_size("     3    #comment")) == 3
    assert (parser.get_puzzle_size("   4    #comment")) == 4
    assert (parser.get_puzzle_size("     42    #comment")) == 42
