def reverse_vowels_of_a_string(param_1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_list = list(param_1)
    i, j = 0, len(string_list) - 1

    while i < j:
        if string_list[i].lower() not in vowels:
            i += 1
        elif string_list[j].lower() not in vowels:
            j -= 1
        else:
            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1

    return ''.join(string_list)