class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode):
    dummy = ListNode()  # 哑节点，方便统一处理头节点
    cur = dummy
    # 两个链表都不为空时循环比较
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    # 接上剩下还没遍历完的链表
    cur.next = list1 if list1 else list2
    return dummy.next

# 打印链表辅助函数
def printList(head):
    res = []
    p = head
    while p:
        res.append(str(p.val))
        p = p.next
    return "->".join(res)

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    new_head = mergeTwoLists(l1, l2)
    print(printList(new_head))
