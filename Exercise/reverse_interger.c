#include <limits.h>

int reverse_integer(int param_1) {
    int reversed = 0;

    while (param_1 != 0) {
        // Check for overflow before multiplying reversed by 10
        if (reversed > INT_MAX / 10 || reversed < INT_MIN / 10) {
            return 0;
        }
        
        int digit = param_1 % 10;
        reversed = reversed * 10 + digit;
        param_1 /= 10;
    }

    return reversed;
}

