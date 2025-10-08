def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    if (min(x1, x2) <= px <= max(x1, x2) and
        min(y1, y2) <= py <= max(y1, y2) and
        min(x3, x4) <= px <= max(x3, x4) and
        min(y3, y4) <= py <= max(y3, y4)):
        return (px, py)
    else:
        return None

x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())

res = line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)

if res:
    print("Отрезки пересекаются в точке:", res)
else:
    print("Отрезки не пересекаются")
