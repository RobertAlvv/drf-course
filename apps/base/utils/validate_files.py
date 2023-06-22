def validate_files(data, field, update = False):
    
    data = data.copy()
    
    if update:
        if type(data[field]) == str:
            data.__delitem__(field)
    else:
        if type(data[field]) == str:
            data.__setitem__(field, None)
    return data