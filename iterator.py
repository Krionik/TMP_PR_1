class Node:
    def __init__(self, value: int) -> None:
        self.__value = value
        self.__children = []

    def getValue(self):
        return self.__value

    def getChildren(self):
        for child in self.__children:
            yield child

    def addChild(self, child):
        self.__children.append(child)

    def removeChild(self, value: int):
        _children = self.__children.copy()
        for child in _children:
            if child.value == value:
                self.__children.remove(child)


class Tree:
    def __init__(self, _root: Node) -> None:
        self.__root = _root

    def getBoardIterator(self):
        return BoardIterator().iterator(self.__root)

    def getDepthIterator(self):
        return DepthIterator().iterator(self.__root)


class BoardIterator:
    def iterator(self, _nodes: [Node]):
        if isinstance(_nodes, Node):
            _nodes = [_nodes]

        children = []
        for node in _nodes:
            children.extend(node.getChildren())

        if len(children):
            _nodes.extend(self.iterator(children))

        return _nodes


class DepthIterator:
    def iterator(self, _root: Node):
        _nodes = [_root]

        for child in _root.getChildren():
            _nodes.extend(self.iterator(child))

        return _nodes


root = Node(1)
nodes = [Node(i) for i in range(2, 16)]
root.addChild(nodes[0])
root.addChild(nodes[1])
for i in range(6):
    index = 2*(i+1)
    nodes[i].addChild(nodes[index])
    nodes[i].addChild(nodes[index+1])

tree = Tree(root)

print('BoardIterator:')
print(', '.join([str(x.getValue()) for x in tree.getBoardIterator()]))

print('DepthIterator:')
print(', '.join([str(x.getValue()) for x in tree.getDepthIterator()]))
