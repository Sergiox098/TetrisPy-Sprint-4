import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("tetrispy-3688a-firebase-adminsdk-5bay2-831edfedd6.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://tetrispy-3688a-default-rtdb.firebaseio.com/"
})
users = "Users/"
usersref = db.reference(users)

def signuser(x,y,z):
    existing_users = usersref.get()
    duplicadoname = False
    duplicadoemail = False
    if existing_users is None:
        existing_users = {}
    for u in existing_users.values():
        if u['Nombre de Usuario'] == x:
            duplicadoname = True  
        if u["Correo Electrónico"] == y:
            duplicadoemail = True 
    if duplicadoname:
        return 1
    if duplicadoemail:
        return 2
    if duplicadoemail and duplicadoname:
        return 3
    if duplicadoname == False and duplicadoemail == False:
        usersref.push().set({
            "Nombre de Usuario": x,
            "Correo Electrónico": y,
            "Contraseña": z,
            "Puntaje máximo alcanzado": 0,
            "Máximo de códigos realizados":0,
            "Nivel más alto": 0,
            "Tiempo de partida" : 0
        })
        return x
def loginuser(x,z):
    existing_users = usersref.get()
    if existing_users is None:
        existing_users = {}
    correct_username = False
    correct_password = False
    for u in existing_users.values():
        if u['Nombre de Usuario'] == x:
            correct_username = True

        if u['Contraseña'] == z:
            correct_password = True
    if correct_username and correct_password:
        return 1
    
def puntaje(x,y):
        existing_users = usersref.get()
        if existing_users is None:
            existing_users = {}
        for key,u in existing_users.items():
            if u['Nombre de Usuario'] == x:
                usersref.child(key).update({
                    "Puntaje máximo alcanzado": y
                })
                succes = True
                return succes
        
def nivel(x,y):
        print("Esta sección del menú es para que ingreses el nivel máximo obtenido")
        existing_users = usersref.get()
        if existing_users is None:
            existing_users = {}
        for key,u in existing_users.items():
            if u['Nombre de Usuario'] == x:
                usersref.child(key).update({
                    "Nivel más alto": y
                })
        print("El nivel ha sido registrado en la cuenta:",x)
def codigo(x,y):
        existing_users = usersref.get()
        if existing_users is None:
            existing_users = {}
        for key,u in existing_users.items():
            if u['Nombre de Usuario'] == x:
                usersref.child(key).update({
                    "Máximo de códigos realizados": y
                })
        print("El máximo de códigos realizados ha sido registrado en la cuenta:",x)
def topleaderboard():
    leaderboard = usersref.get()
    list_top=[]
    top=()
    if leaderboard is None:
        leaderboard = {}
    for i in leaderboard.values():
        topscore=i['Puntaje máximo alcanzado']
        topuser=i['Nombre de Usuario']
        top=(topuser,topscore)
        list_top.append(top)
    list_top.sort(key = lambda x: x[1],reverse=True)
    cont = 0
    while cont < len(list_top):
        print(cont+1,list_top[cont])
        cont += 1
        if  cont == 4:
            break
def deleteaccount(y,z,p):
    p=str(p)
    success = False
    usersdata = usersref.get()
    if usersdata is None:
        usersdata = {}
    for key,value in usersdata.items():
        print(value)
        if value["Correo Electrónico"] == y and value["Contraseña"] == z:
            print(f"\nCuenta encontrada: {value}")
            if p.lower() == "si":
                usersref.child(key).delete()
                print("\n¡Cuenta eliminada exitosamente!")
                success = True
                return True
            else:
                print("\nOperación cancelada.")
                return False
    if success == False:
        print("\nNo se encontró ninguna cuenta con el identificador proporcionado.")
        return False
def comprobaciónmod(x,z):       
    usersdata = usersref.get()
    correct = False
    if usersdata is None:
        usersdata = {}
    for key,i in usersdata.items():
        print(key,(i["Contraseña"] == z))
        print(i["Nombre de Usuario"] == x or i["Correo Electrónico"] == x)
        if(i["Contraseña"] == z and (i["Nombre de Usuario"] == x or i["Correo Electrónico"] == x)):
            return True, key
    if correct == False:
        return False, None
    
def modifyuser(x,y,z):
    if x == True:
        existing_users = usersref.get()
        duplicadoname = False
        if existing_users is None:
            existing_users = {}
        for u in existing_users.values():
            if u['Nombre de Usuario'] == z:
                duplicadoname = True 
        if duplicadoname:
            return 1
        else:
            usersref.child(y).update({"Nombre de Usuario" : z})    
            return 2
def modifyemail(x,z):
    usersdata = usersref.get()
    if usersdata is None:
        usersdata = {}
    for key,i in usersdata.items():
        if(i["Contraseña"] == z and (i["Nombre de Usuario"] == x or i["Correo Electrónico"] == x)):
            newemail = str(input("Ingrese  nuevo correo: "))
            usersref.child(key).update({"Correo Electrónico" : newemail})   
            print("El cambio ha sido regristrado correctamente")
            break
def modifypassword(x,z):
    usersdata = usersref.get()
    if usersdata is None:
        usersdata = {}
    for key,i in usersdata.items():
        if(i["Contraseña"] == z and (i["Nombre de Usuario"] == x or i["Correo Electrónico"] == x)):
            newpassword = str(input("Ingrese  nueva contraseña: "))
            usersref.child(key).update({"Contraseña" : newpassword})   
            print("El cambio ha sido regristrado correctamente")
        else:
            print("La contraseña no fue escrita correctamente")
        break