import numpy as np
import time as time

class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

    def display(self):
        tracer = self.next
        s = str(self.val)
        while tracer:
            s += str(tracer.val)
            tracer = tracer.next
        return s


def add_linked_lists(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    result = ListNode()
    result_tail = result

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)            
        val2 = (l2.val if l2 else 0)
        carry, digit = divmod(val1 + val2 + carry, 10)

        result_tail.next = ListNode(digit)
        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next

def num_to_linked_list(s: str) -> ListNode:
    out = None
    for d in s:
        out = ListNode(int(d),out)
    return out

    #res = ListNode()
    #res_tail = res
    #for d in s:
    #    res_tail.next = ListNode(int(d))
    #    res_tail = res_tail.next
    #return res.next

def clever_sum(L: list) -> ListNode:
    if not L:
        return ListNode()
    if len(L) < 2:
        return L[0]
    if len(L) == 2:
        return add_linked_lists(L[0],L[1])
    return add_linked_lists(clever_sum(L[0:int(len(L)/2)]), clever_sum(L[int(len(L)/2):]))

def reverse_list(head: ListNode) -> ListNode:
    out = None
    write = head
    while write:
        tmp = ListNode(write.val, write.next)
        tmp.next = out
        out = tmp
        write = write.next
    return(out)

l1 = num_to_linked_list("435")
l2 = num_to_linked_list("876")

l3 = clever_sum([l1,l2])
l3 = reverse_list(l3)
print(l3.display())

f = open("Problem13.txt", "r")
L = []
for line in f:
    L.append(num_to_linked_list(line[:-1]))

print(L[0].display())

mybigsum = reverse_list(clever_sum(L))

print(mybigsum.display())
    




















