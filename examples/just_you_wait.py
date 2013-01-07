# a short guide how to make sure tests run as quick as possible

import time

time_elapsed = None


def track_time(f, *args, **kwargs):

    def inner():
        global time_elapsed
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        time_elapsed = end - start
        return result

    return inner


def test_track_time():
    seconds = 2

    @track_time
    def a_function():
        time.sleep(seconds)

    a_function()

    assert int(time_elapsed) == seconds
