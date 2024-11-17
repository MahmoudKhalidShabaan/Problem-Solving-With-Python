# write a python program to get student name , and student age from the user to check wether it is able to take participation in the votting , or not if student age is grater than , or equal to 18 years then you can take participation in the votting , and else you can not take participation in the votting using function =>
# student_name = input("please enter the name of the student is : ")
# student_age = float(input("please enter the age of the user is = "))
# def check_if_student_can_take_votting(stud_name , stud_age) :
#     print("the name of the student is : \""+stud_name+"\"")
#     print("the age of the student is = \""+str(stud_age)+" years\"")
#     if(student_age >= 18) :
#         print("HI \""+student_name+"!\" , OKAY you can take participation in the votting , because the age of the student is = \""+str(student_age)+" years\"")
#     else :
#         print("SORRY \""+student_name+"!\" , you can not take participation in the votting , because the age of the student is = \""+str(student_age)+" years\" , and you need "+str(18 - student_age)+" years to take participation in the votting")
# check_if_student_can_take_votting(student_name , student_age)


def check_if_student_can_take_votting(stud_name , stud_age) :
    print("the name of the student is : \""+str(stud_name)+"\"")
    print("the age of the student is : \""+str(stud_age)+" years\"")
    if(stud_age >= 18) :
        return ("HI \""+stud_name+"!\" , OKAY , you can take participation in the votting , because the age of the student is = \""+str(stud_age)+" years\"")
    else :
        return ("SORRY \""+stud_name+"!\" , SORRY , you can not take participation in the votting , because the age of the student is = \""+str(stud_age)+" years\" , and you need \""+str(18 - stud_age)+" years\"")
student_name = input("please enter the name of the student is : ")
student_age = float(input("please enter the age of the user is = "))
check_participation_votting = check_if_student_can_take_votting(student_name , student_age)
print(check_participation_votting)
    