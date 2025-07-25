
while  True:
    
    valor1 = input("informe um primeiro numero")
    valor2 = input("informe um segundo valor")
    operador = input("informe uma operacao (+; - ; *; /)")
    
    numeros_validos = None
    val_1_float = 0
    val_2_float = 0
    
        
    try:
            val_1_float = float(valor1)
            val_2_float = float(valor2)
            
    except:
            numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou dois números digitados não são válidos")
        continue
    
    operadores_permitidos = "+/-*"
    
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print("digite apenas operadores válidos")
        
    print("Realizando a operação")
    
    if operador == "+":
        print(val_1_float + val_2_float)
    elif operador == "-":
        print(val_1_float - val_2_float)
    elif operador == "*":
        print(val_1_float * val_2_float)
    elif operador == "/":
        print(val_1_float / val_2_float)
    
    else:
        print("Fim das operações")
    
    sair = input('Deseja sair? [s]im: ').lower( ) .startswith('s')

    if sair is True:
         break   