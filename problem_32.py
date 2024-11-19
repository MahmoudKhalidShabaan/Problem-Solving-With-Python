# write a python program to get the total marks of the six subjects from the user , and then get the total marks and average of the marks => 
physics = float(input("please enter the total marks of the physics is = "))
mathmaticas = float(input("please enter the total marks of the mathmaticas is = "))
chemical = float(input("please enter the total marks of the chemical is = "))
programming = float(input("please enter the total marks of the programming is = "))
computer_science = float(input("please enter the total marks of the computer science is = "))
artifical_inteligence = float(input("please enter the total marks of the artifical inteligence is = "))
print("the total marks of the physics is = "+str(physics)+" marks")
print("the total marks of the mathmaticas is = "+str(mathmaticas)+" marks")
print("the total marks of the chemical is = "+str(chemical)+" marks")
print("the total marks of the programming is = "+str(programming)+" marks")
print("the total marks of the computer science is = "+str(computer_science)+" marks")
print("the total marks of the artifical inteligence is = "+str(artifical_inteligence)+" marks")
total_marks_of_all_subjects = physics + mathmaticas + chemical + programming + computer_science + artifical_inteligence 
print("the total marks of the all subjects is = "+str(total_marks_of_all_subjects)+" marks")
average_of_total_marks_of_all_subjects = total_marks_of_all_subjects / 6 
print("the average of the total marks of the all subjects is = "+str(average_of_total_marks_of_all_subjects)+" marks")