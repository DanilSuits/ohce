class FiniteStateMachine:
    def __init__(self, *, running=True):
        self.running_ = running

    def running(self):
        return self.running_

    def on_input(self, line, now):
        if "Stop!" == line:
            self.running_ = False

    def output(self):
        if self.running_:
            return []
        else:
            return ["Adios Pedro"]
