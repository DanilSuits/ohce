class V20220820:
    class ReadOneLine:
        def __init__(self, stdin):
            self.stdin_ = stdin

        def __call__(self):
            return self.stdin_()

    class FlushLines:
        def __init__(self, stdout):
            self.stdout_ = stdout

        def __call__(self, lines):
            self.stdout_(lines, flush=True)

    class InteractiveLoop:
        def __init__(self, readOneLine, flushLines):
            pass

        def __call__(self):
            pass


    @staticmethod
    def interactive_loop(*, stdin, stdout, epoch_seconds):
        read_one_line = V20220820.ReadOneLine(stdin)
        flush_lines = V20220820.FlushLines(stdout)

        return V20220820.InteractiveLoop(
            read_one_line,
            flush_lines
        )
