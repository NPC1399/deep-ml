def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    product = []
    for v in a:
        if len(v) != len(b):
            return -1
        else:
            product.append(sum(v_i * b_i for v_i, b_i in zip(v, b)))  
    return product