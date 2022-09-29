def quadrado(numero):
    lista = []
    for teste in range(1,numero+1):
        a = "{} {} {}".format(teste,teste**2,teste**3)
        lista.append(a)
    
    return lista