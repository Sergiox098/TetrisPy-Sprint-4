import tkinter as tk
import RealtimeFirebase as rtf
from tkinter import ttk
import PygameJuego as Pgame
from tkinter import messagebox


psp14 = ("Press Start 2P", 14)
psp12 = ("Press Start 2P", 12)
psp10 = ("Press Start 2P", 10)
psp8 = ("Press Start 2P", 8)
psp6 = ("Press Start 2P", 6)

# Definir la venta principal
menu = tk.Tk()
menu.title("TetrisPy")
menu.call('tk', 'scaling', 1.5)
menu.geometry("800x500")
menu.config(bg="#0f0f0f")
title = tk.Label(menu, text="", font=("Press Start 2P", 26), fg="green", bg="#0f0f0f")
title_game = tk.Label(menu, text="TETRIS PY", font=("Press Start 2P", 26), fg="green", bg="#0f0f0f")
title.pack(pady=5)
title_game.pack(pady=5)

def pack_widget(x):
    x.pack(pady=5)
    for i in x.winfo_children():
        i.pack(pady=5)

def pack_forget_widget(x):
    x.pack_forget()
    for i in x.winfo_children():
        i.pack_forget()

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
        global username
        username = usuario
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
login_error_lbl = tk.Label(login_frame, text="El nombre de usuario o la contraseña \n es incorrecta o no existe", font=psp6, fg="red",bg="#0f0f0f")
return_btn_login = tk.Button(login_frame, text="Regresar", font=psp10, command=lambda:return_btn(login_frame, menu_start), fg="white", bg="#0f0f0f")

# Función menu inicio
menu_start = tk.Frame(menu, bg="#0f0f0f")

sign_in_btn = tk.Button(menu_start, text="Crear cuenta", font=psp14, command=sign_in, fg="white", bg="#0f0f0f")

log_in_btn = tk.Button(menu_start, text="Ingresar", font=psp14, command=log_in, fg="white", bg="#0f0f0f")

exit_btn = tk.Button(menu_start, text="Salir", font=psp14, command=menu.quit, fg="white", bg="#0f0f0f")

pack_widget(menu_start)

def usernamelog():
    if sign_user_entry.get() == "":
        username = login_user_entry.get()
    else:
        username = sign_user_entry.get()
    return username

def play():
    
    mj_frame.pack_forget()
    
    play_frame = tk.Frame(menu,bg="#0f0f0f")
    play_text = tk.Label(play_frame, text="Tetris Py es un juego educativo en dónde \ndebes crear líneas de código de Python para \nganar puntaje y superar niveles.\n\n En el tablero irán cayendo partes de una línea de \ncódigo y deberás colocarla en el órden correcto.", font=psp8,fg="white",bg="#0f0f0f") 
    play_text_preparado = tk.Label(play_frame, text="¿Estás preparado para iniciar...?", font=psp12,fg="green", bg="#0f0f0f")
    play_btt = tk.Button(play_frame, text="¡Jugar!", font=psp14, fg="white", bg="#0f0f0f",command=lambda:(return_btn(play_frame,mj_frame),game()))
    return_btn_play = tk.Button(play_frame, text="Regresar", font=psp10,fg="white", bg="#0f0f0f", command=lambda:return_btn(play_frame,mj_frame))
    
    play_frame.pack(pady=5)
    play_text.pack(pady=5)
    play_text_preparado.pack(pady=5)
    play_btt.pack(pady=5)
    return_btn_play.pack(pady=5)
    
    def game():
        results=Pgame.maingame()
        print(results)
        score = results[0]
        code = results[1]
        level = results[2]
        time = results[3]
        usernameresults = usernamelog()
        rtf.puntaje(usernameresults,score)
        rtf.codigo(usernameresults,code)
        rtf.nivel(usernameresults,level)
        rtf.tiempo(usernameresults,time)

def stats():
    statsuser = usernamelog()
    stats_frame = tk.Frame(menu, bg="#0f0f0f")
    statslist = rtf.getscore(statsuser) or [0, 0, 0, 0]
    statsscore = str(statslist[0])
    statslevel = str(statslist[1])
    statscode = str(statslist[2])
    statstime = str(statslist[3])
    
    mj_frame.pack_forget()
    stats_frame.pack(pady=5)
    
    stats_columnuser_lbl = tk.Label(stats_frame, text="Usuario: ", font=psp10,fg="green",bg="#0f0f0f")
    stats_columnscore_lbl = tk.Label(stats_frame, text="Puntaje máximo: ", font=psp10,fg="green",bg="#0f0f0f")
    stats_columnlevel_lbl = tk.Label(stats_frame, text="Nivel máximo: ", font=psp10,fg="green",bg="#0f0f0f")
    stats_columncode_lbl = tk.Label(stats_frame, text="Códigos realizados: ", font=psp10,fg="green",bg="#0f0f0f")
    stats_columntime_lbl = tk.Label(stats_frame, text="Tiempo de partida: ", font=psp10,fg="green",bg="#0f0f0f")

    stats_columresultsnuser_lbl = tk.Label(stats_frame, text=statsuser, font=psp10,fg="white",bg="#0f0f0f")
    stats_columnresultsscore_lbl = tk.Label(stats_frame, text=statsscore, font=psp10,fg="white",bg="#0f0f0f")
    stats_columnresultslevel_lbl = tk.Label(stats_frame, text=statslevel, font=psp10,fg="white",bg="#0f0f0f")
    stats_columnresultscode_lbl = tk.Label(stats_frame, text=statscode, font=psp10,fg="white",bg="#0f0f0f")
    stats_columnresultstime_lbl = tk.Label(stats_frame, text=(statstime+"s"), font=psp10,fg="white",bg="#0f0f0f")
    return_btn_stats = tk.Button(stats_frame, text="Volver", font=psp14, command=lambda: return_btn(stats_frame,mj_frame))
    
    stats_columnuser_lbl.grid(row=0, column=0, padx=10, pady=10)
    stats_columnscore_lbl.grid(row=1, column=0, padx=10, pady=10)
    stats_columnlevel_lbl.grid(row=2, column=0, padx=10, pady=10)
    stats_columncode_lbl.grid(row=3, column=0, padx=10, pady=10)
    stats_columntime_lbl.grid(row=4, column=0, padx=10, pady=10)
    stats_columresultsnuser_lbl.grid(row=0, column=1, padx=10 , pady=10)
    stats_columnresultsscore_lbl.grid(row=1, column=1, padx=10, pady=10)
    stats_columnresultslevel_lbl.grid(row=2, column=1, padx=10, pady=10)
    stats_columnresultscode_lbl.grid(row=3, column=1, padx=10, pady=10)
    stats_columnresultstime_lbl.grid(row=4, column=1, padx=10, pady=10)
    return_btn_stats.grid(row=5,column=1,padx=10,pady=10)

def top5():
    mj_frame.pack_forget()
    top_frame = tk.Frame(menu, bg="#0f0f0f")
    top_frame.pack(pady=5)
    
    list_top = rtf.topleaderboard()
    print(list_top)
    
    while len(list_top) < 5:
        list_top.append(("---", "0", "0", "0", "0")) 
        
    encabezados = ["#", "Usuario", "Puntaje", "Nivel", "Códigos", "Tiempo"]
    for col, text in enumerate(encabezados):
        lbl = tk.Label(top_frame, text=text, font=psp10, fg="white", bg="#0f0f0f")
        lbl.grid(row=0, column=col, padx=10, pady=5)
    
    for row in range(5):  
        tk.Label(top_frame, text=f"{row+1}.", font=psp10, fg="white", bg="#0f0f0f").grid(row=row+1, column=0, padx=10, pady=5)
        
        for col in range(5):  
            text = list_top[row][col]  
            lbl = tk.Label(top_frame, text=text, font=psp10, fg="white", bg="#0f0f0f")
            lbl.grid(row=row+1, column=col+1, padx=10, pady=5)  
            
    return_btn_top = tk.Button(top_frame, text="Volver", font=psp14, command=lambda: return_btn(top_frame,mj_frame))
    return_btn_top.grid(row=6,column=5,padx=10,pady=10)
    
def opciones():
    mj_frame.pack_forget()
    options_frame = tk.Frame(menu, bg="#0f0f0f")
    op_modificar_cuenta = tk.Button(options_frame, text="Modificar Cuenta", font=psp14, command=lambda:(modificacion_cuenta()), fg="white", bg="#0f0f0f")
    op_eliminar_cuenta = tk.Button(options_frame, text="Eliminar Cuenta", font=psp14, command=lambda:(delcuenta()), fg="white", bg="#0f0f0f")  
    op_return_btn = tk.Button(options_frame, text="Regresar", font=psp14, command=lambda:return_btn(options_frame, mj_frame), fg="white", bg="#0f0f0f")
    
    options_frame.pack(pady=5)
    op_modificar_cuenta.pack(pady=5)
    op_eliminar_cuenta.pack(pady=5)
    op_return_btn.pack(pady=5)
    
    def modificacion_cuenta():
        
        global mod_return_btn
        
        def btt_mod_selectpack():
            options_frame.pack_forget()
            mod_cuenta_frame.pack(pady=5)
            mod_user_btt.pack(pady=5)
            mod_email_btt.pack(pady=5)
            mod_password_btt.pack(pady=5)
            mod_return_btn.pack(pady=5)
            
            mod_emailoruser_lbl.pack_forget()
            mod_emailoruser_etr.pack_forget()
            mod_passlogin_lbl.pack_forget()
            mod_passlogin_etr.pack_forget()
            
        def verification_mod():
            mod_user_btt.pack_forget()
            mod_email_btt.pack_forget()
            mod_password_btt.pack_forget()
            mod_return_btn.pack_forget()
            
            mod_emailoruser_lbl.pack(pady=5)
            mod_emailoruser_etr.pack(pady=5)
            mod_passlogin_lbl.pack(pady=5)
            mod_passlogin_etr.pack(pady=5)
            mod_return_btn.pack(pady=5)
        
        mod_cuenta_frame = tk.Frame(menu, bg="#0f0f0f")
        mod_user_btt = tk.Button(mod_cuenta_frame, text="Modificar Usuario", font=psp14, command=lambda:modificar_dato("Usuario"), fg="white", bg="#0f0f0f")
        mod_email_btt = tk.Button(mod_cuenta_frame, text="Modificar Correo", font=psp14, command=lambda:modificar_dato("Correo"), fg="white", bg="#0f0f0f")
        mod_password_btt = tk.Button(mod_cuenta_frame, text="Modificar Contraseña", font=psp14, command=lambda:modificar_dato("Contraseña"), fg="white", bg="#0f0f0f")
        mod_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame), fg="white", bg="#0f0f0f")
        
        mod_emailoruser_lbl = tk.Label(mod_cuenta_frame, text="Ingrese Correo Electrónico o Usuario", font=psp10, bg="#0f0f0f", fg="white")
        mod_emailoruser_etr = tk.Entry(mod_cuenta_frame, bg="#0f0f0f", fg="white")
        mod_passlogin_lbl = tk.Label(mod_cuenta_frame, text="Ingrese Contraseña", font=psp10, bg="#0f0f0f", fg="white")
        mod_passlogin_etr = tk.Entry(mod_cuenta_frame, bg="#0f0f0f", fg="white")
    
        btt_mod_selectpack()
        
        def modificar_dato(x):
            if x == "Usuario":
                def mod_username():
                    useroremail = mod_emailoruser_etr.get()
                    password = mod_passlogin_etr.get()
                    comprobacion_rtf_mod=rtf.comprobaciónmod(useroremail,password)
                    if comprobacion_rtf_mod[0] == True:          
                        def usermodify():
                            succes = rtf.modifyuser(comprobacion_rtf_mod[0],comprobacion_rtf_mod[1],newuser_etr.get())
                            global newuser_error_lbl
                            newuser_error_lbl = tk.Label(mod_cuenta_frame, text="Usuario ya existe", font=psp6, fg="red", bg="#0f0f0f")
                            if succes == 1:
                                newuser_error_lbl.pack(before=newuser_btt, pady=5) 
                                
                            elif succes == 2:
                                newuser_error_lbl.pack_forget()
                                newuser_btt.pack_forget()
                                newuser_lbl.pack_forget()
                                newuser_etr.pack_forget()
                                user_succes_lbl = tk.Label(mod_cuenta_frame, text="Usuario modificado correctamente", font=psp14,bg="#0f0f0f", fg="white")
                                user_succes_lbl.pack(pady=5)
                                comfirm_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                                comfirm_return_btn.pack(pady=5)
                                
                        global newuser_lbl, newuser_etr, newuser_btt
                        newuser_lbl = tk.Label(mod_cuenta_frame, text="Ingrese un Nombre de usuario nuevo", font=psp10,bg="#0f0f0f", fg="white")
                        newuser_etr = tk.Entry(mod_cuenta_frame, bg="#0f0f0f", fg="white")
                        newuser_btt = tk.Button(mod_cuenta_frame, text="Confirmar", font=psp14, command=usermodify, fg="white", bg="#0f0f0f")
                        
                        
                        mod_emailoruser_lbl.pack_forget()
                        mod_emailoruser_etr.pack_forget()
                        mod_passlogin_lbl.pack_forget()
                        mod_passlogin_etr.pack_forget()
                        mod_return_btn.pack_forget()
                        mod_account_lbl.pack_forget()
                        mod_comfirm_btn.pack_forget()
                        newuser_lbl.pack(pady=5)
                        newuser_etr.pack(pady=5)
                        newuser_btt.pack(pady=5)
    
                    else:
                        mod_account_lbl.pack_forget()
                        mod_comfirm_btn.pack_forget()
                        mod_return_btn.pack_forget()
                        user_error_lbl = tk.Label(mod_cuenta_frame, text="Datos incorrectos", font=psp14,bg="#0f0f0f", fg="red")
                        user_error_lbl.pack(pady=5)
                        comfirm_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                        comfirm_return_btn.pack(pady=5)
                        
                mod_account_lbl = tk.Label(mod_cuenta_frame, text="Modificación de Cuenta", font=psp14, bg="#0f0f0f", fg="white")
                mod_account_lbl.pack(pady=5)
                verification_mod()
                mod_return_btn.pack_forget()
                mod_comfirm_btn = tk.Button(mod_cuenta_frame, text="Confirmar", font=psp14, command=lambda:mod_username(), fg="white", bg="#0f0f0f")
                mod_comfirm_btn.pack(pady=5)
                mod_return_btn.pack(pady=5)
                    
                
            if x == "Correo":
                def mod_email():
                    useroremail = mod_emailoruser_etr.get()
                    password = mod_passlogin_etr.get()
                    comprobacion_rtf_mod=rtf.comprobaciónmod(useroremail,password)
                    if comprobacion_rtf_mod[0] == True:          
                        def emailmodify():
                            succes = rtf.modifyemail(comprobacion_rtf_mod[0],comprobacion_rtf_mod[1],newemail_etr.get())
                            global newemail_error_lbl
                            newemail_error_lbl = tk.Label(mod_cuenta_frame, text="Correo electrónico en uso", font=psp6, fg="red", bg="#0f0f0f")
                            if succes == 1:
                                newemail_error_lbl.pack(before=newuser_btt, pady=5) 
                                
                            elif succes == 2:
                                newemail_error_lbl.pack_forget()
                                newemail_btt.pack_forget()
                                newemail_lbl.pack_forget()
                                newemail_etr.pack_forget()
                                mod_cuenta_frame.pack(pady=5)
                                email_succes_lbl = tk.Label(mod_cuenta_frame, text="Correo Electrónico modificado correctamente", font=psp14,bg="#0f0f0f", fg="white")
                                email_succes_lbl.pack(pady=5)
                                comfirm_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                                comfirm_return_btn.pack(pady=5)
                                
                        global newuser_lbl, newuser_etr, newuser_btt
                        newemail_lbl = tk.Label(mod_cuenta_frame, text="Ingrese un correo electrónico nuevo", font=psp10,bg="#0f0f0f", fg="white")
                        newemail_etr = tk.Entry(mod_cuenta_frame, bg="#0f0f0f", fg="white")
                        newemail_btt = tk.Button(mod_cuenta_frame, text="Confirmar", font=psp14, command=emailmodify, fg="white", bg="#0f0f0f")
                        
                        
                        mod_emailoruser_lbl.pack_forget()
                        mod_emailoruser_etr.pack_forget()
                        mod_passlogin_lbl.pack_forget()
                        mod_passlogin_etr.pack_forget()
                        mod_return_btn.pack_forget()
                        mod_account_lbl.pack_forget()
                        mod_comfirm_btn.pack_forget()
                        newemail_lbl.pack(pady=5)
                        newemail_etr.pack(pady=5)
                        newemail_btt.pack(pady=5)
    
                    else:
                        mod_account_lbl.pack_forget()
                        mod_comfirm_btn.pack_forget()
                        mod_return_btn.pack_forget()
                        user_error_lbl = tk.Label(mod_cuenta_frame, text="Datos incorrectos", font=psp14,bg="#0f0f0f", fg="red")
                        user_error_lbl.pack(pady=5)
                        comfirm_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                        comfirm_return_btn.pack(pady=5)
                        
                mod_account_lbl = tk.Label(mod_cuenta_frame, text="Modificación de usuario", font=psp14, bg="#0f0f0f", fg="white")
                mod_account_lbl.pack(pady=5)
                verification_mod()
                mod_return_btn.pack_forget()
                mod_comfirm_btn = tk.Button(mod_cuenta_frame, text="Confirmar", font=psp14, command=lambda:mod_email(), fg="white", bg="#0f0f0f")
                mod_comfirm_btn.pack(pady=5)
                mod_return_btn.pack(pady=5)

            if x == "Contraseña":   
                def mod_password():
                    useroremail = mod_emailoruser_etr.get()
                    password = mod_passlogin_etr.get()
                    comprobacion_rtf_mod=rtf.comprobaciónmod(useroremail,password)
                    if comprobacion_rtf_mod[0] == True:          
                        def passwordmodify():
                            succes = rtf.modifypassword(comprobacion_rtf_mod[0],comprobacion_rtf_mod[1],newpassword_etr.get())    
                            if succes == 2:
                                mod_cuenta_frame.pack(pady=5)
                                newpassword_btt.pack_forget()
                                newpassword_lbl.pack_forget()
                                newpassword_etr.pack_forget()
                                password_succes_lbl = tk.Label(mod_cuenta_frame, text="Contraseña modificada correctamente", font=psp14,bg="#0f0f0f", fg="white")
                                password_succes_lbl.pack(pady=5)
                                comfirm_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                                comfirm_return_btn.pack(pady=5)
                                
                        global newpassword_lbl, newpassword_etr, newpassword_btt
                        newpassword_lbl = tk.Label(mod_cuenta_frame, text="Ingrese una contraseña nueva", font=psp10,bg="#0f0f0f", fg="white")
                        newpassword_etr = tk.Entry(mod_cuenta_frame, bg="#0f0f0f", fg="white")
                        newpassword_btt = tk.Button(mod_cuenta_frame, text="Confirmar", font=psp14, command=passwordmodify, fg="white", bg="#0f0f0f")
                        
                        
                        mod_emailoruser_lbl.pack_forget()
                        mod_emailoruser_etr.pack_forget()
                        mod_passlogin_lbl.pack_forget()
                        mod_passlogin_etr.pack_forget()
                        mod_return_btn.pack_forget()
                        mod_account_lbl.pack_forget()
                        mod_comfirm_btn.pack_forget()
                        newpassword_lbl.pack(pady=5)
                        newpassword_etr.pack(pady=5)
                        newpassword_btt.pack(pady=5)
    
                    else:
                        mod_account_lbl.pack_forget()
                        mod_comfirm_btn.pack_forget()
                        mod_return_btn.pack_forget()
                        user_error_lbl = tk.Label(mod_cuenta_frame, text="Datos incorrectos", font=psp14,bg="#0f0f0f", fg="red")
                        user_error_lbl.pack(pady=5)
                        comfirm_return_btn = tk.Button(mod_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(mod_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                        comfirm_return_btn.pack(pady=5)
                        
                mod_account_lbl = tk.Label(mod_cuenta_frame, text="Modificación de usuario", font=psp14, bg="#0f0f0f", fg="white")
                mod_account_lbl.pack(pady=5)
                verification_mod()
                mod_return_btn.pack_forget()
                mod_comfirm_btn = tk.Button(mod_cuenta_frame, text="Confirmar", font=psp14, command=lambda:mod_password(), fg="white", bg="#0f0f0f")
                mod_comfirm_btn.pack(pady=5)
                mod_return_btn.pack(pady=5)
                
    def delcuenta():
        def verification_del():
            useroremail = del_emailoruser_etr.get()
            password = delpasslogin_etr.get()                                                                   
            comprobacion_rtf_del=rtf.comprobaciónmod(useroremail,password)
            if comprobacion_rtf_del[0] == True:          
                confirmacion = messagebox.askyesno("Mensaje de confirmación","¿Está seguro de eliminar su cuenta?")
                if confirmacion is True:
                    rtf.deleteaccount(comprobacion_rtf_del[1])
                    pack_forget_widget(del_cuenta_frame)
                    del_cuenta_frame.pack(pady=5)
                    password_succes_lbl = tk.Label(del_cuenta_frame, text="Cuenta eliminada correctamente", font=psp14,bg="#0f0f0f", fg="white")
                    password_succes_lbl.pack(pady=5)
                    comfirm_return_btn = tk.Button(del_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(del_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                    comfirm_return_btn.pack(pady=5)
                else:
                    pack_forget_widget(del_cuenta_frame)
                    del_cuenta_frame.pack(pady=5)
                    password_succes_lbl = tk.Label(del_cuenta_frame, text="Operación Cancelada", font=psp14,bg="#0f0f0f", fg="white")
                    password_succes_lbl.pack(pady=5)
                    comfirm_return_btn = tk.Button(del_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(del_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                    comfirm_return_btn.pack(pady=5)
                        
            else:
                        del_account_lbl.pack_forget()
                        del_comfirm_btn.pack_forget()
                        mod_return_btn.pack_forget()
                        user_error_lbl = tk.Label(del_cuenta_frame, text="Datos incorrectos", font=psp14,bg="#0f0f0f", fg="red")
                        user_error_lbl.pack(pady=5)
                        comfirm_return_btn = tk.Button(del_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(del_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
                        comfirm_return_btn.pack(pady=5)
                        
        options_frame.pack_forget()
        del_cuenta_frame = tk.Frame(menu, bg="#0f0f0f")
        del_account_lbl = tk.Label(del_cuenta_frame, text="Eliminación de Cuenta", font=psp14, bg="#0f0f0f", fg="white")
        del_emailoruser_lbl = tk.Label(del_cuenta_frame, text="Ingrese Correo Electrónico o Usuario", font=psp10, bg="#0f0f0f", fg="white")
        del_emailoruser_etr = tk.Entry(del_cuenta_frame, bg="#0f0f0f", fg="white")
        del_passlogin_lbl = tk.Label(del_cuenta_frame, text="Ingrese Contraseña", font=psp10, bg="#0f0f0f", fg="white")
        delpasslogin_etr = tk.Entry(del_cuenta_frame, bg="#0f0f0f", fg="white")
        del_comfirm_btn = tk.Button(del_cuenta_frame, text="Confirmar", command=lambda:verification_del(), font=psp14, fg="white", bg="#0f0f0f")
        del_return_btn = tk.Button(del_cuenta_frame, text="Regresar", font=psp14, command=lambda:return_btn(del_cuenta_frame, options_frame),bg="#0f0f0f", fg="white")
        pack_widget(del_cuenta_frame)
            
mj_frame = tk.Frame(menu, bg="#0f0f0f")
mj_play_btn = tk.Button(mj_frame, text="Jugar", font=psp14, fg="white", bg="#0f0f0f",command=play)
mj_stats_btn = tk.Button(mj_frame, text="Estadísticas", font=psp14, fg="white", bg="#0f0f0f", command=stats)
mj_top_5_btn = tk.Button(mj_frame, text="Top 5", font=psp14, fg="white", bg="#0f0f0f",command=top5)
mj_options_btn = tk.Button(mj_frame, text="Opciones", font=psp14, command=opciones, fg="white", bg="#0f0f0f")
mj_return_btn = tk.Button(mj_frame, text="Salir", font=psp14, command=lambda:return_btn(mj_frame, menu_start), fg="white", bg="#0f0f0f")

menu.mainloop()
