with open('../huddle.py') as file:
    code = compile(file.read(), "../huddle.py", 'exec')
    exec(code)
