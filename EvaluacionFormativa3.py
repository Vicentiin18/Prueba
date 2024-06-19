


descAfp=0.12
cargos=[]
SueldoBruto=[]
ListaTrabajador=[]
descSalud=0.07






while True:
    try:

        print("1. Registrar trabajador")
        print("2. Listar todo los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del Programa")

        opc=int(input())
        
        if opc==1: 
            nombreApellido=input("Ingrese su nombre y apellido: ")
            ListaTrabajador.append(nombreApellido)
            print("Seleccione su cargo: \n1. CEO\n2. Desarrollador\n3. Analista de datos")
            cargo=int(input())
            if cargo==1:
                cargo="CEO"
                cargos.append(cargo)
                print(f"{nombreApellido}, seleccionaste el cargo de CEO")
                sueldoBruto=int(input("Ingrese su sueldo: \n"))
                suelAfp=(sueldoBruto*descAfp)
                suelSalud=(sueldoBruto*descSalud)
                sueldoLiquido=(sueldoBruto-suelAfp-suelSalud)
                
            
            elif cargo==2:
                cargo="Desarrollador"
                cargos.append(cargo)
                print(f"{nombreApellido}, seleccionaste el cargo de Desarrollador")
                sueldoBruto=int(input("Ingrese su sueldo: \n"))
                suelAfp=(sueldoBruto*descAfp)
                suelSalud=(sueldoBruto*descSalud)
                sueldoLiquido=(sueldoBruto-suelAfp-suelSalud)
                
            elif cargo==3:
                cargo="Analista de datos"
                cargos.append(cargo)
                print(f"{nombreApellido}, seleccionaste el cargo de Analista de datos")
                sueldoBruto=int(input("Ingrese su sueldo: \n"))
                SueldoBruto.append(sueldoBruto)
                suelAfp=(sueldoBruto*descAfp)
                suelSalud=(sueldoBruto*descSalud)
                sueldoLiquido=(sueldoBruto-suelAfp-suelSalud)

        if opc==2:
            for i in range (len(ListaTrabajador)):
                print(f"{i+1}.-{ListaTrabajador[i]}")
             
        if opc==3:
            
            with open ('RegistroTrajadores.txt','w') as x:
                for i in range (len(ListaTrabajador)):
                    x.write(f"{ListaTrabajador}   |   {cargos}    |    {sueldoBruto}   |    {suelAfp}    |    {suelSalud}    |    {sueldoLiquido}    \n")
            for i in range (len(ListaTrabajador)):
                print(f"{ListaTrabajador[i]}   |   {cargos[i]}    |    {sueldoBruto[i]}   |    {suelAfp[i]}    |    {suelSalud[i]}    |    {sueldoLiquido[i]}    ")

        if opc==4:
            print("Saliendo....")
            break            
            
            
    except ValueError:
        print("Error, solo valores numericos")
