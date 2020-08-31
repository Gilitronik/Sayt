#!/usr/bin/env python3
import cgi
import html


form = cgi.FieldStorage()
our_login = form.getfirst("login", "")
our_apassword = form.getfirst("apass", "")
our_bpassword = form.getfirst("bpass", "")
our_secret = form.getfirst("secret", "")


our_login = html.escape(our_login)
our_apassword = html.escape(our_apassword)
our_bpassword = html.escape(our_bpassword)
our_secret = html.escape(our_secret)

print("Content-type: text/html")
print()



print('''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Краду наши пароли</title>
</head>
<body>
''')



if our_login == "":
    print('<a href="../registration.html">перейти на регистрация</a><br>')
    print('Ты не ввёл логин')
elif our_apassword == "":
    print('<a href="../registration.html">перейти на регистрация</a><br>')
    print('Ты не ввёл пароль')
elif our_bpassword == "":
    print('<a href="../registration.html">перейти на регистрация</a><br>')
    print('Ты не ввёл пароль повторно')
elif our_secret == "":
    print('<a href="../registration.html">перейти на регистрация</a><br>')
    print('Ты не ввёл секрет')
elif our_apassword != our_bpassword:
    print('<a href="../registration.html">перейти на регистрация</a><br>')
    print('Пароли не совпадают')
else:
    f = open('users.txt', 'r')
    text = f.read()
    rar = []
    arr = text.split('\n')
    slov = dict()
    for i in range(0, len(arr), 4):
        if arr[i] == 'login:'+our_login:
            print('<a href="../registration.html">перейти на регистрация</a><br>')
            print('Такой юзер уже есть')
            break
    else:
        f.close()
        f = open('users.txt', 'a', encoding='utf-8')
        f.write(f"""
login:{our_login}
pass:{our_apassword}
secret:{our_secret}
===""")
        print(f'Здравствуйте, вы успешно зарегистрированны, {our_login}!<br>Ваш секрет --> {our_secret}')
    f.close()
    
    del(text)
    del(slov)
    del(arr)


print('''
<br><a href="../index.html">перейти на главную</a>
</body>
</html>
''')