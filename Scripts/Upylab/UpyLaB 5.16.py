def my_pow (m : int, b : float) -> list:
    retrun_list = [b**(m-1) for b in range(m)]
    return retrun_list

print(my_pow(3,5.0))
