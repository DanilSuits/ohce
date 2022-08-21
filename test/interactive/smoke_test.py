from ohce.v20220820 import V20220820


flush_lines = V20220820.FlushLines.live()
read_one_line = V20220820.ReadOneLine.live()
epoch_seconds = V20220820.EpochSeconds.live()

flush_lines([
    str(epoch_seconds()),
    "Tell me your name:",
])
line = read_one_line()
flush_lines([
    "ohce",
    line,
    line,
])