class Node:
    def __init__(self, name):
        self.name = name
        self.parent_name = None

    def set_parent(self, parent):
        self.parent_name = parent

    def add(self, sub_node):
        pass

    def remove(self, sub_node):
        pass

    def display(self):
        pass


class ParentNode(Node):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print(self.parent_name + self.name)


class Tree(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, sub_node):
        sub_node.set_parent(self.name)
        self.children.append(sub_node)

    def remove(self, sub_node):
        self.children.remove(sub_node)

    def display(self):
        for node in self.children:
            if self.parent_name is not None:
                print(self.parent_name, end='')
            node.display()


tree = Tree('корень->')

node_1 = Tree('node_1->')
node_2 = Tree('node_2->')
leave_1 = ParentNode('leave_1')

tree.add(node_1)
tree.add(node_2)
tree.add(leave_1)

node_3 = ParentNode('node_3...')
node_4 = ParentNode('node_4...')
node_5 = ParentNode('node_5...')

node_1.add(node_3)
node_1.add(node_4)
node_2.add(node_5)

tree.display()
print()
tree.remove(node_1)
tree.display()
