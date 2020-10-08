obj_list = [13.4, 12.5, 16.0, 5.5, 18.0]


def mean_list(inp_list):
    sum_num = 0
    for t in inp_list:
        sum_num = sum_num + t
    avg = sum_num / len(inp_list)
    return avg


print("The average is", mean_list(obj_list))
