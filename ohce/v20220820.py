import time


class V20220820:
    @staticmethod
    def live():
        # TODO: notice that we haven't yet incorporated the
        #  connection to the clock.
        return V20220820.InteractiveLoop (
            V20220820.ReadOneLine.live(),
            V20220820.FlushLines.live(),
            V20220820.EpochSeconds.live(),
        )

    class EpochSeconds:
        @staticmethod
        def live():
            return V20220820.EpochSeconds(time.time)

        def __init__(self, time):
            self.time = time

        def __call__(self):
            return self.epoch_seconds(
                self.time()
            )

        @staticmethod
        def epoch_seconds(now):
            return int(now)

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
            self.stdout_(
                *lines,
                **self.formatting()
            )

        @staticmethod
        def formatting(*, sep='\n', flush=True):
            return locals()

    class InteractiveLoop:
        def __init__(self, readOneLine, flushLines, epoch_seconds):
            pass

        def __call__(self):
            pass

