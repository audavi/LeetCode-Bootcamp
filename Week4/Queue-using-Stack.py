class MyQueue(object):

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.back.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.frontToBack()
        return self.front.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.frontToBack()
        return self.front[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.front) + len(self.back) == 0

    def frontToBack(self):
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()