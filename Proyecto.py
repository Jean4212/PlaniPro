
from tkinter import Button, Entry, Frame, Label, Tk, Toplevel
from tkinter.constants import END
from tkinter.ttk import Treeview, Style

class App(Tk):

    def __init__(self):
        super(App, self).__init__()  

        self.ventanaActive = 0
        self.title('PlaniPRO')
        self.geometry('900x600+-8+0')
        self.resizable(0,0)
        self.configure(bg='#171515') 

        self.label01 = Label(self,  bg='#6B6864', cursor='hand2', text='PRIMERO')        
        self.label02 = Label(self,  bg='#6B6864', cursor='hand2', text='SEGUNDO')
        self.label03 = Label(self,  bg='#6B6864', cursor='hand2', text='TERCERO')
        self.label04 = Label(self,  bg='#6B6864', cursor='hand2', text='CUARTO')
        self.label05 = Label(self,  bg='#6B6864', cursor='hand2', text='QUINTO')
        self.label06 = Label(self,  bg='#6B6864', cursor='hand2', text='SEXTO')
        
        self.label01.bind('<Button-1>', lambda event: self.botonAbajo(self.label01))
        self.label01.bind('<ButtonRelease-1>', lambda event: self.botonArriba(self.label01))

        self.label02.bind('<Button-1>', lambda event: self.botonAbajo(self.label02))
        self.label02.bind('<ButtonRelease-1>', lambda event: self.botonArriba(self.label02))

        self.label03.bind('<Button-1>', lambda event: self.botonAbajo(self.label03))
        self.label03.bind('<ButtonRelease-1>', lambda event: self.botonArriba(self.label03))
        
        self.label04.bind('<Button-1>', lambda event: self.botonAbajo(self.label04))
        self.label04.bind('<ButtonRelease-1>', lambda event: self.botonArriba(self.label04))
        
        self.label05.bind('<Button-1>', lambda event: self.botonAbajo(self.label05))
        self.label05.bind('<ButtonRelease-1>', lambda event: self.botonArriba(self.label05))
        
        self.label06.bind('<Button-1>', lambda event: self.botonAbajo(self.label06))
        self.label06.bind('<ButtonRelease-1>', lambda event: self.botonArriba(self.label06))

        self.label01.place(x=1,y=  1,width=98,height=98)        
        self.label02.place(x=1,y=101,width=98,height=98)        
        self.label03.place(x=1,y=201,width=98,height=98)       
        self.label04.place(x=1,y=301,width=98,height=98)        
        self.label05.place(x=1,y=401,width=98,height=98)        
        self.label06.place(x=1,y=501,width=98,height=98)
        
        self.menuActivo = 0

        self.mainloop()  
        
    def botonAbajo(self, boton):        
        if boton['text'] == 'PRIMERO':
            self.label01.place(x=0,y=0,width=100,height=100)             
        elif boton['text'] == 'SEGUNDO':
            self.label02.place(x=0,y=100,width=100,height=100)
        elif boton['text'] == 'TERCERO':
            self.label03.place(x=0,y=200,width=100,height=100)
        elif boton['text'] == 'CUARTO':
            self.label04.place(x=0,y=300,width=100,height=100)
        elif boton['text'] == 'QUINTO':
            self.label05.place(x=0,y=400,width=100,height=100)
        elif boton['text'] == 'SEXTO':
            self.label06.place(x=0,y=500,width=100,height=100)
        
    def botonArriba(self, boton): 
        self.destroyWindow()
        if boton['text'] == 'PRIMERO':            
            self.label01.place(x=1,y=  1,width=98,height=98)
            if self.menuActivo != 1:                
                print('abri 1')            
                self.menuActivo = 1
                self.menu01() 
            else:
                 self.menuActivo = 0  
        elif boton['text'] == 'SEGUNDO':
            self.label02.place(x=1,y=101,width=98,height=98)
            if self.menuActivo != 2:                
                print('abri 2')            
                self.menuActivo = 2
                self.menu02() 
            else:
                 self.menuActivo = 0 
        elif boton['text'] == 'TERCERO':
            self.label03.place(x=1,y=201,width=98,height=98)  
            if self.menuActivo != 3:                
                print('abri 3')            
                self.menuActivo = 3
                self.menu03() 
            else:
                 self.menuActivo = 0  
        elif boton['text'] == 'CUARTO':
            self.label04.place(x=1,y=301,width=98,height=98)   
            if self.menuActivo != 4:                
                print('abri 4')            
                self.menuActivo = 4
                self.menu04() 
            else:
                 self.menuActivo = 0 
        elif boton['text'] == 'QUINTO':
            self.label05.place(x=1,y=401,width=98,height=98)
            if self.menuActivo != 5:                
                print('abri 5')            
                self.menuActivo = 5
                self.menu05() 
            else:
                 self.menuActivo = 0 
        elif boton['text'] == 'SEXTO':
            self.label06.place(x=1,y=501,width=98,height=98) 
            if self.menuActivo != 6:                
                print('abri 6')            
                self.menuActivo = 6
                self.menu06() 
            else:
                 self.menuActivo = 0 

    def destroyWindow(self):
        if self.menuActivo==1:
            self.frame01.destroy()
        elif self.menuActivo==2:
            self.frame02.destroy()
        elif self.menuActivo==3:
            self.frame03.destroy()
        elif self.menuActivo==4:
            self.frame04.destroy()
        elif self.menuActivo==5:
            self.frame05.destroy()
        elif self.menuActivo==6:
            self.frame06.destroy()
         
    def menu01(self):
        self.frame01 = Frame(self, bg='white')
        self.frame01.place(x= 110, y=10, width=780, height=580)

        self.treeview01 = Treeview(self.frame01, columns=('#1','#2','#3'),show='headings', selectmode='browse', height=26, padding=5)
        self.treeview01.column('#1', width=70, minwidth=70)
        self.treeview01.column('#2', width=280, minwidth=280)
        self.treeview01.column('#3', width=80, minwidth=80)
        self.treeview01.heading('#1', text='DNI')
        self.treeview01.heading('#2', text='APELLIDOS Y NOMBRE')
        self.treeview01.heading('#3', text='NACIMIENTO')
        #Style().theme_use('default')
        Style().configure("Treeview", background="#383838",foreground="white",font=("Trebuchet MS", 10))
        Style().configure("Treeview.Heading",background = "blue",foreground="Black",font=("Trebuchet MS", 9,'bold'))
        
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='08555618',value=('08555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.treeview01.insert('',index=END,text='08555618',value=('08555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))

        self.treeview01.bind('<<TreeviewSelect>>', self.on_tree_item_select)

        self.treeview01.place(x= 10, y= 11)

        self.boton1 = Button(self.frame01, text='Nuevo', cursor='hand2', relief='raised', bd=1, command= self.menu01Registrar)
        self.boton1.place(x=470, y=540)

    def menu01Registrar(self):
        
        self.frame02 = Frame(self.frame01, bg='yellow')
        self.frame02.place(x= 10, y=10, width=760, height=560)
        
        label01 = Label(self.frame02,   text    ='DNI',                                 
                                bg      ='#393834', 
                                fg      ='#72B4F3',                                                                
                                width   =18,                                
                                anchor  ='w', 
                                font    =("Trebuchet MS", 10,'bold'))
        label01.grid(row =0, column =0, padx =10, pady =1)

        self.textbox01 = Entry(self.frame02, bg      ='#393834', 
                                fg      ='#3DC43F',
                                width   =16,
                                relief  ='flat',                                
                                selectbackground    ='#E9D412', 
                                selectforeground    ='#0E0E0E',                                 
                                insertbackground    ='#898879',                                                       
                                font    =('Trebuchet MS', 11,'bold')) 
        self.textbox01.grid(row =0, column =1, padx =10, pady =1)
        boton1 = Button(self.frame02, text='Grabar', command= self.menu01RegistrarTrabajador)        
        boton1.grid(row=6, column=0)
        boton2 = Button(self.frame02, text='MODIFICAR', command= self.menu01ModificarTrabajador)        
        boton2.grid(row=6, column=1)

    def menu01RegistrarTrabajador(self):
        self.treeview01.insert('',index=END,text='48555618',value=('48555618','OROPEZA INCA JEANCARLOS ALBERTO','28/12/1989'))
        self.frame02.destroy()

    def menu01ModificarTrabajador(self):
        selected_item = self.treeview01.selection()[0] 
        self.treeview01.item(selected_item, text='91988927',value=('91988927','OROPEZA GARCIA BRIANNA ALESSIA','26/08/2020'))
        self.frame02.destroy()


    def menu02(self):
        self.frame02 = Frame(self, bg='green')
        self.frame02.place(x= 110, y=10, width=780, height=580)
    
    def menu03(self):
        self.frame03 = Frame(self, bg='yellow')
        self.frame03.place(x= 110, y=10, width=780, height=580)
    
    def menu04(self):
        self.frame04 = Frame(self, bg='pink')
        self.frame04.place(x= 110, y=10, width=780, height=580)
    
    def menu05(self):
        self.frame05 = Frame(self, bg='blue')
        self.frame05.place(x= 110, y=10, width=780, height=580)
    
    def menu06(self):
        self.frame06 = Frame(self, bg='red')
        self.frame06.place(x= 110, y=10, width=780, height=580)

    def delete(self):
        selected_item = self.treeview01.selection()[0] ## get selected item
        print(selected_item)
        self.treeview01.delete(selected_item)

    def edit(self):   
        selected_item = self.treeview01.selection()[0]         
        self.treeview01.item(selected_item, text='48555618', values=('foo', 'bar','lala'))

    def on_tree_item_select(self, e):
        curItem = self.treeview01.focus()
        #print(self.treeview01.item(curItem))
        print (str(self.treeview01.item(curItem).get('text')))

   

      
if __name__ == '__main__':
    aplicacion = App()
