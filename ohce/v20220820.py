import time


class V20220820:
    @staticmethod
    def live():
        # TODO: notice that we haven't yet incorporated the
        #  connection to the clock.
        return V20220820.InteractiveLoop (
            V20220820.ReadOneLine.live(),
            V20220820.FlushLines.live()
        )

    class ReadOneLine:
        @staticmethod
        def live():
            return V20220820.ReadOneLine(input)

        def __init__(self, stdin):
            self.stdin_ = stdin

        def __call__(self):
            return self.stdin_()

    class FlushLines:
        @staticmethod
        def live():
            return V20220820.FlushLines(print)

        def __init__(self, stdout):
            self.stdout_ = stdout

        def __call__(self, lines):
            self.stdout_(lines, flush=True)

    class InteractiveLoop:
        def __init__(self, read_one_line, flush_lines):
            self.read_one_line = read_one_line.__call__
            self.flush_lines = flush_lines.__call__

        def __call__(self):
            line = self.read_one_line()
            self.flush_lines("%s\n%s" % (line, line))


