import time


def timed(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        output = fn(*args, **kwargs)
        print(fn.__name__, time.time() - start)
        return output

    return wrapper


@timed
def train_model():
    time.sleep(0.1)
    return "Training complete"


if __name__ == "__main__":
    print(train_model())
