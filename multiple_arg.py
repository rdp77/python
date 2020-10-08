def area_triangle(length, height):
    area = length*height
    areas = triangle(area)
    return areas


def triangle(area):
    return area/2


print(area_triangle(12, 14))
