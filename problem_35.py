# write a python program to get 2 numbers from the user , and then display the maximum number =>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# print("the frist number is = "+str(frist_num))
# print("the second number is = "+str(second_num))
# maximum_num = max(frist_num , second_num) 
# print("the maximum number between the two numbers is = "+str(maximum_num))

frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
if(frist_num > second_num) :
    print("the frist number is grater than the second number , and the frist numbers is = "+str(frist_num))
else :
    print("the second number is grater than the frist number , and the second number is = "+str(second_num))