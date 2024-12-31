data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
count = 0


def calculate_structure_sum(lst):
    global count
    for n in lst:
        if isinstance(n, int) or isinstance(n, float):
            count += n
        elif isinstance(n, str):
            count += len(n)
        elif isinstance(n, list) or isinstance(n, tuple) or isinstance(n, set):
            calculate_structure_sum(n)
        elif isinstance(n, dict):
            for item in n.items():
                calculate_structure_sum(item)
    return count


result = calculate_structure_sum(data_structure)
print(result)