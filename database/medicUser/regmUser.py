import psycopg2

def reg_mUser(id, email, phone, password):
    connect = psycopg2.connect(
        host = "postgresql-jesus.alwaysdata.net",
        database = "jesus_hospital",
        user = "jesus",
        password = "51246380"
    )
    mycursor = connect.cursor()
    query = "INSERT INTO usuariomedico (id, email, phone, password) VALUES (%s, %s, %s, %s)"
    values = (id, email, phone, password)
    q = mycursor.execute(query, values)
    connect.commit()

    if (q):
        return True
    else:
        return False