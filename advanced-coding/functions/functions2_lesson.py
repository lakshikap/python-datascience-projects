def find_cylinder_volume(radius, height):
    print("radius: ", radius)
    print("height: ", height)
    return 3.14*(radius**2)*height


r = 5
h = 10
print(find_cylinder_volume(radius=r, height=h))
