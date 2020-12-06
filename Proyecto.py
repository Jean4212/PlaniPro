import tkinter as tk
from tkinter import Event, Frame, Image, Label, PhotoImage, ttk
from tkinter.constants import CENTER, EXTENDED, NONE

class programa():

    def __init__(self): 

        self.app = tk.Tk()
        self.app.title('PlaniPRO')
        self.app.geometry('900x600+-8+0')
        self.app.resizable(0,0)
        self.app.configure(bg='#101417') 



        
       
        #Label(self.app,se image=self.imagen).place(x=-2, y=0)      

        s = ttk.Style()
        s.configure('Kim.TLabel', background='#FBFCFD',)
        a = ttk.Style()
        a.configure('Kim2.TLabel', background='#101417')
        b = ttk.Style()
        b.configure('Kim3.TFrame', background='#FBFCFD')
        p = ttk.Style()
        p.configure('Kim.Treeview', background='#FBFCFD', font=('Trebuchet MS', 10))


        # Crear Botones
        self.boton1 = ttk.Label(self.app, cursor='hand2')   #, style='Kim.TLabel', image=self.imagen)
        self.boton2 = ttk.Label(self.app, cursor='hand2')
        self.boton3 = ttk.Label(self.app, cursor='hand2')
        self.boton4 = ttk.Label(self.app, cursor='hand2')
        self.boton5 = ttk.Label(self.app, cursor='hand2')
        self.boton6 = ttk.Label(self.app, cursor='hand2')

        # Crear Ventanas
        self.ventana1 = ttk.Frame(self.app)
        self.ventana2 = ttk.Frame(self.app)
        self.ventana3 = ttk.Frame(self.app)
        self.ventana4 = ttk.Frame(self.app)
        self.ventana5 = ttk.Frame(self.app)
        self.ventana6 = ttk.Frame(self.app)

        # Crear Objetos de Ventana 1
        self.ventana1_label1 = ttk.Label(self.ventana1, text='TRABAJADORES',anchor=CENTER)
        self.ventana1_listbox1 = ttk.Treeview(self.ventana1,selectmode='browse',columns=('A','B'),show='headings',style='Kim.Treeview')
        self.ventana1_boton1 = ttk.Button(self.ventana1,text='Nuevo',cursor='hand2')

        #self.ventana1_boton1.bind('<Boton-1>',crear)
        hola = 'mama'
        hola2 = 'papa'
        #print("gdgdgd %s y %s" %(hola,hola2))
        #print("gdgdgd {} y {}".format(hola,hola2))

        self.ventana1_listbox1.heading('A', text='DNI', anchor=tk.CENTER)
        self.ventana1_listbox1.heading('B', text='APELLIDOS Y NOMBRES', anchor=tk.CENTER)
        self.ventana1_listbox1.column('A', stretch=tk.NO, width=70)
        self.ventana1_listbox1.column('B', stretch=tk.NO, width=308)
       

        self.ventana1_listbox1.place(x=10,y=30,width=380,height=550)
        self.ventana1_label1.place(x=0,y=0,width=800,height=30)
        self.ventana1_boton1.place(x=400,y=556)
        #self.boton5.bind('<Button-1>',lambda a: self.mostrarOcultar(self.ventana5))

        self.ventana1_listbox1.insert('', 'end', values=('48555618','OROPEZA INCA JEANCARLOS ALBERTO'))
        self.ventana1_listbox1.insert('', 'end', values=('71260453','LAURA HUAMAN KARINA'))
        self.ventana1_listbox1.insert('', 'end', values=('45998421','AGAMA HERRERA JUANA MARCELINA'))




        self.ventana1.place(x=100,y=0,width=800,height=600)
        #self.ventana2.place(x=100,y=0,width=800,height=600)
        #self.ventana3.place(x=100,y=0,width=800,height=600)
        #self.ventana4.place(x=100,y=0,width=800,height=600)
        #self.ventana5.place(x=100,y=0,width=800,height=600)
        #self.ventana6.place(x=100,y=0,width=800,height=600)

        self.boton1.place(x=0, y=000, width=100, height=100)  
        self.boton2.place(x=0, y=100, width=100, height=100) 
        self.boton3.place(x=0, y=200, width=100, height=100) 
        self.boton4.place(x=0, y=300, width=100, height=100) 
        self.boton5.place(x=0, y=400, width=100, height=100) 
        self.boton6.place(x=0, y=500, width=100, height=100) 



        self.app.mainloop()  

        

    
        

if __name__ == '__main__':
    aplicacion = programa()

