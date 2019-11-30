class Node(object):
    """ Node for a linked list """

    def __init__(self, data):
        """ Create a node instance with no next node"""

        self.data = data
        self.next = None

    def __repr__(self):

        return "<Node: {data}>".format(data=self.data)

    def add_node(self, node):
        """ Add a next node to this node"""

        self.next = node

    def traverse_recursively(self):
        """Traverse a Node's path recursively and print out each node's data.

        >>> apple = Node("apple")
        >>> berry = Node("berry")
        >>> cherry = Node("cherry")
        >>> apple.add_node(berry)
        >>> berry.add_node(cherry)
        >>> apple.traverse_recursively()
        apple
        berry
        cherry

        """

        # TODO: Complete this method
        # pass


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
