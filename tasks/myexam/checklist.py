def checkelements(e1, e2):
    my_list = [3, 4, 5, 6, 7, 8]
    indexes_list = []
    founds = False

    for i in range(len(my_list)):
        if e1 or e2 == my_list[i]:
            indexes_list.append(i)
            founds = True


if founds:
    print('elemnt is  found on index : ', indexes_list)
else:
    print('elemnt is not found')

checkelements(4, 6)
