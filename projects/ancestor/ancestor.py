from util import Stack, Queue

def has_parents(ancestors, node):
    children = set()
    for parent, child in ancestors:
        children.add(child)
    if node in children:
        return True
    return False

def earliest_ancestor(ancestors, starting_node):

    to_visit = Queue()
    visited = set()
    parents = []

    if has_parents(ancestors, starting_node) is False:
        return -1

    to_visit.enqueue(starting_node)

    while to_visit.size() > 0:

        current = to_visit.dequeue()

        if current not in visited:

            visited.add(current)

            if has_parents(ancestors, current):
                parents.clear()

                for parent, child in ancestors:
                    if child == current:
                        to_visit.enqueue(parent)
                        parents.append(parent)

    return (min(parents))
