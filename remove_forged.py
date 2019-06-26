with open('prefix.txt', 'r') as file:
    lines = file.readlines()

prefix_list = [p.strip() for p in sorted(lines)]


def binary_search(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = int(l + (r - l) / 2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


def is_forged(mac):
    check = mac[:6].upper()
    length = len(prefix_list)
    idx = binary_search(prefix_list, 0, length - 1, check)
    return idx != -1


if __name__ == '__main__':
    print(is_forged('482CA04A7D89'))
