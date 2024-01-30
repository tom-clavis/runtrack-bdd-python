import mysql.connector

mymbd = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "1234",
    database="LaPlateforme",
)

cursor=mymbd.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle")

result = cursor.fetchone()


print(f"La capacité totale des salles est de {result[0]}")


cursor.close()
mymbd.close()
