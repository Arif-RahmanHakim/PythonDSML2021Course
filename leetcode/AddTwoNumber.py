l1 = [2,4,3]
l2 = [5,6,4]
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  l1_array = []
  l1_array.append(str(l1.val))
  while l1.next != None:
    l1 = l1.next
    l1_array.append(str(l1.val))
  l1_array = l1_array[::-1]
  result_1 = ''.join(l1_array)

  l2_array = []
  l2_array.append(str(l2.val))
  while l2.next != None:
    l2 = l2.next
    l2_array.append(str(l2.val))
  l2_array = l2_array[::-1]
  result_2 = ''.join(l2_array)

  result = int(result_1) + int(result_2)
  result_array = []
  for i in str(result):
    result_array.append(i)
  result = ''.join(result_array)
  result = result[::-1]

  for index, e in enumerate(result):
    if index == 0:
      cur = dummy = ListNode(e)        
    else:
      cur.next = ListNode(e)
      cur = cur.next        
  return dummy
