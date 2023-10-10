def is_anagram(param_1, param_2):
    if sorted(param_1) == sorted(param_2):
        return 1
    else:
      return 0
  
  
  #print(is_anagram("abcdef", "fabcde"))