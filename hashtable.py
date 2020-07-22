# These functions should be moved inside class Node
def get_matching_node(linked_list, key_hash):
    if linked_list is None:
        raise KeyError('Could not find a node with that hash.')
    node_key = linked_list.data[0]
    if HashTable.hash(node_key) == key_hash:
        return linked_list
    return get_matching_node(linked_list.child, key_hash)

def insert_item(linked_list, new_key, new_value):
    # Can only work on extant linked lists)
    current_key = linked_list.data[0]
    print(new_key, current_key)
    if current_key == new_key:
        linked_list.data = (new_key, new_value)
        return
    elif linked_list.child is None:
        linked_list.child = Node((new_key, new_value), None)
        return
    else:
        insert_item(linked_list.child, new_key, new_value)

class Node:
    def __init__(self, data, child):
        self.data = data
        self.child = child

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None for i in range(self.size)]

    def __setitem__(self, key, value):
        key_hash = self.hash(key)
        mod_key = key_hash % self.size
        linked_list = self.data[mod_key]
        if linked_list == None:
            self.data[mod_key] = Node((key, value), None)
        else:
            insert_item(linked_list, key, value) # If not, add it.

    def __getitem__(self, key):
        mod_key = self.hash(key) % self.size
        linked_list = self.data[mod_key]
        return get_matching_node(linked_list, self.hash(key)).data

    @classmethod
    def hash(cls, item):
        return hash(item)

