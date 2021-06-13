import psycopg2

def observation(idpaciente, nompacient, fechnac, hospital, medico, observacion, estado, especialidad):
    connect = psycopg2.connect(
        host = "postgresql-jesus.alwaysdata.net",
        database = "jesus_hospital",
        user = "jesus",
        password = "51246380"
    )
    mycursor = connect.cursor()
    query = "INSERT INTO observaciones (idpaciente, nompacient, fechnac, hospital, medico, observacion, estado, especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (idpaciente, nompacient, fechnac, hospital, medico, observacion, estado, especialidad)
    q = mycursor.execute(query, values)
    connect.commit()

    if (q):
        return True
    else:
        return False