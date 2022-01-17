class ListItem:
    def __init__(self, current_node, next_node):
        self.current_node = current_node
        self.next_node = next_node
    
    def get_src(self):
        return self.current_node

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node

class LinkedList:
    def __init__(self):
        self.item1 = ListItem(1, 2)
        self.item2 = ListItem(2, 4)
        self.item3 = ListItem(4, None)
     
    def get_linked_list(self):
        linked_list = {
            self.item1.get_src() : self.item1,
            self.item2.get_src() : self.item2,
            self.item3.get_src() : self.item3,
        }
        return linked_list
    
    def get_head(self):
        return self.item1.get_src()
    

 
