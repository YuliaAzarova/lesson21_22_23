def Caesar(x):
    if 'A' <= x <= 'Z':
        tmp = ord(x) - 3
        if tmp > ord('Z'):
            tmp -= 26
        x = chr(tmp)
    elif 'a' <= x <= 'z':
        tmp = ord(x) - 3
        if tmp > ord('z'):
            tmp += 26
        x = chr(tmp)

    return x


s = input()
for elem in s:
    print(Caesar(elem), end='')