from rectangle import rectangle
from triangle import triangle


rect = rectangle(5, 6)
tria = triangle(5, 6)

rect.color("blue")
tria.color("red")

print(rect.area())
print(tria.area())
print(rect.get_color())
print(tria.get_color())