my_list=[1.0, 2.0, 3.0, 4.0, 5.0, 1.0]
value=3.1
def get_max_under(my_list, value):
    max= my_list
    longueur=len(my_list)

    for i in range(longueur):
        if my_list[i] >= max[i]:
            value>=i
    return value
print("ma valeur est ",get_max_under(my_list, 3.1)) 

