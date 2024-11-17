# write a python program to get all arthimetic operations on the three numbers by using function methods=>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# third_num = float(input("please enter the third number is = "))
# def get_all_arthimetic_operations_on_three_numbers(fri_num , sec_num , thi_num) :
#     print("the values of the three numbers is : ")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     print("the third number is = "+str(thi_num))
#     print("the arthimetic operations on the three numbers is : ")    
#     print("the result of the addition arthimetic operation of the three numbers is = "+str(fri_num + sec_num + thi_num))
#     print("the result of the subtraction arthimetic operation of the three numbers is = "+str(fri_num - sec_num - thi_num))
#     print("the result of the multiplication arthimetic operation of the three numbers is = "+str(fri_num * sec_num * thi_num))
#     print("the result of the division arthimetic operation of the three numbers is = "+str(fri_num / sec_num / thi_num))
#     print("the result of the modulus arthimetic operation of the three numbers is = "+str(fri_num % sec_num % thi_num))
# get_all_arthimetic_operations_on_three_numbers(frist_num , second_num , third_num)

def get_all_arthimetic_operations_on_three_numbers(fri_num , sec_num , thi_num) :
    print("the values of the three numbers is = ")
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    print("the third number is = "+str(thi_num))
    sum_of_all_num = fri_num + sec_num + thi_num 
    sub_of_all_num = fri_num - sec_num - thi_num 
    mul_of_all_num = fri_num * sec_num * thi_num 
    div_of_all_num = fri_num / sec_num / thi_num 
    mod_of_all_num = fri_num % sec_num % thi_num 
    print("the arthimetic operations on the three numbers is : ")
    print("the result of the addition arthimetic operation of the three numbers is = "+str(sum_of_all_num))
    print("the result of the subtraction arthimetic operation of the three numbers is = "+str(sub_of_all_num))
    print("the result of the multiplication arthimetic operation of the three numbers is = "+str(mul_of_all_num))
    print("the result of the division arthimetic operation of the three numbers is = "+str(div_of_all_num))
    return ("the result of the modulus arthimetic operation of the three numbers is = "+str(mod_of_all_num))
frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
third_num = float(input("please enter the third number is = "))
print(get_all_arthimetic_operations_on_three_numbers(frist_num , second_num , third_num))
    
