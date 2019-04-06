
from deque import Deque

def is_palindrome(item):
    """palindrome with deque"""
    deque = Deque()
    for i in range(len(item)):
        deque.addTail(item[i])
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True   