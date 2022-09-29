def notas_validas(nota1, nota2):
    notas_validas = 0
    media = 0

    if nota1 >= 0 and nota1 <= 10:
        notas_validas = notas_validas + 1
        media = media + nota1

    if nota2 >= 0 and nota2 <= 10:
        notas_validas = notas_validas + 1
        media = media + nota2
    
    if notas_validas < 2:
        return "alguma nota invalida"
    else:
        return media/2

