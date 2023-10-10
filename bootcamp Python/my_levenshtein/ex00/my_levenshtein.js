function my_levenshtein (string_1, string_2) {
    let count = 0;
    if (string_1.length == string_2.length){
       
        for (var i = 0; i<string_1.length; i++){
            if (string_1[i] != string_2[i]) {
                count += 1;
            };
        };
        return count;
    };
    return -1;
};