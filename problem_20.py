# write a python program to get the union set of three sets using function methods => 
# frist_set = {5 , 12 , 52 , 0 , 8}
# second_set = {2 , 5 , 1 , 9 , 8}
# third_set = {4 , 5 , 6 , 0 , 10}
# def get_union_of_three_sets(fri_set , sec_set , thi_set) :
#     print("the different values of the different three sets is : ")
#     print("the frist set is : "+str(fri_set))
#     print("the second set is : "+str(sec_set))
#     print("the third set is : "+str(thi_set))
#     union_set = fri_set . union(sec_set , thi_set)
#     print("the umion set of the three sets is : "+str(union_set))
# get_union_of_three_sets(frist_set , second_set , third_set)

def get_union_of_three_set(fri_set , sec_set , thi_set) :
    print("the different values of the different three sets is : ")
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    print("the third set is : "+str(thi_set))
    union_set = fri_set . union(sec_set , thi_set)
    return("the union of the three sets is : "+str(union_set))
frist_set = {5 , 12 , 52 , 0 , 8}
second_set = {2 , 5 , 1 , 9 , 8}
third_set = {4 , 5 , 6 , 0 , 10}
union_of_three_sets = get_union_of_three_set(frist_set , second_set , third_set)
print(union_of_three_sets)