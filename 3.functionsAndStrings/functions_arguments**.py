# Aggiungendo * abbiamo un numero illimitato di argomenti da poter aggiungere
def unlimited_arguments(*args):
    print(args)  # tuple
    for argument in args:
        print(argument)


unlimited_arguments(1, 2, 3, 4)
unlimited_arguments(*[1, 2, 3, 4])
print(*[1, 2, 3, 4])

print('-'*90)

# kargs = keyword arguments


def unlimited_dict_arguments(*args, **keyword_args):
    print(keyword_args)  # dictionary
    for argument in keyword_args.items():
        print(argument)
    for argument in keyword_args.keys():
        print(argument)
    for argument in keyword_args.values():
        print(argument)


unlimited_dict_arguments(1, 2, 3, 4, name='Marco', age=26)
