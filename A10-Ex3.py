def main():

    num=int(input("Cuantos usuarios quieres insertar?: "))
    for x in range(num):
        usuarios= {
            "username": str(input("Introduce el nombre del usuario: ")),
            "department": str(input("Introduce el departamento: ")),
            "classroom": int(input("Introduce el numero de clase (entre 1 i 15): "))
        }
        while usuarios["classroom"] < 1 or usuarios["classroom"] > 15:
            usuarios["classroom"]= int(input("Introduce el numero de clase (entre 1 i 15): "))
    print("El usuario es", usuarios["username"], ", el departamento es", usuarios["department"], "y el classroom es", usuarios["classroom"])

if __name__ == '__main__':
    main()
