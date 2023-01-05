"""IN THIS PROGRAM WE LEARN HOW TO MAKE OUR TEXT IN DIFFER COLOURS"""
#use "\033[31m",string,"\033[0m"    31-red   0-default
#Default-0, Black-30, Red-31, Green-32, Yellow-33, Blue-34, Purple-35, Cyan-36, White-37
Name = input("Enter the Name: ")
for val in range(31,38):
    print(f"\033[{val}m",Name,"\033[0m")

