import re


l = ['a', 'b', 'c']


def concatenate_list_to_str(l):
    print (''.join(l))


def create_2d_list(size):
    print ([[x+(y*size) for x in range(size)] for y in range(size)])

d = {
    'Jaś': 10,
    'Jan': 15,
    'Adam': 20,
}


def search_dict_by_value(d, search):
    for name, age in d.items():
        if age == search:
            print(name, age)

def validate_email(email):
    pattern = re.compile(r'([^@]){3,}@([a-zA-Z0-9]){1,}\.([a-zAZ0-9]){1,}')
    res = pattern.match(email)
    if res:
        print('MATCHED')
    else:
        print('NOT MATCHED')

def name_in_frame():
    usr_inp = input()
    usr_inp_len = len(usr_inp)
    print ((usr_inp_len + 2) * '*')
    print ('*' + usr_inp + '*')
    print ((usr_inp_len + 2) * '*')


def odd_one():
    usr_inp = input()
    print(usr_inp[::2])


s = 'asdj3hj429f29103'


def only_digits(inp):
    print(''.join(c for c in inp if c.isdigit()))

if __name__ == '__main__':
    print('CONCATENATE')
    concatenate_list_to_str(l)
    print('\n')

    print('2D ARRAY')
    create_2d_list(4)
    print('\n')

    print('VALIDATE EMAIL')
    validate_email('231@wp.pl')
    print('\n')

    print('SEARCH DICT')
    search_dict_by_value(d, 15)
    print('\n')

    print('INPUT IN FRAME')
    name_in_frame()
    print('\n')

    print('ODD ONE')
    odd_one()
    print('\n')

    print('ONLY DIGITS')
    only_digits(s)
    print('\n')
