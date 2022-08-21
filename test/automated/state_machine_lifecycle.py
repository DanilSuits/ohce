from ohce.finite_state_machine import FiniteStateMachine


def test_an_initialized_state_machine_is_running():
    fsm = FiniteStateMachine()
    assert fsm.running()


class Adapter:
    def __init__(self, fsm):
        self.fsm = fsm

    def on_input(self, line):
        self.fsm.on_input(line, self.anytime())

    @staticmethod
    def anytime():
        return 0


def test_a_running_machine_stops_on_command():
    fsm = FiniteStateMachine()
    adapter = Adapter(fsm)
    adapter.on_input(
        "Stop!"
    )
    assert not fsm.running()
