




token = 'foo bar'

text = """ bar foo bar
foo barbar foo
foofoo foo bar
"""
count = 0
tmp = 0
#para guardar la palabra
token_tmp = ''
#recorriendo letra por letra el texto
for i in text:
    #cuando la letra haga match con el token que entra
    if i == token[tmp]:
        #para determinar el inicio de la palabra
        if 0 == tmp:
            start = count
        tmp += 1
        token_tmp += i
        #si la cadena esta completa
        if len(token) == tmp:
            tmp = 0
            print(f'encontrada -> {token_tmp} | inicio -> {start} | Final -> {count}')
            token_tmp = ''
    #si no coinciden
    else:
        tmp = 0
        token_tmp = ''
        #print(f'{i} no es igual a "{token[tmp]}" | contador: {count}')
    count += 1


    
