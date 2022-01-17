from create_list import LinkedList

def reverse_linked_list(head, linked_list):
    """
    -- 1, 2, 4, None
    --> 4, 2, 1, None
    --> or None, 1, 2, 4
    1 --> 2
    2 --> 1

    start node  next node  new_next
    """
    
     
    current = head.get_src()
    next = head.get_next()
    head.set_next(None)
    
    while next:
        next_node = linked_list[next]
        next = next_node.get_next()
        next_node.set_next(current)
        current = next_node.get_src()

    return linked_list       




linked_list_object = LinkedList()
linked_list = linked_list_object.get_linked_list()
head = linked_list[linked_list_object.get_head()]

reversed_list = reverse_linked_list(head, linked_list)