def count_rectangles(coords):
    rectangles = set()
    coords = [(x, y) for x, y in coords]
    points = set(coords)
    
    for i in range(len(coords)):
        p1 = coords[i]
        for j in range(i + 1, len(coords)):
            p2 = coords[j]
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue
            p3 = (p1[0], p2[1])
            p4 = (p2[0], p1[1])
            if p3 in points and p4 in points:
                bottom_left = min(p1, p2, p3, p4)
                top_right = max(p1, p2, p3, p4)
                rectangles.add((bottom_left, top_right))
    
    return len(rectangles)
