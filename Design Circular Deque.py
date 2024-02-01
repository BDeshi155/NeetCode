class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque(object):

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        node = ListNode(value)
        next = self.left.next
        prev = self.left

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

        self.space -= 1
        return True

    def insertLast(self, value: int) -> bool:
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

    def deleteFront(self)->bool:
        if self.isEmpty(): return False

        node = ListNode(0)
        next = self.left.next
        prev = self.left

        next.prev = prev
        prev.next = next

        self.space += 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False

        node = ListNode(0)
        next = self.right
        prev = self.right.prev

        next.prev = prev
        prev.next = next

        self.space += 1
        return True



    def getFront(self)->int:
        if self.isEmpty(): return -1

        return self.left.next.val

    def getRear(self) -> int:
        if self.isEmpty(): return -1

        return self.right.prev.val


    def isEmpty(self):
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()