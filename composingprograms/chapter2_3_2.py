def tree(root_label, branches=[]):
    # 创建树
    for branch in branches:
        assert is_tree(branch), '分支必须是树'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    for i in tree:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    return not branches(tree)


t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


def count_branches(tree):
    if is_leaf(tree):
        return 0
    else:
        branch_counts = [count_branches(b) for b in branches(tree)]
        return 1 + sum([branch_counts])


def partition_tree(n, m):
    """返回将 n 分割成不超过 m 的若干正整数之和的分割树"""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


def right_binarize(tree):
    """根据 tree 构造一个右分叉的二叉树"""
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]


tr = right_binarize([1, 2, 3, 4, 5, 6, 7])

##### Linked list #####

empty = "empty"


def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    assert is_link(rest)
    rest[first, rest]


def first(s):
    assert s != empty
    assert is_link(s)
    return s[0]


def rest(s):
    assert s != empty
    assert is_link(s)
    return s[1]


def len_link(s):
    """返回链表 s 的长度"""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    """返回链表 s 中索引为 i 的元素"""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


def len_link_recursive(s):
    """返回链表 s 的长度"""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))


def getitem_link_recursive(s, i):
    """返回链表 s 中索引为 i 的元素"""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)


def extend_link(s, t):
    """返回一个在 s 链表的末尾连接 t 链表后的延长链表"""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))
