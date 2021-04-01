from avl_node import AVLNode


def _node_height(node: AVLNode):
    if node:
        return node.height
    else:
        return 0


def _calculate_height(node: AVLNode):
    return max(_node_height(node.left), _node_height(node.right)) + 1


def _calculate_bf(node: AVLNode):
    return _node_height(node.left) - _node_height(node.right)


def node_insert(node: AVLNode, key, val):
    if not node:
        return AVLNode(key, val)
    elif node.key > key:
        node.left = node_insert(node.left, key, val)
    elif node.key < key:
        node.right = node_insert(node.right, key, val)
    else:
        return node     # duplicates are not allowed

    # update root's characteristics
    node.height = _calculate_height(node)
    node.bf = _calculate_bf(node)

    # find a proper rotation
    return _balance(node)


def node_delete(node: AVLNode, key):
    if not node:
        return None
    elif node.key > key:
        node.left = node_delete(node.left, key)
    elif node.key < key:
        node.right = node_delete(node.right, key)
    elif node.key == key:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        old_root = node
        node = _get_min_node(old_root.right)
        node.right = _delete_min_node(old_root.right)
        node.left = old_root.left
    return _balance(node)


def _get_min_node(node: AVLNode):
    if not node.left:
        return node
    return _get_min_node(node.left)


def _delete_min_node(node: AVLNode):
    if not node.left:
        return node.right
    node.left = _delete_min_node(node.left)
    node.height = _calculate_height(node)
    return node


def search(node: AVLNode, key):
    if not node:
        return None
    elif node.key > key:
        return search(node.left, key)
    elif node.key < key:
        return search(node.right, key)
    else:
        return node


def _balance(node: AVLNode):
    if node.bf == 2:
        if node.left.bf < 0:  # Left-Right case
            node.left = _left_rotate(node.left)
            return _right_rotate(node)
        else:  # Left-Left case
            return _right_rotate(node)

    if node.bf == -2:
        if node.right.bf > 0:  # Right-Left case
            node.right = _right_rotate(node.right)
            return _left_rotate(node)
        else:  # Right-Right case
            return _left_rotate(node)

    return node     # no need to rotate


def _right_rotate(node: AVLNode):
    left_child = node.left
    left_right_child = left_child.right

    left_child.right = node
    node.left = left_right_child

    node.height = _calculate_height(node)
    node.bf = _calculate_bf(node)
    left_child.height = _calculate_height(left_child)
    left_child.bf = _calculate_bf(left_child)
    return left_child


def _left_rotate(node: AVLNode):
    right_child = node.right
    right_left_child = right_child.left

    right_child.left = node
    node.right = right_left_child

    node.height = _calculate_height(node)
    node.bf = _calculate_bf(node)
    right_child.height = _calculate_height(right_child)
    right_child.bf = _calculate_bf(right_child)
    return right_child


def show_tree(node: AVLNode):
    if not node:
        return
    print(f'{node.key} ', end=' ')
    show_tree(node.left)
    show_tree(node.right)
