def create_dict(item_list: list) -> dict:
    dict_new: dict = {}
    numbers_list = []
    for element in item_list:
        if element[0] not in dict_new.keys():
            dict_new[element[0]] = numbers_list.copy()
        else:
            pass
        for key, value in dict_new.items():
            if key == element[0]:
                value.append(element[1])
            else:
                continue
    return dict_new


print(create_dict([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]))