import psycopg2

def register(id, name, adress, date):
    connect = psycopg2.connect(
        host = "postgresql-jesus.alwaysdata.net",
        database = "jesus_hospital",
        user = "jesus",
        password = "51246380"
    )
    mycursor = connect.cursor()
    query = "INSERT INTO pacientes (id, name, adress, date) VALUES (%s, %s, %s, %s)"
    values = (id, name, adress, date)
    q = mycursor.execute(query, values)
    connect.commit()

    if (q):
        return True
    else:
        return False
