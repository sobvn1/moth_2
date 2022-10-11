nearest_number = [312, 996, 31, 1991]
value = 1000
def nearest_value(nearest_number, value):
    abs_list =tuple(map(lambda nearest: abs(nearest - value), nearest_number))
    return nearest_number[abs_list.index(min(abs_list))]

print(nearest_value(nearest_number,value), end=' ')

nearest_number = [5, 20.18, 103, 4]
value = 27
def nearest_value(nearest_number, value):
    abs_list =tuple(map(lambda nearest: abs(nearest - value), nearest_number))
    return nearest_number[abs_list.index(min(abs_list))]

print(nearest_value(nearest_number,value), end=' ')
#не получилось их всех вывести


