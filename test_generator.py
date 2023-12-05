import random

from read_store_file import store_to_txt


def generate_weighted_set_cover(n, m, l):
    possible_numbers = range(n)

    U = set(range(1, n+1))

    subsets = []
    control = set()
    for i in range(l - 1):
        sub_size = random.randrange(1, m)
        sub = set(random.sample(list(U), sub_size))  # convert U to list before passing to random.sample()
        subsets.append(sub)
        control |= sub

    rest = U - control
    if rest:
        subsets.append(rest)

    costs = [random.randint(1, 200) for _ in range(l)]

    return U, subsets, costs


def create_and_save_dataset(file_name, n, m, l):
    U, subsets, costs = generate_weighted_set_cover(n, m, l)
    store_to_txt(file_name, U, subsets, costs)
    print(f'{file_name} has been saved')


def main():
    for i in range(1, 4):
        create_and_save_dataset(f'./dataset/kecil_{i}.txt', 20, 10, 20)
        create_and_save_dataset(f'./dataset/sedang_{i}.txt', 200, 100, 25)
        create_and_save_dataset(f'./dataset/besar_{i}.txt', 2000, 1000, 30)


if __name__ == '__main__':
    main()
    print('Datasets have been generated')
