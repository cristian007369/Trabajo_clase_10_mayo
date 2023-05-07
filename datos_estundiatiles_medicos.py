from tkinter import *
from tkinter import ttk

# funciones de la app
def ingresar_datos_academicos():
    global toplevel_academico, calculo, algebra, fund
    calculo=IntVar()
    algebra=IntVar()
    fund=IntVar()
    toplevel_academico = Toplevel()
    toplevel_academico.title("Ingrese datos academicos")
    toplevel_academico.resizable(False, False)
    toplevel_academico.geometry("400x270")
    toplevel_academico.config(bg="white")

    # logo de estudiante y universidad
    lb_logo = Label(toplevel_academico, image=estudiante, bg="white")
    lb_logo.place(x=10,y=10)

    lb_uis = Label(toplevel_academico, image=uis, bg="white")
    lb_uis.place(x=240,y=110)

    # etiquetas
    lb_nomcod = Label(toplevel_academico, text = f"Nombre: {nombre.get()}\nCódigo: {codigo.get()}")
    lb_nomcod.config(bg="white", fg="blue", font=("times new roman", 18))
    lb_nomcod.place(x=120, y=10)

    lb_calf = Label(toplevel_academico, text = "Cálculo: \nÁlgebra: \nFund Prog: ")
    lb_calf.config(bg="white", fg="blue", font=("times new roman", 18))
    lb_calf.place(x=10, y=120)

    entry_calculo = Entry(toplevel_academico, textvariable=calculo)
    entry_calculo.config(bg="white", fg="blue", font=("Times New Roman", 19), width=5)
    entry_calculo.focus_set()
    entry_calculo.place(x=130,y=120)

    entry_algebra = Entry(toplevel_academico, textvariable=algebra)
    entry_algebra.config(bg="white", fg="blue", font=("Times New Roman", 19), width=5)
    entry_algebra.place(x=130,y=150)

    entry_fund = Entry(toplevel_academico, textvariable=fund)
    entry_fund.config(bg="white", fg="blue", font=("Times New Roman", 19), width=5)
    entry_fund.place(x=130,y=175)

   # boton para aceptar
    bt_aceptar = Button(toplevel_academico,text="Aceptar", command= aceptar)
    bt_aceptar.place(x=150, y=230, width=100, height=30)
    
def ingresar_datos_medicos():
    global toplevel_medicos, peso, altura, dep, ans, est
    dep= IntVar()
    ans= IntVar()
    est= IntVar()
    peso=IntVar()
    altura=IntVar()
    mf= StringVar()
    toplevel_medicos = Toplevel()
    toplevel_medicos.title("Medicos")
    toplevel_medicos.resizable(False, False)
    toplevel_medicos.geometry("400x320")
    toplevel_medicos.config(bg="white")

    # logo de medicina
    lb_logo = Label(toplevel_medicos, image=medicina, bg="white")
    lb_logo.place(x=10,y=10)

    # etiquetas
    lb_nomcod = Label(toplevel_medicos, text = f"Nombre: {nombre.get()}\nCódigo: {codigo.get()}")
    lb_nomcod.config(bg="white", fg="blue", font=("times new roman", 18))
    lb_nomcod.place(x=120, y=10)

    lb_peal = Label(toplevel_medicos, text = "Peso(Kg): \nAltura(cm): ")
    lb_peal.config(bg="white", fg="blue", font=("times new roman", 18))
    lb_peal.place(x=10, y=120)

    lb_peal = Label(toplevel_medicos, text = "Salud mental")
    lb_peal.config(bg="white", fg="blue", font=("times new roman", 18))
    lb_peal.place(x=140, y=200)

    # entrys
    entry_peso = Entry(toplevel_medicos, textvariable=peso)
    entry_peso.config(bg="white", fg="blue", font=("Times New Roman", 19), width=5)
    entry_peso.focus_set()
    entry_peso.place(x=130,y=120)

    entry_altura = Entry(toplevel_medicos, textvariable=altura)
    entry_altura.config(bg="white", fg="blue", font=("Times New Roman", 19), width=5)
    entry_altura.place(x=130,y=150)

    # radiobutton para hombre o mujer
    rb_k = Radiobutton(toplevel_medicos, text="Masculino", variable=mf, value="Masculino")
    rb_k.config(bg="white", fg="blue", font=("Helvetica", 18))
    rb_k.place(x=230, y=110)

    rb_f = Radiobutton(toplevel_medicos, text="Femenino", variable=mf, value="Femenino")
    rb_f.config(bg="white", fg="blue", font=("Helvetica", 18))
    rb_f.place(x=230, y=140)

    # checkbutthon
    cb_dep = Checkbutton(toplevel_medicos, text="Depresión", variable=dep)
    cb_dep.config(bg="white", fg="blue", font=("times new roman", 15))
    cb_dep.place(x=10, y=240)

    cb_ans = Checkbutton(toplevel_medicos, text="Ansiedad", variable=ans)
    cb_ans.config(bg="white", fg="blue", font=("times new roman", 15))
    cb_ans.place(x=140, y=240)

    cb_est = Checkbutton(toplevel_medicos, text="Estres", variable=est)
    cb_est.config(bg="white", fg="blue", font=("times new roman", 15))
    cb_est.place(x=280, y=240)

   # boton para aceptar
    bt_aceptar = Button(toplevel_medicos,text="Aceptar", command= aceptar1)
    bt_aceptar.place(x=150, y=280, width=100, height=30)

def consultar_estado_academico_medico():
    if cmb_estado.get()=="Estado academico":
        ventana_principal.destroy()
    if cmb_estado.get()=="Estado salud":
        ventana_principal.destroy()
    else:
        t_resultados.insert(INSERT, "Debes selecionar una opción")
def aceptar():
    global promedio
    promedio=round((calculo.get()+algebra.get()+fund.get())/3,1)
    toplevel_academico.destroy()
def aceptar1():
    global imc 
    imc=round(peso.get()/(altura.get()/100)**2,1)
    toplevel_medicos.destroy()

#ventana princpal
ventana_principal = Tk()
ventana_principal.title("Datos médicos y academicos")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="blue")

global estudiante
global medicina
global nombre
global codigo
global uis
A=IntVar()
M=IntVar()
nombre = StringVar()
codigo = StringVar()
estado=["Estado academico","Estado salud"]
estado_selected= StringVar()
uis=PhotoImage(file="img/logo_uis1.png")

# Primer frame.........................................................................................
frame_superior = Frame(ventana_principal)
frame_superior.config(bg="white", width=480, height=100)
frame_superior.place(x=10, y=10)

titulo = Label(frame_superior, text="Estudiante")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 30))
titulo.place(x=150,y=10)

# etiqueta para el nombre y código
lb_nombre = Label(frame_superior, text = "Nombre:")
lb_nombre.config(bg="white", fg="blue", font=("times new roman", 18))
lb_nombre.place(x=10, y=60)

lb_codigo = Label(frame_superior, text = "Código:")
lb_codigo.config(bg="white", fg="blue", font=("times new roman", 18))
lb_codigo.place(x=298, y=60)

# caja de texto para el nombre y el código
entry_nombre = Entry(frame_superior, textvariable=nombre)
entry_nombre.config(bg="white", fg="blue", font=("Times New Roman", 19), width=15)
entry_nombre.focus_set()
entry_nombre.place(x=100,y=60)

entry_codigo = Entry(frame_superior, textvariable=codigo)
entry_codigo.config(bg="white", fg="blue", font=("Times New Roman", 19), width=7)
entry_codigo.place(x=380,y=60)

# Segundo frame..........................................................................................
frame_secundario = Frame(ventana_principal)
frame_secundario.config(bg="white", width=480, height=180)
frame_secundario.place(x=10, y=120)

titulo = Label(frame_secundario, text="Academicos:          Medicos:             Consultar:")
titulo.config(bg = "white",fg="blue", font=("Times new roman", 15))
titulo.place(x=40,y=10)

# Botones academico, medico y consulta 
estudiante= PhotoImage(file="img/estudiante.png")
bt_estudiante = Button(frame_secundario,bg="green",image=estudiante, command=ingresar_datos_academicos)
bt_estudiante.place(x=40, y=50, width=100, height=100)

medicina= PhotoImage(file="img/medicina.png")
bt_medicina = Button(frame_secundario,bg="black",image=medicina, command=ingresar_datos_medicos)
bt_medicina.place(x=180, y=50, width=110, height=100)

# chechbox para estado academico y medico
cmb_estado = ttk.Combobox(frame_secundario, textvariable=estado_selected, values=estado, font=("times new roman", 10))
cmb_estado.place(x=330, y=50)

bt_comsulta = Button(frame_secundario,text="Consultar", command= consultar_estado_academico_medico)
bt_comsulta.place(x=330, y=118, width=100, height=30)

# Tercer frame...................................................................................................
frame_inferior = Frame(ventana_principal)
frame_inferior.config(bg="white", width=480, height=180)
frame_inferior.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_inferior)
t_resultados.config(bg="black", fg="green yellow", font=("times new roman", 20))
t_resultados.place(x=10,y=10,width=460,height=160)

ventana_principal.mainloop()