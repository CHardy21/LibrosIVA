# session.py
session = {}
observers = []


def add_observer(observer):
    observers.append(observer)


def remove_observer(observer):
    if observer in observers:
        observers.remove(observer)


def notify_observers():
    for observer in observers:
        observer.update_session()
