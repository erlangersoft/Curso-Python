import tkinter

ventana = tkinter.Tk()
ventana.title("Mi Primer Programa")
ventana.geometry("800x600")

etiqueta = tkinter.Label(ventana, text="Hola Mundo", bg="blue")
#etiqueta.pack()
#etiqueta.pack(side=tkinter.BOTTOM)
#etiqueta.pack(fill = tkinter.X)
#etiqueta.pack(fill = tkinter.Y, expand=True)
etiqueta.pack(fill = tkinter.BOTH, expand=True)


ventana.mainloop()
