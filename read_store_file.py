def store_to_txt(filename, U, subsets, costs):
    with open(filename, 'w') as f:
        f.write(f'U: {list(U)}\n')
        f.write(f'subsets: {subsets}\n')
        f.write(f'costs: {costs}\n')


def read_from_txt(filename):
    with open(filename, 'r') as f:
        U = set(eval(f.readline().split(':')[1].strip()))
        subsets = eval(f.readline().split(':')[1].strip())
        costs = eval(f.readline().split(':')[1].strip())
    return U, subsets, costs