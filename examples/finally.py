def third_time_always_works(filename):
    try:
        return open(filename)
    except:
        return open(filename)
    # This does not even compile in some languages
    finally:
        return open(filename)
