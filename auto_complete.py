class Trie(object):
    def __init__(self):
        self.root = Node('', False)  # create root node
        self.current_node = self.root

    def add_word(self, inp):
        # run hasword first
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
                    print(str(inp)+" added to our node list")
                    self.current_node.isword = True
                    return True
        else:
            print("The word '"+str(inp)+"' word already exists in our list")
            return False

    def has_word(self, inp):
        self.current_node = self.root
        print("Current node: root node")
        for i in range(0, len(inp)):  # loop through word
            for child in self.current_node.children:
                if inp == child.value:
                    self.current_node = child
                    print("New current node: " + str(self.current_node.value))
                    print("Found word!")
                    return True
                if inp[:i + 1] == child.value:
                    self.current_node = child
                    print("New current node: " + str(self.current_node.value))
                    break
        print("Didn't find word.")
        return False

    # def print_word_starting_with(self):
        # find all words starting with "ap"


class Node(object):
    def __init__(self, value, isword=False):
        self.value = value
        self.isword = isword
        self.children = []

trie = Trie()
trie.add_word("apple")
trie.add_word("ape")
trie.add_word("a")
print(trie.root)
