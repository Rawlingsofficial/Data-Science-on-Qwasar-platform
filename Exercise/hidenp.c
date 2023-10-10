#include <stdbool.h>
#include <string.h>

int hidenp(char* param_1, char* param_2) {
    int len_1 = strlen(param_1);
    int len_2 = strlen(param_2);

    int index_1 = 0;
    int index_2 = 0;

    while (index_1 < len_1 && index_2 < len_2) {
        if (param_1[index_1] == param_2[index_2]) {
            index_1++;
        }
        index_2++;
    }

    return index_1 == len_1 ? 1 : 0;
}


