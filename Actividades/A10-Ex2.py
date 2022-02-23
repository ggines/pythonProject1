def main():
    num=int(input("Introduce la cantidad de notas: "))
    lista = []
    aprobados = []
    suspendidos = []
    sumaAprobados=0
    sumaSuspendidos=0
    for x in range(num):
        nota=int(input("Introduce la nota (del 1 al 10): "))
        while nota < 1 or nota > 10:
            nota = int(input("Introduce la nota (del 1 al 10): "))
        lista.append(nota)

    for nota in lista:
        if nota >=5:
            aprobados.append(nota)
        elif nota <= 4:
            suspendidos.append(nota)

    for notas in aprobados:
        sumaAprobados+=notas

    for notas in suspendidos:
        sumaSuspendidos+=notas
    print("La media de aprobados es", sumaAprobados/num)
    print("La media de suspendidos es", sumaSuspendidos/num)
    print("Hay", len(aprobados), "aprobados", "y", len(suspendidos), "suspendidos")

if __name__ == '__main__':
    main()