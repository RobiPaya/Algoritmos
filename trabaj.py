#candado
from tkinter import *
ventana=Tk()
ventana.title('ola')
ventana.minsize(width=300,height=200)
import random
import string
import pyperclip
from tkinter import messagebox

RAND=[] #es para la contraseña aleatoria

def generr(): #y simbolos
    passwor.delete(first=0, last=20)    
    hola=list(string.ascii_lowercase)
    HOLA=list(string.ascii_uppercase)
    sim= ['!', '#', '$', '%', '&', (', '), '*', '+']
    for x in range(2):
        a=random.randint(0,10)
        b=random.choice(hola)
        c=random.choice(sim)
        d=random.choice(HOLA)
        RAND.append(a)
        RAND.append(b)
        RAND.append(c)
        RAND.append(d)
        RAND.append(b)
    random.shuffle(RAND)
    passwor.insert(END, string=RAND)
    pyperclip.copy(RAND)
    RAND.clear()

imag=PhotoImage(file='ole.png')
fondo=Label(image=imag).grid(column=2,row=0)



ola=Entry()
ola.grid(column=1,row=1, columnspan=2)

hi=Label(text='website :')
hi.grid(column=0,row=1)

emai=Entry()
emai.grid(column=1,row=2, columnspan=2)

em=Label(text='email:')
em.grid(column=0,row=2)

passwor=Entry()
passwor.grid(column=1,row=3, columnspan=2)

pas=Label(text='password:')
pas.grid(column=0,row=3)

generar= Button(text='Generar', command=generr)
generar.grid(column=3,row=3,columnspan=2)

def guardar():
    sitioweb=ola.get()
    email=emai.get()
    password=(passwor.get()) 
    messagebox.showinfo(title='hola', message='vas a guardar???  \U0001f628')
    if sitioweb=='' or email=='' or password=='':
        messagebox.showinfo(title='hola', message='pero pues pon algo no?  \U0001f628')
        quit()
    
    else:
        ok = messagebox.askokcancel(title='???', message='¿Quieres guardar esta información?')

        if ok :


            messagebox.showinfo(title='datos', message=f'{sitioweb[:]} | {email[:]} | {password[:]}')

            with open("datos.txt", "a") as archivo:
             archivo.write(f'{str(sitioweb)[1:-1]} | {str(email)[1:-1]} | {str(password)[1:-1]}\n')
        
try:
    f=open('datos.txt')
    try:
        f.write('un nuevo dato')
    except:
        print('hubo un error al intentar guardar la información')
    finally:
        f.close()
except:
    print('error al abrir el archivo')



guardar= Button(text='Guardar', command=guardar)
guardar.grid(column=4,row=5,columnspan=2)

rempl=Label(text='usuarios: ')




ventana.mainloop()