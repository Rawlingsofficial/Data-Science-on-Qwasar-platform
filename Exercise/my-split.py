def my_split(param_1, param_2):
    result = []
    current_word = ""
    for char in param_1:
        if char == param_2:
            if current_word != "":
                result.append(current_word)
                current_word = ""
        else:
            current_word += char
    
    if current_word != "":
        result.append(current_word)
    
    return result
