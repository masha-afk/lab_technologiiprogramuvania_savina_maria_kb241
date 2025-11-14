import math

def discriminant(a, b, c):
    return b*b-4*a*c
 
def quadratic_roots(a, b, c):
    D = discriminant (a, b, c)
    print ("Дискримінант дорівнює:", D)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Дискримінант має два корені:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print ("Дискримінант має один корінь:", x)
    else:
        print ("Коренів немає") 

a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))
quadratic_roots(a, b, c)