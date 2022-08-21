import time


class V20220820:
    @staticmethod
    def live():
        # TODO: notice that we haven't yet incorporated the
        #  connection to the clock.
        return V20220820.InteractiveLoop.build (
            V20220820.ReadOneLine.live(),
            V20220820.FlushLines.live(),
            V20220820.EpochSeconds.live(),
            V20220820.FiniteStateMachine()
        )

    class FiniteStateMachine:
        def running(self):
            return False

        def on_input(self, line, now):
            pass

        def output(self):
            return None

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
        @staticmethod
        def build(read_one_line, flush_lines, epoch_seconds, fsm):
            return V20220820.InteractiveLoop(
                read_one_line,
                flush_lines,
                epoch_seconds,
                fsm.running,
                fsm.on_input,
                fsm.output
            )

        def __init__(self, read_one_line, flush_lines, epoch_seconds, running, on_input, output):
            self.read_one_line = read_one_line
            self.flush_lines = flush_lines
            self.epoch_seconds = epoch_seconds
            self.running = running
            self.on_input = on_input
            self.output = output

        def __call__(self):
            while self.running():
                line = self.read_one_line()
                now = self.epoch_seconds()

                self.on_input(line, now)

                output = self.output()
                self.flush_lines(output)

