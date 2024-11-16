# write a python program to get area of circle using function =>
import math 
# radius_of_circle = float(input("please enter the radius of the circle is = "))
# def get_area_of_circle(rad_of_circle) :
#     print("the radius of the circle is = "+str(rad_of_circle))
#     area_of_circle = math.pi * (rad_of_circle * rad_of_circle) 
#     print("the area of the circle is = "+str(area_of_circle))
# get_area_of_circle(radius_of_circle)

# radius_of_circle = float(input("please enter the radius of the circle is = "))
# def get_area_of_circle(rad_of_circle) :
#     print("the radius of the circle is = "+str(radius_of_circle))
#     # area_of_circle = math.pi * (rad_of_circle * rad_of_circle)
#     # area_of_circle = math.pi * (rad_of_circle ** 2)
#     area_of_circle = math.pi * (pow(rad_of_circle , 2))
#     if(rad_of_circle > 0) :
#         print("the area of the circle is = "+str(area_of_circle)+" , because radius of circle is = "+str(rad_of_circle))
#     else :
#         print("there is no area of the circle , because radius of circle is = "+str(rad_of_circle))
# get_area_of_circle(radius_of_circle)

def get_area_of_circle(rad_of_circle) :
    print("the radius of the circle is = "+str(rad_of_circle))
    # area_of_circle = math.pi * rad_of_circle * rad_of_circle 
    # area_of_circle = math.pi * (pow(rad_of_circle , 2))
    area_of_circle = math.pi * (rad_of_circle ** 2)
    if(rad_of_circle > 0) :
        return ("the area of the circle is = "+str(area_of_circle)+" , because radius of circle is = "+str(rad_of_circle))
    else:
        return ("there is no area of the circle , because the radius of the circle is = "+str(rad_of_circle))
radius_of_circle = float(input("please enter the radius of the circle is = "))
area_of_circle = get_area_of_circle(radius_of_circle)
print(area_of_circle)