#!/usr/bin/env python3
import cgi
import random




print("Content-type: text/html")
print()


print('''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Считай!</title>
</head>
<body>
''')

form = cgi.FieldStorage()
a = form.getfirst("a")
b = form.getfirst("b")
answer = form.getfirst("answer")
if a != None:
    a, b = int(a), int(b)
    answer = int(answer)
    if a + b == answer:
        print(f'У вас правильный ответ на пример {a} + {b} = {answer}')
    else:
        print(f'У вас неправильный ответ <b>{answer}</b> на пример <b>{a} + {b}</b><br>')
        print(f'Правильный ответ: {a} + {b} = {a + b}')


a, b = random.randint(0, 10), random.randint(0, 10)
print(f'''
<form action="schot.py">
        <p>
            {a} + {b} = 
            <input type="text" name="answer">
        </p>
        <input type="hidden" name="a" value="{a}">
        <input type="hidden" name="b" value="{b}">
        <input type="submit" value="ПРОВЕРИТЬ!">
    </form>

''')





print('''
<br><a href="../index.html">перейти на главную</a>
</body>
</html>
''')