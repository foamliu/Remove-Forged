with open('prefix.txt', 'r') as file:
    lines = file.readlines()

prefix_set = {x.strip() for x in lines}


def is_forged(mac):
    check = mac[0:6].upper()
    return check in prefix_set


if __name__ == '__main__':
    print(is_forged('482CA04A7D89'))
    print(is_forged('000000000000'))
