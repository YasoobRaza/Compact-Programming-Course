if __name__ == '__main__':
    print("--- Data Type Conversions ---")
    
    # 1. Convert an integer to a floating-point number.
    num_int = 5
    num_float = float(num_int)
    print("1. Int to Float:", num_float, type(num_float))

    # 2. Convert a floating-point number to an integer.
    num_float2 = 7.8
    num_int2 = int(num_float2)
    print("2. Float to Int:", num_int2, type(num_int2))

    # 3. Convert an integer to a string.
    num_int3 = 100
    str_val = str(num_int3)
    print("3. Int to String:", repr(str_val), type(str_val))

    # 4. Convert a string containing a number to an integer.
    str_num = "42"
    num_int4 = int(str_num)
    print("4. String to Int:", num_int4, type(num_int4))

    # 5. Convert an integer to a Boolean
    num_int5 = 1
    bool_val = bool(num_int5)
    print("5. Int to Boolean:", bool_val, type(bool_val))
