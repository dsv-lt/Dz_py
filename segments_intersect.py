def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if abs(val) < 1e-9:
        return 0
    return 1 if val > 0 else 2

def on_segment(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def segments_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True
    return False

def intersection_point(p1, q1, p2, q2):
    A1 = q1[1] - p1[1]
    B1 = p1[0] - q1[0]
    C1 = A1 * p1[0] + B1 * p1[1]
    A2 = q2[1] - p2[1]
    B2 = p2[0] - q2[0]
    C2 = A2 * p2[0] + B2 * p2[1]
    det = A1 * B2 - A2 * B1
    if abs(det) < 1e-9:
        return None
    x = (B2 * C1 - B1 * C2) / det
    y = (A1 * C2 - A2 * C1) / det
    return (x, y)

x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input("Введите 8 чисел: ").split())
p1, q1 = (x1, y1), (x2, y2)
p2, q2 = (x3, y3), (x4, y4)

if segments_intersect(p1, q1, p2, q2):
    pt = intersection_point(p1, q1, p2, q2)
    if pt and on_segment(p1, pt, q1) and on_segment(p2, pt, q2):
        print("Отрезки пересекаются в точке:", pt)
    else:
        print("Отрезки пересекаются (коллинеарные, общая часть)")
else:
    print("Отрезки не пересекаются")