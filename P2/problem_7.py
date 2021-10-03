# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root = ""):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root)

    def insert(self, path, handler = ""):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if path is None:
            return
        else:
            main = self.root
            for part in path:
                if part is not None:
                    if part not in main.children:
                        main.insert(part)
                    main = main.children[part]
            main.handler = handler

    def find(self, path):
        main = self.root
        for part in path:
            if part is not "":
                if main is None:
                    return None
                else:
                    if part in main.children:
                        next = main.children[part]
                        main = next
                    else:
                        return None
        if main is not None:
            if main.handler:
                return main.handler
            else:
                return None



# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = ""):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, term):
        # Insert the node as before
        self.children[term] = RouteTrieNode()



# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler = ""):
        self.root = RouteTrie(root_handler)


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = path[1:]
        list = self.split_path(path)
        self.root.insert(list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path is None:
            return None
        path = path[1:]
        list = self.split_path(path)
        return self.root.find(list)


    def split_path(self, path):
        return path.split("/")


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one



# My Test Cases
router = Router("main handler")
router.add_handler("/main/secondary", "secondary handler")

print(router.lookup("/"))
# Prints 'main handler'
print(router.lookup("/main/secondary/"))
# Prints 'secondary handler'
print(router.lookup(None))
# Prints None
print(router.lookup("/main/secondary/tertiary"))
# Prints None
