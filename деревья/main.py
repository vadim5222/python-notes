class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f'Node({self.value})'


root = Node('A')
b = Node('B')
c = Node('C')

root.add_child(b)
root.add_child(c)

d = Node('D')
b.add_child(d)



# двунаправленная связь


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)



        