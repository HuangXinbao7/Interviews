'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


class ListNode:
    """单链表的结点"""
    def __init__(self, item):
        self.val = item
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0                   # 记录是否增加新结点，或在链表下一个结点是否需要加1，同时记录链表同级结点的和
        res = pre = ListNode(0)     # 这里的执行顺序是 res = ListNode(0), pre = res

        while l1 or l2 or carry:    # 判断l1 l2 carry 是否有值，carry有值的话需要增加新结点，或在链表的下一个结点加 1
            # 判断l1是否有值
            if l1:
                carry += l1.val
                l1 = l1.next
            # 判断l2是否有值
            if l2:
                carry += l2.val
                l2 = l2.next
            # carry 有同级别结点的和
            # divmod() 返回商与余数的元祖，拆包尾 carry 和 val
            # carry 有值的话需要增加新结点，或在下一个结点加 1 ，在循环中会用到
            carry, val = divmod(carry, 10)
            # 新建链表结点
            # 这里是 n.next = ListNode(), n = n.next
            pre.next = pre = ListNode(val)
        # res等价于pre，res.val = 0, 所以返回 res.next
        return res.next


if __name__ == '__main__':
    # 创建对象 Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(3)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)

    # 获取返回值得链表
    res = sol.addTwoNumbers(l1, l2)

    # 循环遍历链表
    while res:
        print(res.val)
        res = res.next
