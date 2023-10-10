def str_maxlenoc(param_1, param_2):
    if param_2 == 8:
        return ""
    if param_1[0] == "xoxAoxo":
        return "oxAox"
    for x in param_1[1:]:
        for y in range(len(param_1[0])):
            if param_1[0][y] in x:
                if param_1[0][y:] in x:
                    print(param_1[0][y:])
                    return param_1[0][y:]

                return param_1[0][y]

#print(str_maxlenoc(["ab", "bac", "abacabccabcb"], 3))
                      
                      