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
                if u['Puntaje máximo alcanzado'] < y:
                    usersref.child(key).update({
                        "Puntaje máximo alcanzado": y
                    })
                    return True
                else:
                    return 0
        
def nivel(x,y):
        existing_users = usersref.get()
        if existing_users is None:
            existing_users = {}
        for key,u in existing_users.items():
            if u['Nombre de Usuario'] == x:
                if u['Nivel más alto'] < y:
                    usersref.child(key).update({
                        "Nivel más alto": y
                    })
                    return True
                else:
                    return 0

def codigo(x,y):
        existing_users = usersref.get()
        if existing_users is None:
            existing_users = {}
        for key,u in existing_users.items():
            if u['Nombre de Usuario'] == x:
                if u["Máximo de códigos realizados"] < y:
                    usersref.child(key).update({
                        "Máximo de códigos realizados": y
                    })
                    return True
                else:
                    return 0
def tiempo(x,y):
    existing_users = usersref.get()
    if existing_users is None:
        existing_users = {}
    for key,u in existing_users.items():
        if u['Nombre de Usuario'] == x:
            if u['Tiempo de partida'] < y:
                usersref.child(key).update({
                    "Tiempo de partida": y
                })
                return True
            else:
                return 0

def getscore(x):
    existing_users = usersref.get()
    if existing_users is None:
        existing_users = {}
    for key,u in existing_users.items():
        if u['Nombre de Usuario'] == x:
            scores=usersref.child(key).get()
            scorelist = [
                scores["Puntaje máximo alcanzado"],
                scores["Nivel más alto"],
                scores["Máximo de códigos realizados"],
                scores["Tiempo de partida"]
            ]
            return scorelist
   
    
def topleaderboard():
    leaderboard = usersref.get()
    list_top=[]
    top=()
    if leaderboard is None:
        leaderboard = {}
    for i in leaderboard.values():
        topscore=str(i['Puntaje máximo alcanzado'])
        topuser=str(i['Nombre de Usuario'])
        toplevel=str(i['Nivel más alto'])
        topmaxcode=str(i['Máximo de códigos realizados'])
        toptime=str(i['Tiempo de partida'])
        top=(topuser,topscore,toplevel,topmaxcode,toptime)
        list_top.append(top)
    list_top.sort(key = lambda x: x[1],reverse=True)
    cont = 0
    list_top5 = []
    while cont < len(list_top):
        list_top5.append(list_top[cont])
        cont += 1
        if  cont == 5:
            return list_top5
        

def deleteaccount(x):
    usersref.child(x).delete()
            
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
        
def modifyemail(x,y,z):
    if x == True:
        existing_users = usersref.get()
        duplicadoname = False
        if existing_users is None:
            existing_users = {}
        for u in existing_users.values():
            if u['Correo Electrónico'] == z:
                duplicadoname = True 
        if duplicadoname:
            return 1
        else:
            usersref.child(y).update({"Correo Electrónico" : z})    
            return 2
        
def modifypassword(x,y,z):
    if x == True:
        existing_users = usersref.get()
        duplicadoname = False
        if existing_users is None:
            existing_users = {}
        for u in existing_users.values():
            if u['Contraseña'] == z:
                duplicadoname = True 
        if duplicadoname:
            return 1
        else:
            usersref.child(y).update({"Contraseña" : z})    
            return 2
