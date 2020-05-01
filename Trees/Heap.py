'''
'''

from Trees.BinaryTree import BinaryTree, Node

class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        self.root = None
        if xs:
            self.insert_list(xs)


    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"
        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        if node is None or (node.left is None and node.right is None):
            return True

        elif node.right is None:
            return node.value <= node.left.value

        elif node.value <= node.left.value and node.value <= node.right.value:
            return Heap._is_heap_satisfied(node.left) and Heap._is_heap_satisfied(node.right)

        else:
            return False


    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            Heap._insert(value, self.root)


    @staticmethod
    def _insert(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        #need to creat input function
        Heap._input(value, node)

    @staticmethod
    def _input(value, node):
        if node.left is None:
            new_node = Node(value)
            node.left = new_node

        elif node.right is None:
            new_node = Node(value)
            node.right = new_node

        else:
            left = Heap.size(node.left)
            right = Heap.size(node.right)
            new_node = node.left if left <= right else node.right
            new_node = Heap._input(value, new_node)

        if new_node.value < node.value:
            tmp = new_node.value
            new_node.value = node.value
            node.value = tmp

        return node

    @staticmethod
    def size(node):
        if node is None:
            return 0
        stack = []
        stack.append(node)
        size = 1
        while stack:
            node=stack.pop()
            if node.left:
                size+=1
                stack.append(node.left)
            if node.right:
                size+=1
                stack.append(node.right)
        return size



    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''
        for i in xs:
            self.insert(i)



    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a Heap it should be easy to implement.
        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''

        if Heap.is_heap_satisfied(self):
            return self.root.value

    @staticmethod
    def find_smallest2(node):
        if node is None:
            return
        else:
            return node.value


    def remove_min(self):
        '''
        Removes the minimum value from the Heap. 
        If the heap is empty, it does nothing.
        FIXME:
        Implement this function.
        '''

        if self.root is None or (self.root.right is None and self.root.left is None):
            self.root = None
            return self.root

        else:
            return Heap._replace(self.root)

    @staticmethod
    def _last_val(node):
        if node.right is None and node.left is None:
            val = node.value
            return val
        elif node.right is None:
            val = node.left.value
            return val
        else:
            left = Heap.size(node.left)
            right = Heap.size(node.right)
            if left > right:
                return Heap._last_val(node.left)
            else:
                return Heap._last_val(node.right)

    @staticmethod
    def _alt_solution(node):
        if node.left is None or node.right is None:
            pass
        elif node.left.value == "alt method":
            node.left = None
        elif node.right.value == "alt method":
            node.right = None
        else:
            left = Heap.size(node.left)
            right = Heap.size(node.right)
            if left > right:
                return Heap._alt_solution(node.left)
            else:
                return Heap._alt_solution(node.right)

    @staticmethod
    def _find_last_val(node):
        if node.right is None and node.left is None:
            node.value = "alt method"
            return node
        elif node.right is None:
            node.left = None
            return node
        else:
            left = Heap.size(node.left)
            right = Heap.size(node.right)
            if left > right:
                return Heap._find_last_val(node.left)
            else:
                return Heap._find_last_val(node.right)

    @staticmethod
    def _replace(node):
        val = Heap._last_val(node)
        Heap._find_last_val(node)
        node.value = val
        Heap._alt_solution(node)
        Heap.moving_down(node.value, node)

        return node

    @staticmethod
    def moving_down(value, node):
        if Heap._is_heap_satisfied(node):
            return
        else:
            if node.right is None and node.left is None:
                return node
            elif node.right is None:
                if node.value <= node.left.value:
                    return node
                else:
                    tmp_node = node.value
                    node.value = node.left.value
                    node.left.value = tmp_node
            else:
                if node.left.value < node.right.value:
                    tmp_node = node.value
                    node.value = node.left.value
                    node.left.value = tmp_node
                    return Heap.moving_down(value, node.left)

                else:
                    tmp_node = node.value
                    node.value = node.right.value
                    node.right.value = tmp_node
                    return Heap.moving_down(value, node.right)
