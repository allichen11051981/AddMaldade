



import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="usma1981", database="elevage")
cursor = conn.cursor()

def searchMalade() :
   while True :
     conn.commit()
     search = input("entrez le nom :")
     cursor.execute("""
     SELECT *
     FROM visit
     WHERE name= %s
     """,(search,))
     user = cursor.fetchone()
     print(user)

     o = input("vous les vous rechercher un autre malade o/n ")
     if o.strip() == 'o':
         continue
     if o.strip() == 'n':
         break

def addMalade() :

    while True :
        nom = input("Entrer le nom du malade :")
        age = input("Entrer son age :")
        diagno = input("entrer le diagnostic :")
        trt = input("Entrer le traitement :")
        user = (nom,age,diagno,trt)


        cursor.execute("""
        INSERT INTO visit
        (name,age,diagno,trt)
        VALUES(%s   ,  %s   , %s  ,  %s)
        """,user)
        conn.commit()
        o = input("vous les vous ajouter un autre malade o/n ")
        if o.strip() == 'o' :
            continue
        if o.strip() == 'n' :
          break

print("                                                      ******************************************")
print("                                                      |                Add Malade              |")
print("                                                      ******************************************")

print("Entrer votre choix")
print()
print("1- Ajouter un nouveau malade")
print("2- Rechercher un malade")
i = input()

if i == '1' :
    addMalade()
if i == '2' :
    searchMalade()