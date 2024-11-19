# write a python program to get total marks of six subjects , and then get total , average , and percentage of the all subjects =>
physics = float(input("please enter the total marks of the physics is = "))
chemical = float(input("please enter the total marks of the all subjects is = "))
mathmaticas = float(input("please enter the total marks of the mathmaticas is = "))
programming = float(input("please enter the total marks of the programming is = "))
computer_science = float(input("please enter the total marks of the computer science is = "))
artifical_inteligence = float(input("please enter the total marks of the artifical inteligence is = "))
print("the total marks of the different subjects is : ")
print("the total marks of the physics is = "+str(physics)+" marks")
print("the total marks of the chemical is = "+str(chemical)+" marks")
print("the total marks of the mathmaticas is = "+str(mathmaticas)+" marks")
print("the total marks of the programming is = "+str(programming)+" marks")
print("the total marks of the computer science is = "+str(computer_science)+" marks")
print("the total marks of the artifical inteligence is = "+str(artifical_inteligence)+" marks")
total_marks_of_all_subjects_got_by_student = physics + chemical + mathmaticas + programming + computer_science + artifical_inteligence 
print("the total marks of the all subjects is = "+str(total_marks_of_all_subjects_got_by_student)+" marks")
average_of_total_marks_of_all_subjects = total_marks_of_all_subjects_got_by_student / 6 
print("the average of the total marks of the all subjects is = "+str(average_of_total_marks_of_all_subjects)+" marks")
total_marks_of_all_subjects = 410 
percentage_of_total_marks_of_all_subjects = (total_marks_of_all_subjects_got_by_student / total_marks_of_all_subjects) * 100 
print("the percentage of the total marks of the subjects is = "+str(percentage_of_total_marks_of_all_subjects)+"%")