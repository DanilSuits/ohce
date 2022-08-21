from ohce.finite_state_machine import FiniteStateMachine


def anytime():
    return 0


def test_valediciton_includes_operators_name():
    fsm = FiniteStateMachine()
    fsm.on_input("ohce Pedro", anytime())
    fsm.on_input("Stop!", anytime())
    assert ["Adios Pedro"] == fsm.output()
