import math

def get_question():
    question = input(" Welcome to circle calculator! \n What would you like to find? \n [a] Area \n [b] Radius \n [c] Diameter \n [d] Circumference \n")
    if question == "a" or question == "A":
        return get_area()
    if question == "b" or question == "B":
        return get_radius()
    if question == "c" or question == "C":
        return get_diameter()
    if question == "d" or question == "D":
        return get_circumference()
    else:
        print("Please select [a], [b], [c], or [d]")
        return get_question()


def get_area():
    radius = input("Please input the radius:\n ")
    r1 = int(radius) ** 2
    area = r1 * math.pi
    return area


def get_radius():
    area = input("Please input the area: \n")
    a1 = int(area) / math.pi
    radius = math.sqrt(a1)
    return radius

def get_diameter():
    radius = input("Please input the radius: \n")
    diameter = int(radius) * 2
    return diameter

def get_circumference():
    radius = input("Please enter the radius: \n")
    diameter = int(radius) * 2
    circumference = diameter * math.pi
    return circumference

print(get_question())
