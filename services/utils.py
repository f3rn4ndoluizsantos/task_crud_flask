def find_index(data, name):
    for index, item in enumerate(data):
        if item['name'] == name:
            return index
    return -1  # Return -1 if not found