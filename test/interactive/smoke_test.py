from ohce.v20220820 import V20220820


flush_lines = V20220820.FlushLines.live()
read_one_line = V20220820.ReadOneLine.live()

flush_lines(["Tell me your name:"])
line = read_one_line()
flush_lines([
    "ohce",
    line,
    line,
])