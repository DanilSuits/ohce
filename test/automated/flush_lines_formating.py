from ohce.v20220820 import V20220820


def kwargs():
    return V20220820.FlushLines.formatting()


def test_flush():
    """
    We care about this check because we want to be sure that
    output text is always flushed to the console before the
    operator is prompted for more input.
    """
    kw = kwargs()
    assert "flush" in kw
    assert kw["flush"] is True


def test_sep():
    """
    We care about this check because the message structure
    is intended to be a list of lines of output, so we
    want to ensure that multiple lines in the message
    are broken out across multiple lines, using pythons
    built in formatting.
    """
    kw = kwargs()
    assert "sep" in kw
    assert kw["sep"] == '\n'

