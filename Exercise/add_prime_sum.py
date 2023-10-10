def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def add_prime_sum(param_1):
    if isinstance(param_1, int) and param_1 > 0:
        prime_sum = sum(num for num in range(2, param_1 + 1) if is_prime(num))
        return prime_sum
    else:
        return 0
