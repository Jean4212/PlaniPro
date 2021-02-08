from Conexion import executeQuery








databasePath = {'host'     :'localhost',
                'port'     :3306,
                'user'     :'root',
                'password' :'root',
                'database' :'planipro'}

#dni = input('\nIngresa el DNI: ')
#apaterno = input('Ingresa el Apellido Paterno: ')
#amaterno = input('Ingresa el Apellido Materno: ')
#pnombre = input('Ingresa el Primer Nombre: ')
#snombre = input('Ingresa el Segundo Nombre: ')
#fnacimiento = input('Ingresa la Fecha de Nacimiento: ')
#espacio = 0 
        #for row in tabla:
            #dni = row[0]
            #nombre = row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4]
            #nacimiento = row[5]        
            #ttk.Label(self.app, text=nombre, anchor='w', style='BW.TLabel', cursor='hand2').place(x=10, y=10+espacio, width=360, height=24)
            #ttk.Label(self.app, text=dni, anchor='w', style='BW.TLabel', cursor='hand2').place(x=360, y=10+espacio, width=100, height=24)
            #ttk.Label(self.app, text=nacimiento, anchor='w', style='BW.TLabel', cursor='hand2').place(x=460, y=10+espacio, width=100, height=24)
            #ttk.Button(self.app, text='Eliminar',command=self.ocultar, cursor='hand2').place(x=570, y=10+espacio, width=80, height=24)
            #ttk.Button(self.app, text='Editar', cursor='hand2').place(x=650, y=10+espacio, width=80, height=24)
            #ttk.Button(self.app, text='Detalle', cursor='hand2').place(x=730, y=10+espacio, width=80, height=24)
            #ttk.Button(self.app, text='Reporte', cursor='hand2').place(x=810, y=10+espacio, width=80, height=24)
            #espacio = espacio + 24



        button01 = Button(self, text    ='OROPEZA INCA JEANCARLOS ALBERTO', 
                                bg      ='#6B6864',
                                relief  ='flat',   
                                bd      =0,   
                                cursor  ='hand2',                             
                                anchor  ='center',
                                activebackground    ='#6B6864',                                                     
                                command =lambda: DatosPersonales(self),
                                font    =("Trebuchet MS", 10,'bold'))

        button02 = Button(self, text    ='Datos Personales', 
                                bg      ='#6B6864',
                                relief  ='flat',   
                                bd      =0,   
                                cursor  ='hand2',   
                                activebackground    ='#6B6864',                                                     
                                command =lambda: DatosLaborales(self),
                                font    =("Trebuchet MS", 10,'bold'))

        button03 = Button(self, text    ='Datos Personales', 
                                bg      ='#6B6864',
                                relief  ='flat',   
                                bd      =0,   
                                cursor  ='hand2',   
                                activebackground    ='#6B6864',                                                     
                                command =lambda: DatosAdicionales(self),
                                font    =("Trebuchet MS", 10,'bold'))  





#query = f"INSERT INTO trabajadores (dni, apaterno, amaterno, pnombre, snombre, fnacimiento) VALUES ('{dni}', '{apaterno}', '{amaterno}', '{pnombre}', '{snombre}', '{fnacimiento}')"
query = 'SELECT * FROM trabajadores'  

f = executeQuery(databasePath, query, False)
print(f)

class DatosPersonales(Toplevel):
    def __init__(self, parent):
        super(DatosPersonales, self).__init__()

        self.title('Datos Personales')
        #self.geometry('400x200+-8+0')
        self.resizable(0,0)
        self.configure(bg='#171515') 
        
        label01 = Label(self,   text    ='DNI',                                 
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                                
                                width   =18,                                
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))
        
        label02 = Label(self,   text    ='APELLIDO PATERNO',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label03 = Label(self,   text    ='APELLIDO MATERNO',
                                bg      ='#393834',  
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label04 = Label(self,   text    ='PRIMER NOMBRE',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label05 = Label(self,   text    ='SEGUNDO NOMBRE',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label06 = Label(self,   text    ='FECHA DE NACIMIENTO',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label01.grid(row =0, column =0, padx =10, pady =1)

        label02.grid(row =1, column =0, padx =10, pady =1)

        label03.grid(row =2, column =0, padx =10, pady =1)

        label04.grid(row =3, column =0, padx =10, pady =1)

        label05.grid(row =4, column =0, padx =10, pady =1)

        label06.grid(row =5, column =0, padx =10, pady =1)
        
        self.textbox01 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',                                
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',                                 
                                insertbackground    ='#898879',                                                       
                                font    =('Trebuchet MS', 11,'bold')) 

        self.textbox02 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',    
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',  
                                insertbackground    ='#898879',                                      
                                font    =('Trebuchet MS', 11,'bold'))
        
        self.textbox03 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',     
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',  
                                insertbackground    ='#898879',                                     
                                font    =('Trebuchet MS', 11,'bold'))
        
        self.textbox04 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',   
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E', 
                                insertbackground    ='#898879',                                        
                                font    =('Trebuchet MS', 11,'bold'))
        
        self.textbox05 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',     
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E', 
                                insertbackground    ='#898879',                                      
                                font    =('Trebuchet MS', 11,'bold'))   

        self.textbox06 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',     
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E', 
                                insertbackground    ='#898879',                                      
                                font    =('Trebuchet MS', 11,'bold'))       

        self.textbox01.grid(row =0, column =1, padx =10, pady =1)

        self.textbox02.grid(row =1, column =1, padx =10, pady =1)

        self.textbox03.grid(row =2, column =1, padx =10, pady =1)

        self.textbox04.grid(row =3, column =1, padx =10, pady =1)

        self.textbox05.grid(row =4, column =1, padx =10, pady =1)

        self.textbox06.grid(row =5, column =1, padx =10, pady =1)

        boton1 = Button(self, text='Grabar', command=self.almacenardatos)
        boton1.grid(row=6, column=0)

        self.focus_set()      
        self.transient(parent)        
        self.grab_set()

    def almacenardatos(self):
        self.datos = [   self.textbox01.get(),
                    self.textbox02.get(),
                    self.textbox03.get(),
                    self.textbox04.get(),
                    self.textbox05.get(),
                    self.textbox06.get()]

        print(self.datos)
 
class DatosLaborales(Toplevel):
    def __init__(self, parent):
        super(DatosLaborales, self).__init__()

        self.title('Datos Laborales')
        #self.geometry('400x200+-8+0')
        self.resizable(0,0)
        self.configure(bg='#171515') 
        
        label01 = Label(self,   text    ='FECHA DE INGRESO',                                 
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                                
                                width   =18,                                
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))
        
        label02 = Label(self,   text    ='SUELDO MENSUAL',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label03 = Label(self,   text    ='PUESTO LABORAL',
                                bg      ='#393834',  
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label04 = Label(self,   text    ='APORTE DE PENSION',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label05 = Label(self,   text    ='CUENTA BANCARIA',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))
        
        label01.grid(row =6, column =0, padx =10, pady =1)

        label02.grid(row =7, column =0, padx =10, pady =1)

        label03.grid(row =8, column =0, padx =10, pady =1)

        label04.grid(row =9, column =0, padx =10, pady =1)

        label05.grid(row =10, column =0, padx =10, pady =1)
     
        textbox01 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',                                
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',                                 
                                insertbackground    ='#898879',                                                       
                                font    =('Trebuchet MS', 11,'bold')) 

        textbox02 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',    
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',  
                                insertbackground    ='#898879',                                      
                                font    =('Trebuchet MS', 11,'bold'))
        
        textbox03 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',     
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',  
                                insertbackground    ='#898879',                                     
                                font    =('Trebuchet MS', 11,'bold'))
        
        textbox04 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',   
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E', 
                                insertbackground    ='#898879',                                        
                                font    =('Trebuchet MS', 11,'bold'))
        
        textbox05 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',     
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E', 
                                insertbackground    ='#898879',                                      
                                font    =('Trebuchet MS', 11,'bold'))   
       
        textbox01.grid(row =6, column =1, padx =10, pady =1)

        textbox02.grid(row =7, column =1, padx =10, pady =1)

        textbox03.grid(row =8, column =1, padx =10, pady =1)

        textbox04.grid(row =9, column =1, padx =10, pady =1)

        textbox05.grid(row =10, column =1, padx =10, pady =1)

        self.focus_set()      
        self.transient(parent)        
        self.grab_set()

class DatosAdicionales(Toplevel):
    def __init__(self, parent):
        super(DatosAdicionales, self).__init__()

        self.title('Datos Adicionales')
        #self.geometry('400x200+-8+0')
        self.resizable(0,0)
        self.configure(bg='#171515') 
        
        label01 = Label(self,   text    ='CATEGORIA DE LICENCIA',                                 
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                                
                                width   =18,                                
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))
        
        label02 = Label(self,   text    ='FECHA DE VENCIMIENTO LICENCIA',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label03 = Label(self,   text    ='NUMERO DE EMERGENCIA 1',
                                bg      ='#393834',  
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label04 = Label(self,   text    ='NUMERO DE EMERGENCIA 2',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))

        label05 = Label(self,   text    ='OTRO DATO',
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                          
                                width   =18,                               
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))
        
        label01.grid(row =6, column =0, padx =10, pady =1)

        label02.grid(row =7, column =0, padx =10, pady =1)

        label03.grid(row =8, column =0, padx =10, pady =1)

        label04.grid(row =9, column =0, padx =10, pady =1)

        label05.grid(row =10, column =0, padx =10, pady =1)
     
        textbox01 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',                                
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',                                 
                                insertbackground    ='#898879',                                                       
                                font    =('Trebuchet MS', 11,'bold')) 

        textbox02 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',    
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',  
                                insertbackground    ='#898879',                                      
                                font    =('Trebuchet MS', 11,'bold'))
        
        textbox03 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',     
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',  
                                insertbackground    ='#898879',                                     
                                font    =('Trebuchet MS', 11,'bold'))
        
        textbox04 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',   
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E', 
                                insertbackground    ='#898879',                                        
                                font    =('Trebuchet MS', 11,'bold'))
        
        textbox05 = Entry(self, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',     
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E', 
                                insertbackground    ='#898879',                                      
                                font    =('Trebuchet MS', 11,'bold'))   
       
        textbox01.grid(row =6, column =1, padx =10, pady =1)

        textbox02.grid(row =7, column =1, padx =10, pady =1)

        textbox03.grid(row =8, column =1, padx =10, pady =1)

        textbox04.grid(row =9, column =1, padx =10, pady =1)

        textbox05.grid(row =10, column =1, padx =10, pady =1)

        self.focus_set()      
        self.transient(parent)        
        self.grab_set()
