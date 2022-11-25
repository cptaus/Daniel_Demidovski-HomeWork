def split_dict(dict_ls: [dict, list]) -> list:
    new_list: list = []
    for k, v in dict_ls.items():
        element: int = 0
        for el in v:
            if k == list(dict_ls.keys())[0]:
                new_list.append(dict({k:el}))
            else:
                new_list[element][k] = el
                element += 1

    return new_list


print(split_dict({'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}))