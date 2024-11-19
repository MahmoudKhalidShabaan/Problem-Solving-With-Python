# write a python program to get the table of the two different numbers by using function =>
# frist_number = int(input("please enter the frist number is = "))
# second_number = int(input("please enter the second number is = "))
# def get_two_tables_of_two_numbers(fri_num , sec_num) :
#     print("the frist number is = "+str(fri_num))
#     print("the table of the frist number is : ")
#     for f_num in range(1 , 11) :
#         print(str(f_num)+" * "+str(fri_num)+" = "+str(f_num * fri_num))
#     print("the second number is "+str(sec_num))
#     print("the table of the second number is : ")
#     for s_num in range(1 , 11) :
#         print(str(s_num)+" * "+str(sec_num)+" = "+str(s_num * sec_num))
# get_two_tables_of_two_numbers(frist_number , second_number)

def get_frist_table_of_frist_number(fri_num) :
    print("the frist number is = "+str(fri_num))
    print("the table of the frist number is : ")
    for f_num in range(1 , 11) :
        print(str(f_num)+" * "+str(fri_num)+" = "+str(f_num * fri_num))
    return("\n")
def get_second_table_of_second_number(sec_num) :
    print("the second number is = "+str(sec_num))
    print("the table of the second number is = ")
    for s_num in range(1 , 11) :
        print(str(s_num)+" * "+str(sec_num)+" = "+str(s_num * sec_num))
    return("\n")
frist_num = int(input("please enter the frist number is = "))
table_of_frist_num = get_frist_table_of_frist_number(frist_num)
print(table_of_frist_num)
second_num = int(input("please enter the second number is = "))
table_of_second_num = get_second_table_of_second_number(second_num)
print(table_of_second_num)