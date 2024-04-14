def raise_exception():
    try:
        raise TypeError
    except TypeError as e:
        raise e
