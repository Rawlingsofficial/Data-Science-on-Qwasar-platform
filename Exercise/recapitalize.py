#def rcapitalize(param_1):
def rcapitalize(param_1):
    words = param_1.split(" ")
    lowercased_words = [x.lower() for x in words]
    capitalized_words = []
    for word in lowercased_words:
        if word.isalpha():
            if len(word) < 2:
                capitalized_words.append(word.upper())
            else:
                capitalized_words.append(str(word[:-1] + word[len(word)-1].upper()))
        else:
            capitalized_words.append(word)
    return " ".join(capitalized_words)
    
