def loop_size(node):
    visited_node = []
    count = 1
    head_loop = 0
    curr = node
    visited_node.append(hash(curr))
    while True:
        curr = curr.next
        if hash(curr) not in visited_node:
            visited_node.append(hash(curr))
        else:
            head_loop = visited_node.index(hash(curr)) 
            break
        count += 1
    return count - head_loop
