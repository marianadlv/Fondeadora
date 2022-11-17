from flatten_array import flatten_array

inputs = [
    [1, [2, [3, [4, 5]]]],
    [1, [2]],
    [1, [2, [3, [4, [5]]]]],
    [1, 2, 3, 4, 5],
    [[1], [2]],
    [1, [2, 3, 4, 5]],
    [[1], 2],
    []
]

for idx, input_array in enumerate(inputs):
    output_array = flatten_array(input_array)
    print(f'Case #{idx + 1}:\nInput array: {input_array}\nOuput array: {output_array}\n')

