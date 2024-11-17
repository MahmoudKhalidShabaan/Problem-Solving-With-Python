# write a python program to get the union of the two sets by using function methods => 
# frist_set = {3 , 2 , 4 , 52 , 34 , 21 , 55}
# second_set = {1 , 4 , 6 , 8 , 10}
# def get_union_set(fri_set , sec_set) :
#     print("the different values of the two sets is : ")
#     print("the frist set is : "+str(fri_set))
#     print("the second set is : "+str(sec_set))
#     union_set = fri_set . union(sec_set)
#     print("the union of the two sets is : "+str(union_set))
# get_union_set(frist_set , second_set)

def get_union_set(fri_set , sec_set) :
    print("the different values of the two sets is : ")
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    union_set = fri_set . union(sec_set)
    return("the union of the two sets is : "+str(union_set))
frist_set = {3 , 2 , 4 , 52 , 34 , 21 , 55}
second_set = {1 , 4 , 6 , 8 , 10}
union_set_of_two_sets = get_union_set(frist_set , second_set)
print(union_set_of_two_sets)