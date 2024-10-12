import tkinter as tk 

def convertir():
    try:
        #obtiene el valor ingresado en el campo de entrada
        kilometros = float(entrada_kilometros.get())
    
    
        #realiza la conversion a millas (1km = 0.621371 millas )
        millas= kilometros* 0.621371
        
        #actualiza la etiqueta de resultado
        etiqueta_resultado.config(text=f"{kilometros} kilómetros son {millas} millas")
    except ValueError:
        #manejo de errores para entradas no validas
        etiqueta_resultado.config(text="Ingrese un valor numerico valido")
#crear la ventana principal
ventana= tk.Tk()
ventana.title("conversor de kilometros a millas")
ventana.geometry("300x150") #establece el tamaño de la ventana

#crear etiqueta de instruccion y colocarla en la cuadricula 
etiqueta_instruccion = tk.Label(ventana, text="ingrese la distancia en kilometros:")
etiqueta_instruccion.grid(row=0, column =0, columnspan=2, padx=10, pady=10)

#crear campo de entrada y colocarlo en la cuadricula 
entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10,pady=10)

#crear boton de conversion y colocarlo en la cuadricula
boton_convertir= tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(row=1, column=1, padx=10, pady=10)

#crear etiqueta de resultado y colocarla en la cuadricula
etiqueta_resultado = tk.Label(ventana,text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10,pady=10)

#iniciar la aplicacion 
ventana.mainloop()
    