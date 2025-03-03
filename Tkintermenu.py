import tkinter as tk
import RealtimeFirebase as rtf
from tkinter import ttk
import PygameJuego as Pgame


psp14 = ("Press Start 2P", 14)
psp12 = ("Press Start 2P", 12)
psp10 = ("Press Start 2P", 10)
psp8 = ("Press Start 2P", 8)
psp6 = ("Press Start 2P", 6)

# Definir la venta principal
menu = tk.Tk()
menu.title("TetrisPy")
menu.call('tk', 'scaling', 1.5)
menu.geometry("600x500")
menu.config(bg="#0f0f0f")
title = tk.Label(menu, text="", font=("Press Start 2P", 26), fg="green", bg="#0f0f0f")
title_game = tk.Label(menu, text="TETRIS PY", font=("Press Start 2P", 26), fg="green", bg="#0f0f0f")
title.pack(pady=5)
title_game.pack(pady=5)

def pack_widget(x):
    x.pack(pady=5)
    for i in x.winfo_children():
        i.pack(pady=5)

def sign_in():
    menu_start.pack_forget()
    
    sign_in_frame.pack(pady=5)
    sign_user_lbl.pack(pady=5)
    sign_user_entry.pack(pady=5)
    sign_user_error_lbl.pack(pady=5)
    sign_email_lbl.pack(pady=5)
    sign_email_entry.pack(pady=5)
    sign_email_error_lbl.pack(pady=5)
    sign_password_lbl.pack(pady=5)
    sign_password_entry.pack(pady=5)
    sign_confirm_btn.pack(pady=10)
    return_btn_sign.pack(pady=5)
    
    sign_email_error_lbl.pack_forget()
    sign_user_error_lbl.pack_forget()
    
def log_in():
    menu_start.pack_forget()
    login_frame.pack(pady=5)
    pack_widget(login_frame)
    login_error_lbl.pack_forget()
    
def return_btn(x,y):
    x.pack_forget()
    for i in x.winfo_children():
        i.pack_forget()
    pack_widget(y)

def mg_menu(x):
    x.pack_forget()
    for f in x.winfo_children():
        f.pack_forget()
    pack_widget(mj_frame)

# Función Sign in
def sigin_comfirm():
    usuario = sign_user_entry.get()
    email = sign_email_entry.get()
    password = sign_password_entry.get()
    if (rtf.signuser(usuario, email, password) == usuario):
        mg_menu(sign_in_frame)
        print("Usuario registrado correctamente", rtf.signuser(usuario, email, password))
    else:
        sign_email_error_lbl.pack_forget()
        sign_user_error_lbl.pack_forget()
        if (rtf.signuser(usuario, email, password) == 3):
            sign_user_error_lbl.pack(before=sign_email_lbl, pady=3)
            sign_email_error_lbl.pack(before=sign_password_lbl, pady=3)
            print("Usuario y correo ya existen", rtf.signuser(usuario, email, password))
        if (rtf.signuser(usuario, email, password) == 1):
            sign_user_error_lbl.pack(before=sign_email_lbl, pady=3)
            print("Usuario ya existe", rtf.signuser(usuario, email, password))
        if (rtf.signuser(usuario, email, password) == 2):
            sign_email_error_lbl.pack(before=sign_password_lbl, pady=3)
            print("Correo ya existe", rtf.signuser(usuario, email, password))        
    

sign_in_frame = tk.Frame(menu, bg="#0f0f0f")

sign_user_lbl = tk.Label(sign_in_frame, text="Nombre Usuario", font=psp10, fg="white", bg="#0f0f0f")

sign_user_entry = tk.Entry(sign_in_frame, bg="#0f0f0f", fg="white")

sign_user_error_lbl = tk.Label(sign_in_frame, text="El nombre de usuario ya existe", font=psp6, fg="red")
sign_email_lbl = tk.Label(sign_in_frame, text="Correo Electrónico", font=psp10, fg="white", bg="#0f0f0f")

sign_email_entry = tk.Entry(sign_in_frame, bg="#0f0f0f", fg="white")

sign_email_error_lbl = tk.Label(sign_in_frame, text="El correo electrónico ya existe", font=psp6, fg="red")
sign_password_lbl = tk.Label(sign_in_frame, text="Contraseña", font=psp10, fg="white", bg="#0f0f0f")

sign_password_entry = tk.Entry(sign_in_frame, bg="#0f0f0f", fg="white")

sign_confirm_btn = tk.Button(sign_in_frame, text="Registrar", font=psp10, command=sigin_comfirm, fg="white", bg="#0f0f0f")
return_btn_sign = tk.Button(sign_in_frame, text="Regresar", font=psp10, command=lambda:return_btn(sign_in_frame, menu_start), fg="white", bg="#0f0f0f")   

# Función login and return
def login_comfirm():
    usuario = login_user_entry.get()
    password = login_password_entry.get()
    if (rtf.loginuser(usuario, password) == 1):
        mg_menu(login_frame)
        print("Usuario logeado correctamente", rtf.loginuser(usuario, password))
    else:
        login_error_lbl.pack_forget()
        login_error_lbl.pack(before=login_confirm_btn, pady=3)
        print("Usuario y contraseña incorrectos", rtf.loginuser(usuario, password))
        
login_frame = tk.Frame(menu, bg="#0f0f0f")

login_user_lbl = tk.Label(login_frame, text="Usuario", font=psp10, fg="white", bg="#0f0f0f")

login_user_entry = tk.Entry(login_frame, bg="#0f0f0f", fg="white")

login_password_lbl = tk.Label(login_frame, text="Contraseña", font=psp10, fg="white", bg="#0f0f0f")

login_password_entry = tk.Entry(login_frame, bg="#0f0f0f", fg="white")

login_confirm_btn = tk.Button(login_frame, text="Ingresar", font=psp10, command=login_comfirm, fg="white", bg="#0f0f0f")
login_error_lbl = tk.Label(login_frame, text="El nombre de usuario o la contraseña \n es incorrecta o no existe", font=psp6, fg="red")
return_btn_login = tk.Button(login_frame, text="Regresar", font=psp10, command=lambda:return_btn(login_frame, menu_start), fg="white", bg="#0f0f0f")

# Función menu inicio
menu_start = tk.Frame(menu, bg="#0f0f0f")

sign_in_btn = tk.Button(menu_start, text="Crear cuenta", font=psp14, command=sign_in, fg="white", bg="#0f0f0f")

log_in_btn = tk.Button(menu_start, text="Ingresar", font=psp14, command=log_in, fg="white", bg="#0f0f0f")

exit_btn = tk.Button(menu_start, text="Salir", font=psp14, command=menu.quit, fg="white", bg="#0f0f0f")

pack_widget(menu_start)

def opciones():
    mj_frame.pack_forget()
    options_frame.pack(pady=5)
    pack_widget(options_frame)

def play():
    mj_frame.pack_forget()
    play_frame.pack(pady=5)
    pack_widget(play_frame)

mj_frame = tk.Frame(menu, bg="#0f0f0f")

mj_play_btn = tk.Button(mj_frame, text="Jugar", font=psp14, fg="white", bg="#0f0f0f",command=play)
mj_stats_btn = tk.Button(mj_frame, text="Estadísticas", font=psp14, fg="white", bg="#0f0f0f")

mj_top_5_btn = tk.Button(mj_frame, text="Top 5", font=psp14, fg="white", bg="#0f0f0f")

mj_options_btn = tk.Button(mj_frame, text="Opciones", font=psp14, command=opciones, fg="white", bg="#0f0f0f")

mj_return_btn = tk.Button(mj_frame, text="Salir", font=psp14, command=lambda:return_btn(mj_frame, menu_start), fg="white", bg="#0f0f0f")

play_frame = tk.Frame(menu,bg="#0f0f0f")
play_text = tk.Label(play_frame, text="Tetris Py es un juego educativo en dónde \ndebes crear líneas de código de Python para \nganar puntaje y superar niveles.\n\n En el tablero irán cayendo partes de una línea de \ncódigo y deberás colocarla en el órden correcto.", font=psp8,fg="white",bg="#0f0f0f") 
play_text_preparado = tk.Label(play_frame, text="¿Estás preparado para iniciar...?", font=psp12,fg="green", bg="#0f0f0f")
play_btt = tk.Button(play_frame, text="¡Jugar!", font=psp14, fg="white", bg="#0f0f0f",command=lambda:(return_btn(play_frame,mj_frame),Pgame.maingame()))
return_btn_play = tk.Button(play_frame, text="Regresar", font=psp10,fg="white", bg="#0f0f0f", command=lambda:return_btn(play_frame,mj_frame))


def mostrar_campos_mod():
    mod_cuenta_frame.pack(pady=5)
    mod_emailoruser_lbl.pack(pady=5)
    mod_emailoruser_etr.pack(pady=5)
    mod_passlogin_lbl.pack(pady=5)
    mod_passlogin_etr.pack(pady=5)
    mod_return_btn.pack(pady=5)

def mostrar_botones_mod():
    options_frame.pack_forget()
    mod_cuenta_frame.pack(pady=5)
    mod_user_btt.pack(pady=5)
    mod_email_btt.pack(pady=5)
    mod_password_btt.pack(pady=5)
    mod_return_btn.pack(pady=5)
    
def ocultar_botones_mod():
    mod_user_btt.pack_forget()
    mod_email_btt.pack_forget()
    mod_password_btt.pack_forget()
    mod_return_btn.pack_forget()
    
def ocultar_campos_mod():
    mod_emailoruser_lbl.pack_forget()
    mod_emailoruser_etr.pack_forget()
    mod_passlogin_lbl.pack_forget()
    mod_passlogin_etr.pack_forget()
    
def eliminar_cuenta():
    options_frame.pack_forget()
    del_cuenta_frame.pack(pady=5)
    pack_widget(del_cuenta_frame)

options_frame = tk.Frame(menu, bg="#0f0f0f")

op_modificar_cuenta = tk.Button(options_frame, text="Modificar Cuenta", font=psp14, command=lambda:(mostrar_botones_mod(), ocultar_campos_mod()), fg="white", bg="#0f0f0f")

op_eliminar_cuenta = tk.Button(options_frame, text="Eliminar Cuenta", font=psp14, command=lambda:eliminar_cuenta(), fg="white", bg="#0f0f0f")  

op_return_btn = tk.Button(options_frame, text="Regresar", font=psp14, command=lambda:return_btn(options_frame, mj_frame), fg="white", bg="#0f0f0f")


def mod_username():
    useroremail = mod_emailoruser_etr.get()
    password = mod_passlogin_etr.get()
    return_rtf_mod=rtf.comprobaciónmod(useroremail,password)
    print(return_rtf_mod)
    if return_rtf_mod[0] == True:
        def newuser_mostrar():
            mod_user_lbl.pack_forget()
            mod_return_btn.pack_forget()
            mod_comfirm_btn.pack_forget()
            newuser_lbl.pack(pady=5)
            newuser_etr.pack(pady=5)
            newuser_btt.pack(pady=5)
        def newuser_ocultar():
            newuser_btt.pack_forget()
            newuser_lbl.pack_forget()
            newuser_etr.pack_forget()
        def usermodify():
            succes = rtf.modifyuser(return_rtf_mod[0],return_rtf_mod[1],newuser_etr.get())
            print(succes)
            if succes == 1:
                global newuser_error_lbl
                newuser_error_lbl = tk.Label(mod_cuenta_frame, text="Usuario ya existe", font=psp6, fg="red")
                newuser_error_lbl.pack(before=newuser_btt, pady=5) 
            elif succes == 2:
                newuser_ocultar()
                newuser_error_lbl.pack_forget()
                user_succes_lbl = tk.Label(mod_cuenta_frame, text="Usuario modificado correctamente", font=psp14)
                user_succes_lbl.pack(pady=5)
                comfirm_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame))
                comfirm_return_btn.pack(pady=5)

        ocultar_campos_mod()
        global newuser_lbl, newuser_etr, newuser_btt
        newuser_lbl = tk.Label(mod_cuenta_frame, text="Ingrese un Nombre de usuario nuevo", font=psp10)
        newuser_etr = tk.Entry(mod_cuenta_frame, bg="#0f0f0f", fg="white")
        newuser_btt = tk.Button(mod_cuenta_frame, text="Confirmar", font=psp14, command=usermodify, fg="white", bg="#0f0f0f")
        newuser_mostrar()             
    else:
        ocultar_campos_mod()
        mod_user_lbl.pack_forget()
        mod_comfirm_btn.pack_forget()
        mod_return_btn.pack_forget()
        user_error_lbl = tk.Label(mod_cuenta_frame, text="Datos incorrectos", font=psp14)
        user_error_lbl.pack(pady=5)
        comfirm_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame))
        comfirm_return_btn.pack(pady=5)
def modificar_dato(x):
    if x == "Usuario":
        ocultar_botones_mod()
        global mod_user_lbl, mod_return_btn, mod_comfirm_btn
        mod_user_lbl = tk.Label(mod_cuenta_frame, text="Modificación de usuario", font=psp14, fg="white")
        mod_user_lbl.pack(pady=5)
        mostrar_campos_mod()
        mod_return_btn.pack_forget()
        mod_comfirm_btn = tk.Button(mod_cuenta_frame, text="Confirmar", font=psp14, command=lambda:mod_username(), fg="white", bg="#0f0f0f")
        mod_comfirm_btn.pack(pady=5)
        mod_return_btn.pack(pady=5)
        
    if x == "Correo":
        mod_email_lbl = tk.Label(mod_cuenta_frame, text="Modificación de correo", font=psp14, fg="white")
        mod_email_lbl.pack(pady=5)
        mostrar_campos_mod()
    if x == "Contraseña":   
        mod_password_lbl = tk.Label(mod_cuenta_frame, text="Modificación de contraseña", font=psp14, fg="white")
        mod_password_lbl.pack(pady=5)
        mostrar_campos_mod()
    
mod_cuenta_frame = tk.Frame(menu, bg="#0f0f0f")

mod_user_btt = tk.Button(mod_cuenta_frame, text="Modificar Usuario", font=psp14, command=lambda:modificar_dato("Usuario"), fg="white", bg="#0f0f0f")

mod_email_btt = tk.Button(mod_cuenta_frame, text="Modificar Correo", font=psp14, command=lambda:modificar_dato("Correo"), fg="white", bg="#0f0f0f")

mod_password_btt = tk.Button(mod_cuenta_frame, text="Modificar Contraseña", font=psp14, command=lambda:modificar_dato("Contraseña"), fg="white", bg="#0f0f0f")

mod_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame), fg="white", bg="#0f0f0f")

mod_emailoruser_lbl = tk.Label(mod_cuenta_frame, text="Ingrese Correo Electrónico o Usuario", font=psp10, fg="white")
mod_emailoruser_etr = tk.Entry(mod_cuenta_frame, bg="#0f0f0f", fg="white")

mod_passlogin_lbl = tk.Label(mod_cuenta_frame, text="Ingrese Contraseña", font=psp10, fg="white")
mod_passlogin_etr = tk.Entry(mod_cuenta_frame, bg="#0f0f0f", fg="white")

return_btn_mod = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:ocultar_campos_mod(), fg="white", bg="#0f0f0f")

del_cuenta_frame = tk.Frame(menu, bg="#0f0f0f")

del_user_btt = tk.Button(del_cuenta_frame, text="Eliminar Usuario", font=psp14, fg="white", bg="#0f0f0f")

del_return_btn = tk.Button(del_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(del_cuenta_frame, options_frame), fg="white", bg="#0f0f0f")

menu.mainloop()
