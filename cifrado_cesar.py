# ******************Cifrado por desplazamiento o Código Cesar******************
# Interfaz gráfica con tkinter para codigo cesar
# Utiliza un alfabeto para tener un indice de caracteres 
# Y un número que identifica la cantidad de desplazamientos para el cifrado


# Importación de librerias
import tkinter as tk            # Libreria para interfaz grafica con python
from tkinter import *           # Libreria para utilizar frames
from tkinter import messagebox  # Libreria para utilizar cuadros de dialogo
from PIL import Image, ImageTk  # Libreria para llamar imagenes

#Configuración de ventana de interfaz gráfica
window = tk.Tk()                    # Inicialización de la ventana que contendra la interfaz grafica
window.title("Cifrado César")  # Titulo de la ventana
canvas = tk.Canvas(window, width=450, height=500)  # define el tamaño de ventana 
canvas.pack()
frame = tk.Frame(window, bg="light sea green")# Creación del marco que contendra todos los bloques  
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

# Inicialización de variables
entry_var = tk.StringVar(window)    # Variable para almacenar el valor del texto de entrada 1 correspondiente al texto a encriptar
entry2_var = tk.StringVar(window)   # Variable para almacenar el valor del texto de entrada 2 correspondiente a la clave para encriptar
lbl5_var = tk.StringVar(window)     # Variable para presentar el texto 5 correspondiente al texto encriptado
lbl7_var = tk.StringVar(window)     # Variable para presentar el texto 7 correspondiente al texto desencriptado

# Inicialización de alfabeto y logitud de alfabeto 
alfabeto=' 0123456789.,:;@#$&%*+-^<>áéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
longitud=len(alfabeto)# Se obtiene la longitud del vector alfabeto

                   
# Función para detectar ingreso de valores numericos en el texto de entrada 2 para la clave
def testVal(inStr,acttyp):
    if acttyp == '1': # Detecta un valor insertado en el cajon de texto
        if not inStr.isdigit():
            messagebox.showinfo("AVISO", "SOLO INGRESE VALORES NUMÉRICOS") #Aviso si el usuario no ingresa un número
            return False # No permite ingresar ese valor no númerico            
    return True

# Función para encriptar
def cypher():
    mensaje=(entry_var.get())# Se obtiene el mensaje ingresado por el usuario
    if len(mensaje) == 0: # Condición para determinar si el usuario ingreso un mensaje
        messagebox.showwarning("ADVERTENCIA", "INGRESE EL TEXTO A ENCRIPTAR ANTES DE EJECUTAR")
    key=(entry2_var.get())# Condición para determinar si el usuario ingreso la clave de desplazamiento
    if len(key) == 0:
        messagebox.showwarning("ADVERTENCIA", "INGRESE EL NÚMERO DE DESPLAZAMIENTO ANTES DE EJECUTAR")
    clave=int(key)# Se convierte el string de la clave en un entero para las futuras operaciones matématicas
    # Se ordena el alfabeto de caracteres en un vector
    print('Este es su mensaje original:'+ ' ' + mensaje)# Se imprime para el usuario el mensaje ingresado
    cript=''# Se inicializa el vector cypher que almacenará los caracteres cifrados

    for i in mensaje:# Secuencia de iteración For para realizar el cifrado por desplazamiento
        pos=alfabeto.find(i)# Encontrar la posición de los caracteres del mensaje dentro del vector alfabeto 
        new_pos=(pos+clave)%longitud# Recorre la posición de acuerdo al numero de clave dentro del alfabeto
        cript+=alfabeto[new_pos]# Guarda los caracteres cifrados dentro del vector cypher

    print('Este es su mensaje encriptado: '+' '+cript)# Presentación del mensaje encriptado 
    lbl5_var.set(cript)# Se imprime el mensaje encriptado el el cajon de texto 5

# Función para desencriptar
def non_cypher():
    encriptado=(lbl5_var.get())# se obtiene el mensaje encriptado del cajon de texto 5
    if len(encriptado) == 0:# Condición para determinar si hay un texto encriptado
        messagebox.showerror("ERROR", "NO EJECUTE DESENCRIPTAR SIN PREVIAMENTE HABER OBTENIDO UN TEXTO ENCRIPTADO")
    key=(entry2_var.get())# se obtiene el numero de desplazmiento del cajon de entrada 2
    clave=int(key)# Se convierte el string de la clave en un entero para las futuras operaciones matématicas
    no_cript=''# Se inicializa el vector non cypher que almacenará los caracteres desencriptados
    for i in encriptado:# Secuencia de iteración For para realizar el descifrado por desplazamiento
        pos2=alfabeto.find(i) # Encuentra la posición de los caracteres del mensaje cifrado dentro del vector alfabeto
        new_pos2=(pos2-clave)%longitud# Recorre la posición de acuerdo al numero de clave dentro del alfabeto 
        no_cript+=alfabeto[new_pos2]# Guarda los caracteres descifrados en el vector non cypher
    print('Este es su mensaje desencriptado: '+' '+no_cript)# Presentación del mensaje desencriptado
    lbl7_var.set(no_cript)# Se imprime el mensaje desencriptado el el cajon de texto 7

# Función para limpiar las entradas y salidas de variables
def borrar():
    entry.delete(0, 'end')  #borrar cajon de entrada 1
    entry2.delete(0, 'end') #borrar cajon de entrada 2
    lbl5_var.set("")        #borrar cajon de texto 5
    lbl7_var.set("")        #borrar cajon de texto 7
    
# Creación de etiquetas para presentación del programa
lbl = Label(window, text="Simulación de Código César",  font=("Arial Bold", 18), bg="light sea green", fg="white")
lbl.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)# pos y tam de etiqueta 1
lbl_a = Label(window, text="UNIVERSIDAD NACIONAL DE LOJA",  font=("Arial", 10), bg="light sea green", fg="white")
lbl_a.place(relx=0.15, rely=0.13, relwidth=0.7, relheight=0.05)# pos y tam de etiqueta 1.1
lbl_b = Label(window, text="ELECTRÓNICA Y TELECOMUNICACIONES",  font=("Arial", 10), bg="light sea green", fg="white")
lbl_b.place(relx=0.15, rely=0.17, relwidth=0.7, relheight=0.05)# pos y tam de etiqueta 1.2

# Creación de etiqueta y entrada para mensaje ingresado por usuario
lbl2 = Label(window, text="Ingrese el texto a encriptar:", font=("Arial Bold", 11),bg="light sea green", fg="white")
lbl2.place(relx=0.1, rely=0.22, relwidth=0.4, relheight=0.05)# pos y tam de etiqueta 2
entry = tk.Entry(window,textvariable=entry_var,bg="azure3")
entry.place(relx=0.1, rely=0.27, relwidth=0.8, relheight=0.05)# pos y tam de cajon de entrada 1

# Creación de etiqueta y entrada para clave ingresada por usuario
lbl3 = Label(window, text="Ingrese el número clave de desplazamiento:", font=("Arial Bold", 11),bg="light sea green", fg="white")
lbl3.place(relx=0.1, rely=0.33, relwidth=0.64, relheight=0.05)# pos y tam de etiqueta 3
entry2 = tk.Entry(window, validate="key", textvariable=entry2_var,bg="azure3")
entry2['validatecommand'] = (entry.register(testVal),'%P','%d')# validación de cajon de entrada 2 para detectar numeros
entry2.place(relx=0.75, rely=0.33, relwidth=0.15, relheight=0.05)# pos y tam de cajon de entrada 2

# Creación de botones 
boton = tk.Button(text="ENCRIPTAR",command=cypher, font=("Verdana", 12),width= 12,bg="medium sea green",fg="white")
boton.place(relx=0.1, rely=0.4, relwidth=0.25, relheight=0.05)# pos y tam de boton 1
boton2 = tk.Button(text="DESENCRIPTAR",command=non_cypher, font=("Verdana", 12),width= 14,bg="medium sea green",fg="white")
boton2.place(relx=0.37, rely=0.4, relwidth=0.31, relheight=0.05)# pos y tam de boton 2
boton3 = tk.Button(text="LIMPIAR",command=borrar, font=("Verdana", 12),width= 10,bg="medium sea green",fg="white")
boton3.place(relx=0.70, rely=0.4, relwidth=0.2, relheight=0.05)# pos y tam de boton 3

# Creación de etiquetas para mostrar mensaje encriptado
lbl4 = Label(window, text="TEXTO ENCRIPTADO",  font=("Arial Bold", 14),bg="light sea green", fg="white")
lbl4.place(relx=0.25, rely=0.47, relwidth=0.5, relheight=0.05)# pos y tam de etiqueta 4
lbl5 = Label(window, textvariable=lbl5_var, font=("Verdana Bold", 12),bg="LemonChiffon2")
lbl5.place(relx=0.1, rely=0.53, relwidth=0.8, relheight=0.05)# pos y tam de etiqueta 5

# Creación de etiquetas para mostrar mensaje desencriptado
lbl6 = Label(window, text="TEXTO DESENCRIPTADO", font=("Arial Bold", 14),bg="light sea green", fg="white")
lbl6.place(relx=0.2, rely=0.60, relwidth=0.6, relheight=0.05)# pos y tam de etiqueta 6
lbl7 = Label(window, textvariable=lbl7_var, font=("Verdana Bold", 12),bg="LemonChiffon2")
lbl7.place(relx=0.1, rely=0.66, relwidth=0.8, relheight=0.05)# pos y tam de etiqueta 7

# Creación de etiquetas para mostrar imagen de la universidad
image = Image.open('unl.png')
tk_image = ImageTk.PhotoImage(image)
lbl8 = tk.Label(window, image=tk_image,bg="light sea green", compound='center')
lbl8.place(relx=0.1, rely=0.73, relwidth=0.8, relheight=0.2)# pos y tam de etiqueta 8 para img

#Finalización de la ventana
window.mainloop()
