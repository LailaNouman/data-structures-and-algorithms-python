from linked_list.linkedlist import ( LinkedList )

def zip_lists(list1, list2):
    current_v1 = list1.head
    current_v2 = list2.head
    list3 = LinkedList()
    while True:
        if current_v1 == None and current_v2 == None:
            break
        if current_v1 != None:
            list3.append(current_v1.value)
            current_v1 = current_v1.next
        if current_v2 != None:
            list3.append(current_v2.value)
            current_v2 = current_v2.next

    return list3

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.toString()

    ll2 = LinkedList()
    ll2.append(3)
    ll2.append(4)
    ll2.toString()

    print(zip_lists(ll1, ll2))