from arango import ArangoClient
from random import randint
# Initialize the client for ArangoDB.
client = ArangoClient(hosts="http://35.242.163.101:80")

# Conectarse a la base de datos "_system" (es la default en la que te metes cuando entras)
# Connec to "_system" database as root user.

sys_db = client.db("_system", username="root", password="rootpassword")

# Create a new database named "test".
#sys_db.delete_collection("students")
i=str(randint(0,1000))
nombre="a"+i
students = sys_db.create_collection(nombre)
