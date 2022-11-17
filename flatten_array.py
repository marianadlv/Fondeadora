def flatten_array_recursive(idx, input_array, output_array):
    if idx >= len(input_array):
        return output_array
    if isinstance(input_array[idx], int):
        output_array.append(input_array[idx])
    elif isinstance(input_array[idx], list):
        flatten_array_recursive(0, input_array[idx], output_array)
    else:
        raise TypeError("Only integers and lists of integers are allowed")

    flatten_array_recursive(idx + 1, input_array, output_array)

    return output_array


def flatten_array(input_array):
    if not isinstance(input_array, list):
        raise TypeError("The input must be a list")

    output_array = flatten_array_recursive(0, input_array, [])

    return output_array
