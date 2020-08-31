f = open('users.txt', 'r')
text = f.read()
rar = []
arr = text.split('\n')
slov = dict()
for i in range(len(arr)):
    if arr[i] == '===':
        rar.append(slov)
        slov = dict()
    else:
        a, b = arr[i].split(':')
        slov[a] = b
f.close()
del(text)
del(slov)
del(arr)

for user in rar:
    print(user)
    print('423423324' + user['login'])