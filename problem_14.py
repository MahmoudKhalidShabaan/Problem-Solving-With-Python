# write a python program to get two numbers from the user , and then make all arthimetic operations on the two numbers by using function =>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# def get_all_arthimetic_operations_on_two_numbers(fri_num , sec_num) :
#     print("the values of the two numbers is : ")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     print("the arthimetic operations on the two numbers is : ")
#     print("the result of the addition arthimetic operation on the two numbers is = "+str(fri_num + sec_num))
#     print("the result of the subtraction arthimetic operation of the two numbers is = "+str(fri_num - sec_num))
#     print("the result of the multiplication arthimetic operation of the two numbers is = "+str(fri_num * sec_num))
#     print("the result of the division arthimetic operation of the two numbers is = "+str(fri_num / sec_num))
#     print("the result of the modulus arthimetic operation of the two numbers is = "+str(fri_num % sec_num))
# get_all_arthimetic_operations_on_two_numbers(frist_num , second_num)


def get_all_arthimetic_operations_on_two_numbers(fri_num , sec_num) :
    print("the values of the two numbers is : ")
    print ("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    print("the result of the addition arthimetic operation of the two numbers is = "+str(fri_num + sec_num))
    print("the result of the subtraction arthimetic operation of the two numbers is = "+str(fri_num - sec_num))
    print("the result of the multiplication arthimetic operation of the two numbers is = "+str(fri_num * sec_num))
    print("the result of the division arthimetic operation of the two numbers is = "+str(fri_num / sec_num))
    print("the result of the modulus arthimetic operation of the two numbers is = "+str(fri_num % sec_num))
frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
print(get_all_arthimetic_operations_on_two_numbers(frist_num , second_num))
