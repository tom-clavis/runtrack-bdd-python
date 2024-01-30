import mysql.connector

mymbd = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "1234",
    database="LaPlateforme",
)

cursor=mymbd.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

result = cursor.fetchone()


print(f"La superficie de la Plateforme est de {result[0]} m2")



cursor.close()
mymbd.close()
