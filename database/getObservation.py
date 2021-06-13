import psycopg2

def getObservation():
    get_observation = []
    connect = psycopg2.connect(
        host="postgresql-jesus.alwaysdata.net",
        database="jesus_hospital",
        user="jesus",
        password="51246380"
    )
    cur = connect.cursor()
    cur.execute("SELECT * FROM observaciones")
    query = cur.fetchall()
    for x in query:
        data = {
        "idpaciente":x[0], 
        "nompacient":x[1],
        "fechnac":x[2],
        "hospital":x[3],
        "medico":x[4],
        "observacion":x[5],
        "estado":x[6],
        "especialidad":x[7]
        }
        get_observation.append(data)
    return get_observation
