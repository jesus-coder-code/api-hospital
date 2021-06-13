import psycopg2

def up_pPass(id, password):
    connect = psycopg2.connect(
        host = "postgresql-jesus.alwaysdata.net",
        database = "jesus_hospital",
        user = "jesus",
        password = "51246380"
    )
    mycursor = connect.cursor()
    query = "UPDATE usuariopaciente SET password = '{}' WHERE id = '{}'".format(password, id)
    #values = (id, email, phone, password)
    q = mycursor.execute(query)

    connect.commit()

    if (q):
        return True
    else:
        return False