import psycopg2

def registerh(id, name, adress, services):
    connect = psycopg2.connect(
        host = "postgresql-jesus.alwaysdata.net",
        database = "jesus_hospital",
        user = "jesus",
        password = "51246380"
    )
    mycursor = connect.cursor()
    query = "INSERT INTO hospital (id, name, adress, services) VALUES (%s, %s, %s, %s)"
    values = (id, name, adress, services)
    q = mycursor.execute(query, values)
    connect.commit()

    if (q):
        return True
    else:
        return False