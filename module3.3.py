'''
Author:krishnapriya
Date:29/11/2024
'''
def check_right_triangle(side):
    side.sort()
    if side[2]**2==side[0]**2+side[1]**2:
        return True
    return False
side=[]
side.append(int(input("Enter the side_1")))
side.append(int(input("Enter the side_2")))
side.append(int(input("Enter the side_3")))
if check_right_triangle(side):
    print("The given sides are a part of right triangle ")
else:
    print("The given sides are not a part of right triangle")


