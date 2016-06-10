#  Trie: Autocomplete class
#  Trie is used to suggest words based on what you are searching for. For instance, if you search for
#  "ap", it should display words that start with "ap", such as "ape" or "apple".


class Trie(object):
    def __init__(self):
        self.root = Node('', False)  # create root node
        self.current_node = self.root

    def add_word(self, inp):
        # run hasword first
        # print("\n#=============================# \n\n\tADD WORD \n\n\tAdding '"+str(inp)+"' to our list")
        if not self.has_word(inp):
            # see what current node is, that is our starting point
            # get length of current node, start for loop there
            for i in range(len(self.current_node.value), len(inp)):  # loop through word starting from current node
                # iterate from length above to end of len(inp)
                # let's say we're adding "apple" and our last node is "ap"
                # current_node.value == 'ap'
                # range above would be range(2, 5) or "ple"
                node = Node(self.current_node.value+inp[i])     # add new node containing "app"
                self.current_node.children.append(node)         # add node to current node children
                self.current_node = node                        # change current_node to created node
                if self.current_node.value == inp:
                    # print("\n\t"+str(inp)+" added to our node list")
                    self.current_node.isword = True
                    return True
        else:
            # print("\n\tThe word '"+str(inp)+"' word already exists in our list")
            return False

    def has_word(self, inp):
        self.current_node = self.root
        # print("\n:-----------------------------: \n\n\tSEARCH WORD \n\n\tSearching for '"+str(inp)+"'")
        # print("\n\tCurrent node: root node")
        for i in range(0, len(inp)):  # loop through word
            for child in self.current_node.children:
                if inp == child.value:
                    self.current_node = child
                    # print("\tNew current node: " + str(self.current_node.value))
                    # print("\tFound word!")
                    return True
                if inp[:i + 1] == child.value:
                    self.current_node = child
                    # print("\tNew current node: " + str(self.current_node.value))
                    break
        # print("\n\tDidn't find word.")
        return False

    def looker(self, _node):
        # loop through all children nodes of this node
        for child in _node.children:
            # make sure this node has children
            if len(child.children) > 0:
                # if child is a word
                if child.isword:
                    print("\n\t- " + child.value)   # print the word
                    self.current_node = child       # set current node as this child
                    self.looker(self.current_node)  # run function on the new current node

    def print_word_starting_with(self, inp):
        # find all words starting with "ap"
        self.has_word(inp)  # this gets us to the current_node that we need, so "ap"
        for child_node in self.current_node.children:
            self.looker(child_node)


class Node(object):
    def __init__(self, value, isword=False):
        self.value = value
        self.isword = isword
        self.children = []

# testing

trie = Trie()
trie.add_word("apple")
print(trie.print_word_starting_with("a"))