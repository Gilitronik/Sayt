#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
our_login = form.getfirst("login", "")
our_password = form.getfirst("pass", "")

our_login = html.escape(our_login)
our_password = html.escape(our_password)


print("Content-type: text/html")
print()



print('''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Краду ваши пароли</title>
</head>
<body>
''')


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
    if user['login'] == our_login:
        if user['pass'] == our_password:
            print(f'Здравствуйте, {our_login}!<br>Ваш секрет --> {user["secret"]}')
        else:
            print(f'Пароль не верный<br>')
        break
else:
    print(f'Пользователя {our_login} нет<br>')
    print(f'<a href="#">зарегистрироваться</a>')


# print(f'Привет, {our_login}!<br>')
# if our_password == '12345678':
#     print(f'Твой пароль {our_password} совсем плохой!<br>')
# else:
#     print(f'Твой пароль {our_password} не совсем плохой!<br>')




print('''
<br><a href="../index.html">вернуться на главную</a>
</body>
</html>
''')
