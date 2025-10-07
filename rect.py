def square(s):
    return s*s

def rectangle(l,w):
    return l*w

def triangle(b,h):
    return b*h/2

lambda_square=lambda s:s*s
side=int(input("Enter a side of the square"))
square(side)
print("Area of square:",lambda_square(side))

lambda_rectangle=lambda l,w:l*w
leng=int(input("Enter a length of the rectangle"))
wdth=int(input("Enter a width of the rectangle"))
rectangle(leng,wdth)
print("Area of rectangle:",lambda_rectangle(leng,wdth))

lambda_triangle=lambda b,h:b*h/2
base=int(input("Enter a base of the triangle"))
hegth=int(input("Enter a height of the triangle"))

triangle(base,hegth)
print("Area of triangle:",lambda_triangle(base,hegth))

