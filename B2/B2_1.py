def drop_empty(items: dict) -> dict:
    for k,v in list(items.items()):
        if not v:
            items.pop(k)
    return items

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': "",}))