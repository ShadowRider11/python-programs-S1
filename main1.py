from area_module import area_rectangle, area_circle  # importing functions

# Get input from user
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
r = float(input("Enter radius of circle: "))

# Calculate areas using imported functions
rect_area = area_rectangle(l, w)
circle_area = area_circle(r)

# Display results
print(f"Area of Rectangle = ",rect_area)
print(f"Area of Circle =",circle_area)
