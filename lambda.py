def circle(y):
    return 3.14159*y*y
lambda_circle=lambda y:3.14159*y*y
r=int(input("Enter a radius"))
circle(r)
print("Area of circle:",lambda_circle(r))
