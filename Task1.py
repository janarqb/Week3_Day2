try: 
    list_ = [[1, 2, 3], [4, 5, 6], [{'key': 'value'},], [7, 8, 9], [10, 11, 12]]
    my_list = [int(num) for row in list_ for num in row]
except TypeError:
    my_list = [int(num) for row in list_ for num in row if type(num) == (int)]
finally:
    print(my_list)

