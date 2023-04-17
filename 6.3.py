import logging


def log(func):
    def wrapper(*args, **kw):
        logging.info("Calling function {} with args={}, kwargs={}".format(func.__name__, args, kw))
        logging.info("Function {} returned {}".format(func.__name__, func(*args, **kw)))
        return func(*args, **kw)

    return wrapper


logging.basicConfig(level=logging.INFO)


@log
def add(x, y):
    return x + y


result = add(2, 3)
