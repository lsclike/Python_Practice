class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        numberLeft = []
        numberRight = []
        leftResult = 0
        rightResult = 0
        resultArray = []
        while l1 is not None:
            numberLeft.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            numberRight.append(l2.val)
            l2 = l2.next
        for n in range(len(numberLeft)):
            leftResult += numberLeft[n] * 10 ** n

        for n in range(len(numberRight)):
            rightResult += numberRight[n] * 10 ** n

        finalResult = leftResult + rightResult
        while (finalResult % 10 > 1):
            resultArray.append(finalResult % 10)
            finalResult = finalResult // 10

        firstNode = ListNode(resultArray[-1])
        for n in range(len(resultArray) - 2, -1, -1):
            newNode = ListNode(resultArray[n])
            newNode.next = firstNode
            firstNode = newNode

        return firstNode

def buildLinked(arr):
    firstNode = ListNode(arr[0])
    for t in range(1, len(arr)):
        newNode = ListNode(arr[t])
        newNode.next = firstNode
        firstNode = newNode

    return firstNode
def main():
    import sys
    import io
    test = [1,2,3]
    linkedList1 = buildLinked(test)
    linkedList2 = buildLinked(test)
    result = Solution().addTwoNumbers(linkedList1, linkedList2)
    while result:
        print(result.val, end=' ')
        result = result.next


if __name__ == '__main__':
    main()