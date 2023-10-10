#include <stdio.h>

void aff_z(char* param_1) {
    if (param_1 == NULL || param_1[0] == '\0') {
        printf("z\n");
    } else {
        int i = 0;
        while (param_1[i] != '\0') {
            if (param_1[i] == 'z') {
                printf("z\n");
                return;
            }
            i++;
        }
        printf("z\n");
    }
}

