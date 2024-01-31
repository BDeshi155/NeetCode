class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue(object):

    def __init__(self, k:int):
        self.space = k
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        node = ListNode(value)
        next = self.right
        prev = self.right.prev

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        node = ListNode(0)
        next = self.left.next
        prev = self.left

        next.prev = prev
        prev.next = next

        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()