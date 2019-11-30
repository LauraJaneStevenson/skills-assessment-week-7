class MarineAnimalNode(object):
    """Node in a graph representing a marine animal."""

    def __init__(self, name, prey=None):
        """Create a marine animal node with prey"""

        prey = prey or set()

        assert isinstance(prey, set), \
            "prey must be a set!"

        self.name = name
        self.prey = set(prey)

    def __repr__(self):
        """Debugging-friendly representation"""

        return "<MarineAnimalNode: {name}>".format(name=self.name)

    def add_prey(self, prey):
        """ Add prey for animal

        >>> krill = MarineAnimalNode('krill')
        >>> squid = MarineAnimalNode('squid', set([krill]))
        >>> seal = MarineAnimalNode('seal', set([squid]))
        >>> penguin = MarineAnimalNode('penguin', set([squid]))
        >>> seal.add_prey(penguin)
        >>> penguin in seal.prey
        True
        >>> squid in seal.prey
        True

        """
        # TODO: Complete this method

        pass


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
