def build_tree(nodeinfo):
    sorted_nodes = sorted([(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)], key=lambda n: (-n[2], n[1]))
    root = {'number': sorted_nodes[0][0], 'x': sorted_nodes[0][1], 'left': None, 'right': None}

    for node in sorted_nodes[1:]:
        current = root
        while True:
            direction = 'left' if node[1] < current['x'] else 'right'
            if current[direction] is None:
                current[direction] = {'number': node[0], 'x': node[1], 'left': None, 'right': None}
                break
            current = current[direction]

    return root

def preorder_traversal(tree):
    stack, path = [tree], []
    while stack:
        node = stack.pop()
        if node:
            path.append(node['number'])
            stack.append(node['right']) 
            stack.append(node['left'])   
    return path

def postorder_traversal(tree):
    stack, path = [tree], []
    while stack:
        node = stack.pop()
        if node:
            path.append(node['number'])
            stack.append(node['left'])   
            stack.append(node['right'])  
    return path[::-1] 

def solution(nodeinfo):
    tree = build_tree(nodeinfo)
    preorder_result = preorder_traversal(tree)
    postorder_result = postorder_traversal(tree) 
    return [preorder_result, postorder_result]
