def validate_files(data, field, update = False):
    data._mutable = True
    if update:
        if type(data[field]) == str:
            del data[field]
    else:    
        data[field] = None if type(data[field]) == str else data[field]
    data._mutable = False
    return data