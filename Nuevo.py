import os
import sys
import time
import mariadb
from colorama import Fore, init
init(autoreset=True)

class Menu_Principal():
    def __init__(self):        
        self.menu = {
            '1' : self.registrar,
            '2' : self.modificar,
            '3' : self.eliminar,
            '4' : self.consultar,
            '5' : self.trabajadoresregistrados,
            '6' : self.salir
        }

class Menu():

    def __init__(self):        
        self.menu = {
            '1' : self.registrar,
            '2' : self.modificar,
            '3' : self.eliminar,
            '4' : self.consultar,
            '5' : self.trabajadoresregistrados,
            '6' : self.salir
        }        

    def arrancar_menu(self):        
        while True:
            os.system('cls')            
            eleccion = input('PlaniPRO V. 1.00\n1 Registrar Trabajador\n2 Modidicar Trabajador\n3 Eliminar Trabajador\n4 Consultar Trabajador\n5 Trabajadores Registrados\n6 Salir\nResponda: ')
            accion = self.menu.get(eleccion)
            if accion:
                accion()                                           
            else:
                print(Fore.RED + f'\n{eleccion} no es una eleccion valida')
                time.sleep(2)
                
    def registrar(self):    
        dni = input('\nIngresa el DNI: ')
        verificar = self.verificar(dni)
        if verificar:
            print(Fore.RED + '\nDNI ya registrado')    
            time.sleep(2)  
            os.system('cls')
            print('PlaniPRO V. 1.00\n1 Registrar Trabajador\n2 Modidicar Trabajador\n3 Eliminar Trabajador\n4 Consultar Trabajador\n5 Trabajadores Registrados\n6 Salir\nResponda: 1')
            self.registrar()      
        else:
            apaterno = input('Ingresa el Apellido Paterno: ')
            amaterno = input('Ingresa el Apellido Materno: ')
            pnombre = input('Ingresa el Primer Nombre: ')
            snombre = input('Ingresa el Segundo Nombre: ')
            fnacimiento = input('Ingresa la Fecha de Nacimiento: ')
            query = f"INSERT INTO trabajadores (dni, apaterno, amaterno, pnombre, snombre, fnacimiento) VALUES ('{dni}', '{apaterno}', '{amaterno}', '{pnombre}', '{snombre}', '{fnacimiento}')"
            self.__conexion(query,True,False)
            print(Fore.BLUE + '\nTrabajar registrado de manera satisfactoria')
            time.sleep(2)

    def modificar(self):
        dni = input('\nIngresa el DNI: ')
        verificar = self.verificar(dni)
        if verificar:
            nuevodni = input('Ingresa el nuevo DNI: ')
            apaterno = input('Ingresa el nuevo Apellido Paterno: ')
            amaterno = input('Ingresa el nuevo Apellido Materno: ')
            pnombre = input('Ingresa el nuevo Primer Nombre: ')
            snombre = input('Ingresa el nuevo Segundo Nombre: ')
            fnacimiento = input('Ingresa la nuevo Fecha de Nacimiento: ')
            query = f"UPDATE trabajadores SET dni = '{nuevodni}', apaterno = '{apaterno}', amaterno = '{amaterno}', pnombre = '{pnombre}', snombre = '{snombre}', fnacimiento = '{fnacimiento}' WHERE dni = '{dni}'"
            self.__conexion(query,True,False)
            print(Fore.BLUE + '\nTrabajar actualizado de manera satisfactoria')
            time.sleep(2)
        else:
            print(Fore.RED + '\nDNI no registrado')    
            time.sleep(2)  
            os.system('cls')
            print('PlaniPRO V. 1.00\n1 Registrar Trabajador\n2 Modidicar Trabajador\n3 Eliminar Trabajador\n4 Consultar Trabajador\n5 Trabajadores Registrados\n6 Salir\nResponda: 2')
            self.modificar()   
            
    def eliminar(self):
        dni = input('\nIngresa el DNI: ')
        verificar = self.verificar(dni)
        if verificar: 
            query = f"DELETE FROM trabajadores WHERE dni = '{dni}'"
            self.__conexion(query,True,False)
            print(Fore.BLUE + '\nTrabajar eliminado de manera satisfactoria')
            time.sleep(2)       
        else:
            print(Fore.RED + '\nDNI no registrado')    
            time.sleep(2)  
            os.system('cls')
            print('PlaniPRO V. 1.00\n1 Registrar Trabajador\n2 Modidicar Trabajador\n3 Eliminar Trabajador\n4 Consultar Trabajador\n5 Trabajadores Registrados\n6 Salir\nResponda: 3')
            self.eliminar()  

    def consultar(self):
        dni = input('\nIngresa el DNI: ')
        verificar = self.verificar(dni)
        if verificar:
            query = f"SELECT dni, apaterno, amaterno, pnombre, snombre, fnacimiento FROM trabajadores WHERE dni = '{dni}'"
            resultado = self.__conexion(query,False,False) 
            print('Apellido Paterno: ', Fore.BLUE + resultado[1])
            print('Apellido Materno: ', Fore.BLUE + resultado[2])
            print('Primer Nombre: ', Fore.BLUE + resultado[3])
            print('Segundo Nombre: ', Fore.BLUE + resultado[4]) 
            print('Fecha Nacimiento: ', Fore.BLUE + resultado[5])   
            time.sleep(10)   
        else:            
            print(Fore.RED + '\nTrabajador no existe')
            time.sleep(2) 
            os.system('cls')
            print('PlaniPRO V. 1.00\n1 Registrar Trabajador\n2 Modidicar Trabajador\n3 Eliminar Trabajador\n4 Consultar Trabajador\n5 Trabajadores Registrados\n6 Salir\nResponda: 4')
            self.consultar()

    def trabajadoresregistrados(self):
        query = f'SELECT * FROM trabajadores'
        resultado = self.__conexion(query,False,True)  
        if resultado:
            print('')
            for fila in resultado:                
                print(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])  
            time.sleep(10)                         
        else:
            print(Fore.RED + '\nNo hay registros para mostrar')      
            time.sleep(2)

    def salir(self):
        sys.exit(0)

    def verificar(self,dni):
        query = f"SELECT dni FROM trabajadores WHERE dni = '{dni}'"
        resultado = self.__conexion(query,False,False)  
        if resultado == None:
            return False
        else:    
            return True               
    
    def __conexion(self,query,commit,fetchall):        
        try:
            conexion = mariadb.connect(host='localhost', port=3306, user='root', password='root', database='planipro')
            cursor = conexion.cursor()          
            cursor.execute(query)  
            if commit:
                conexion.commit()           
            else:
                if fetchall:
                    return cursor.fetchall()
                else:                       
                    return cursor.fetchone()
            conexion.close() 
        except mariadb.Error as error:
            print(error)

if __name__ == '__main__':
    Menu().arrancar_menu()