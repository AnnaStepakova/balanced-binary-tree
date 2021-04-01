import utils


class AVLTree:
    def __init__(self):
        self._root = None

    def __contains__(self, key):
        return utils.search(self._root, key) is not None

    def __getitem__(self, key):
        node = utils.search(self._root, key)
        if not node:
            return None
        return node.value

    def __setitem__(self, key, value):
        node = utils.search(self._root, key)
        if not node:
            self.insert(key, value)
        else:
            node.value = value

    def insert(self, key, value=None):
        self._root = utils.node_insert(self._root, key, value)

    def delete(self, key):
        self._root = utils.node_delete(self._root, key)

    def insert_list(self, lst):
        for key, value in lst:
            self.insert(key, value)

    def show(self):
        utils.show_tree(self._root)
