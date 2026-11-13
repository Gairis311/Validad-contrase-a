import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")


# === FUNCTIONS ===

# 1. Capturar las credenciales
def get_user_password():
    Usuario_ingresado = entry_usuario.get()
    password_ingresado = entry_password.get()

    validate_credentials(Usuario_ingresado, password_ingresado)


# 2. Validar las credenciales
def validate_credentials(usuario_ingresado, password_ingresado):

    if usuario_ingresado == APP_USER and password_ingresado == APP_PASSWORD:
        show_message("Acceso correcto", "green")
    else:
        show_message("Usuario o contraseña incorrectos", "red")


# 3. Mostrar el mensaje
def show_message(mensaje, color):
    label_resultado.config(text=mensaje, fg=color)


# === TKINTER ===

ventana = tk.Tk()
ventana.title("Validar contraseñas")
ventana.geometry("300x300")


# == Usuario ==

label_usuario= tk.Label(ventana, text="Ingrese su Usuario")
label_usuario.pack()

entry_usuario = tk.Entry(ventana)
entry_usuario.pack()


# == Password ==

label_password = tk.Label(ventana, text="Ingrese su contraseña")
label_password.pack()

entry_password = tk.Entry(ventana, show="*")
entry_password.pack()


# == Botón ==

button = tk.Button(ventana, text="Ingresar", command=get_user_password)
button.pack()


# == Mensaje ==

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()


ventana.mainloop()
