import logging
import threading
import time


def core_func(id: str) -> None:
    logging.info(f"Thread {id} is starting")
    time.sleep(2)
    logging.info(f"Thread {id} is finishing")


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


def thread_factory():
    return threading.Thread(target=core_func, args=("1",))


def daemon_thread_factory():
    return threading.Thread(target=core_func, args=("1",), daemon=True)


if __name__ == "__main__":
    threads = list()

    for i in range(3):
        logging.info(f"Main: create thread {i}")
        t = thread_factory()
        threads.append(t)
        t.start()

    for i, t in enumerate(threads):
        logging.info(f"Main: before joining thread {i}")
        t.join()
        logging.info(f"Main: thread {i} done")
