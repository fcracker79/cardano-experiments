def check_assertion_enabled():
    try:
        assert False
        # noinspection PyUnreachableCode
        raise ValueError('Please enable assertions')
    except AssertionError:
        return
