import mysql.connector

choix = 0

bdd = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="",
                                      database="contact")
while choix != 6:
    choix = int(input("Que voulez-vous faire ? :\n1- Afficher\n2- Ajouter\n3- Modifier\n4- Supprimer\n5- Rechercher\n6- Quitter\n"))

    if choix == 1:
        
        curseur = bdd.cursor()
        curseur.execute("select * from contact order by nom")
        for contact in curseur.fetchall():
            print(contact[0],contact[1],contact[2],contact[3],contact[4])
            
    elif choix == 2:
        
        nom = input("Entrez le nom du contact :  ")
        prenom = input("Entrez le prenom du contact :  ")
        mail = input("Entrez le mail du contact :  ")
        tel = input("Entrez le tel du contact :  ")

        curseur = bdd.cursor()
        req = "insert into contact values(null,'"+nom+"','"+prenom+"','"+mail+"','"+tel+"')"
        curseur.execute(req)
        
    elif choix == 3:
        
        num = input("Mettez le numéro du contact pour le sélectionnez  : " )
        req = "select id from contact where '"+num+"' "
        curseur1 = bdd.cursor()
        curseur1.execute(req)
        for contact in curseur1.fetchall():
            res = int(input("Inscrivez le numéro a modifier du contact : \n1- Nom  \n2- Prenom \n3- email\n4- telephone \n\n"))
            if res == 1:
               newNom = input("rentrez le nouveau nom : ")
               curseur = bdd.cursor()
               req2 = "update contact set nom = '"+newNom+"' where id = '"+str(contact[0])+"'"
               curseur.execute(req2)
               
            elif res == 2:
               newPrenom = input("rentrez le nouveau prenom : ")
               curseur = bdd.cursor()
               req3 = "update contact set prenom = '"+newPrenom+"' where id = '"+str(contact[0])+"'"
               curseur.execute(req3)
               
            elif res == 3:
               newMail = input("rentrez le nouveau mail : ")
               curseur = bdd.cursor()
               req = "update contact set email = '"+newMail+"' where id = '"+str(contact[0])+"'"
               curseur.execute(req)
               
            elif res == 4:
               newTel = int(input("rentrez le nouveau telephone : "))
               curseur = bdd.cursor()
               req4 = "update contact set tel = '"+newTel+"' where id = '"+str(contact[0])+"'"
               curseur.execute(req4)

               
    elif choix == 4:
        
        num = input("Ecrivez le numero du contact pour le supprimer : ")
        req5 = "delete from contact where tel = '"+num+"'"
        curseur = bdd.cursor()
        curseur.execute(req5)
        print("Le contact a bien été supprimer \n") 
      
                
        
        
        

 

        

