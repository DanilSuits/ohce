import time


class V20220820:
    @staticmethod
    def live(stdin=input, stdout=print, epoch_seconds=time.time):
        # TODO: notice that we haven't yet incorporated the
        #  connection to the clock.
        return V20220820.InteractiveLoop (
            V20220820.ReadOneLine(
                stdin
            ),
            V20220820.FlushLines(
                stdout
            ),
        )

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

