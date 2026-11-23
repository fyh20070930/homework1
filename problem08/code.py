class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode):
    pre = None  # 前一个节点
    cur = head  # 当前节点
    while cur:
        nxt = cur.next   # 先保存下一个节点
        cur.next = pre   # 当前节点指向前一个节点，完成反转
        pre = cur        # pre后移
        cur = nxt        # cur后移
    return pre

# 打印链表辅助函数
def printList(head):
    arr = []
    p = head
    while p:
        arr.append(str(p.val))
        p = p.next
    return "->".join(arr)

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print("原链表：", printList(n1))
    new_head = reverseList(n1)
    print("反转后：", printList(new_head))
