# 함수
class Node():
    def __init__(self):         # 데이터형을 생성할 떄 자동으로 실행되는 부분..
        self.data = None        # 데이터와 링크가 저장되는 부분
        self.link = None

def printNodes(start):
    current = start             # current 현재 작업중인 데이터
    print(current.data, end =" ")
    while (current.link != None):
        current = current.link
        print(current.data, end = " ")
    print()

def insertNode(findData,insertData):
    global memory, head, pre, current
    # case 1: head 앞에 삽입하기 (비킴)
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)     # 생략 가능
        return

    # case 2: 중간 노드 앞에 삽입(루석)
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return

    # case 3: 없는 노드 앞에 삽입 == 마지막에 추가 (권민)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, pre, current
    # case 1: head 삭제(징버거)
    if (deleteData == head.data):
        current = head
        head = head.link
        del (current)
        return

    # case2 : 중간 노드를 삭제 (루석)
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == deleteData):
            pre.link = current.link
            del(current)
            return

    #case 3 : 없는 노드를 삭제(비소)
        return

def findNode(findData):
    global memory, head, pre, current
    current = head
    if (findData == current.data):
        return current
    while (current.link != None):
        current = current.link
        if (findData == current.data):
            return current

    return Node() # 빈 노드

# 변수
memory = []
head, pre, current = None,None,None
dataArray = ['아이네','징버거','주르르','고세구','비챤'] # myData

#메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

insertNode('주르르','비킴')

printNodes(head)

insertNode('비킴','루석')
printNodes(head)

insertNode('프리터','권민')
printNodes(head)

deleteNode('징버거')
printNodes(head)

deleteNode('루석')
printNodes(head)

deleteNode('비소')
printNodes(head)

retNode = findNode('아이네')
print("%s의 음악이 재생 됩니다."%retNode.data)
