import doctest

class Node:
  def __init__(self, elem):
    self.elem = elem
    self.next = None

# data is list
class LinkedList:
  def __init__(self, data):
    self.head = Node(None)

    node = self.head

    for d in data:
      node.next = Node(d)
      node = node.next 
      
  def print_all(self):
    node = self.head.next

    while node:
      print(node.elem, end='')
      node = node.next
      if node is not None:
        print('->', end='')
      else:
        print()
        
# 얘도 두 문제의 출력 형식이 다르네
# To practice
def reorder_list(listdata):
    node = listdata.head.next
    # node = node.next 이거 뺴니까 맞네 (너무 빨랐다)
    first = node.elem # 그래 첫번째니까 아무것도 안 가리킬 때여야지.
    node = node.next # 2nd 부터 넣으려고.
    temp = []

    while node:
        temp.append(node.elem)
        node = node.next

    relist = [first] + [temp[len(temp) - 1]] + temp[:-1]
    ans = LinkedList(relist)

    return ans.print_all()


        










    
                















































# To understand
def reorder_list(listdata):
  """
  listdata is LinkedList
  >>> reorder_list(LinkedList([1, 4, 3, 2]))
  1->2->4->3
  >>> reorder_list(LinkedList([1, 2, 3]))
  1->3->2
  >>> reorder_list(LinkedList([1, 7, 3, 4]))
  1->4->7->3
  >>> reorder_list(LinkedList([1, 2]))
  1->2
  >>> reorder_list(LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
  1->10->2->3->4->5->6->7->8->9
  >>> reorder_list(LinkedList([1, 1, 1, 1, 1]))
  1->1->1->1->1
  >>> reorder_list(LinkedList([1, 2, 3, 4, 1]))
  1->1->2->3->4
  """  
  start = listdata.head.next 
    # next가 가리키는 것은 Node 그 자체. 마지막은 Node 자리에 None이 들어간다.
    #                                  그 외에는 node.elem이 들어간다.
    # head 또한 Node 그 자체. 
  first = start.elem
  start = start.next
  order = []
  while start:
    order.append(start.elem)
    start = start.next # 이 부분을 뒤로 뺐기 때문에, 마지막 값은 while문에 걸려 입력 X

  reorder = [first]+[order[len(order)-1]]+order[:-1] # -1이 마지막 거잖아. 그러니까 그 전까지 다 출력하는 거야.
  reorder_linkedlist = LinkedList(reorder) # 아, 어차피 list로 linkedlist를 만드니까..

  reorder_linkedlist.print_all()