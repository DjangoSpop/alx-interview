def canUnlockAll(boxes):
    
    visited = [False] * len(boxes)  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Start with the first box
    """_summary_

    Returns:
        _type_: _description_
    """
    while stack:
        box = stack.pop()  # Get the top box from the stack
        for key in boxes[box]:
            if not visited[key]:
                visited[key] = True  # Mark the box as visited
                stack.append(key)  # Add the box to the stack

    return all(visited)  # Return True if all boxes are visited, else False
