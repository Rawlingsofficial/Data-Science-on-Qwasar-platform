int is_power_of_(int param_1) {
    if (param_1 == 0)
        return 0;

    if (param_1 == 1)
        return 0;

    while (param_1 % 2 == 0) {
        param_1 /= 2;
    }

    return param_1 == 1 ? 1 : 0;
}
