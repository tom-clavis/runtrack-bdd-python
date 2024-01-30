import mysql.connector

def connection():
    return mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "1234",
    database="entreprise",
)
def argent(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
    for employe in cursor.fetchall():
        print(employe)
        
        
def service(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT e.nom, e.prenom, s.nom AS service_name
    FROM employe e
    INNER JOIN service s ON e.id_service = s.id
    """)
    for employe in cursor.fetchall():
        print(employe)

        
        

conn = connection()

print("Employé avec un salaire plus de 3000:")
argent(conn)


print("\nservice des employés:")
service(conn)


class employe:
    def __init__(self):
        
        self.database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1234",
            database = "entreprise"
        )
        self.cursor = self.database.cursor()
        
    
    def add_employe(self, nom,prenom,salaire,id_service):
        self.cursor.execute(f"INSERT INTO employe (nom,prenom,salaire,id_service) VALUES ('{nom}','{prenom}',{salaire},{id_service})")
        self.database.commit()
    
    def delete_employe(self,nom):
        self.cursor.execute(f"DELETE FROM employe WHERE nom = {nom} OR prenom = {nom}")
        self.database.commit()
    
    def afficher_employe(self):
        self.cursor.execute("SELECT * FROM employe")
        for ligne in self.cursor.fetchall():
            print(ligne)
    
    def modifie_employe(self,nom,prenom,salaire,id_service):
        self.cursor.execute(f"UPDATE employe SET nom = '{nom}' prenom = '{prenom}' salaire = {salaire} id_service = {id_service}")
        self.database.commit()