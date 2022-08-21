from ohce.finite_state_machine import FiniteStateMachine


def test_an_initialized_state_machine_is_running():
    fsm = FiniteStateMachine()
    assert fsm.running()


def anytime():
    return 0


def test_a_running_machine_stops_on_command():
    fsm = FiniteStateMachine()
    fsm.on_input(
        "Stop!",
        anytime()
    )
    assert not fsm.running()
