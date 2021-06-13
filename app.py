from flask import Flask, jsonify, request
from database.getObservation import getObservation
from database.patientUser.regpUser import reg_pUser
from database.hospitalUser.reghUser import reg_hUser
from database.medicUser.regmUser import reg_mUser
from database.hospitalUser.uphPass import up_hPass
from database.patientUser.uppPass import up_pPass
from database.medicUser.upmPass import up_mPass
from database.medicUser.observation import observation
from database.getObservation import getObservation
from database.regPatient import register
from database.regHospital import registerh

app = Flask(__name__)

'''obtener observaciones'''
@app.route('/getOb')
def getOb():
    get_observation = getObservation()
    try:
        if get_observation:
            return jsonify(get_observation)
        else:
            return jsonify({"mensaje":"error al traer los datos"})
    except:
        return jsonify({"mensaje":"error interno"})

#datos basicos paciente
@app.route('/registrar', methods = ['POST'])
def postPatient():
    if request.method == 'POST':
        add = request.json
        id = add['id']
        name = add['name']
        adress = add['adress']
        date = add['date']
        if register(id, name, adress, date):
            print("hecho")
        return jsonify({"mensaje":"guardado correctamente"})

#endpoint para registrar usuario tipo paciente
@app.route('/regpUser', methods = ['POST'])
def postpUser():
    if request.method == 'POST':
        add = request.json
        id = add['id']
        email = add['email']
        phone = add['phone']
        password = add['password']
        if reg_pUser(id, email, phone, password):
            return jsonify({"mensaje": "usuario paciente registrado"})
        return jsonify({"mensaje":"correcto"})

'''datos basicos hospital'''
@app.route('/reghospital', methods = ['POST'])
def postHospital():
    if request.method == 'POST':
        add = request.json
        id = add['id']
        name = add['name']
        adress = add['adress']
        services = add['services']
        if registerh(id, name, adress, services):
            print("hecho")
        return jsonify({"mensaje":"guardado correctamente"})
        
#endpoint para registro de usuario tipo hospital
@app.route('/reghUser', methods = ['POST'])
def posthUser():
    if request.method == 'POST':
        add = request.json
        id = add['id']
        email = add['email']
        phone = add['phone']
        password = add['password']
        if reg_hUser(id, email, phone, password):
            print("hecho")
        return jsonify({"mensaje":"usuario hospital registrado"})

#registro de usuario tipo medico
@app.route('/regmUser', methods = ['POST'])
def postmUser():
    if request.method == 'POST':
        add = request.json
        id = add['id']
        email = add['email']
        phone = add['phone']
        password = add['password']
        if reg_mUser(id, email, phone, password):
            print("hecho")
        return jsonify({"mensaje":"usuario medico registrado"})

#registrar observaciones medicas
@app.route('/regOb', methods = ['POST'])
def postObservation():
    if request.method == 'POST':
        add = request.json
        idpaciente = add['idpaciente']
        nompacient = add['nompacient']
        fechnac = add['fechnac']
        hospital = add['hospital']
        medico = add['medico']
        observacion = add['observacion']
        estado = add['estado']
        especialidad = add['especialidad']
        if observation(idpaciente, nompacient, fechnac, hospital, medico, observacion, estado, especialidad):
            print("hecho")
        return jsonify({"mensaje":"observacion registrada"})

#actualizar contraseña de hospital
@app.route('/uphPass', methods = ['PUT'])
def puthPass():
    if request.method == 'PUT':
        add = request.json
        id = add['id']
        password = add['password']
        if up_hPass(id, password):
            print("hecho")
        return jsonify({"mensaje":"contraseña hospital actualizada"})
    else:
        return jsonify({"mensaje":"error"})

#actualizar contraseña usuario paciente
@app.route('/uppPass', methods = ['PUT'])
def putpPass():
    if request.method == 'PUT':
        add = request.json
        id = add['id']
        password = add['password']
        if up_pPass(id, password):
            print("hecho")
        return jsonify({"mensaje":"contraseña paciente actualizada"})
    else:
        return jsonify({"mensaje":"error"})

#actualizar contraseña usuario medico
@app.route('/upmPass', methods = ['PUT'])
def putmPass():
    if request.method == 'PUT':
        add = request.json
        id = add['id']
        password = add['password']
        if up_mPass(id, password):
            print("hecho")
        return jsonify({"mensaje":"contraseña medico actualizada"})
    else:
        return jsonify({"mensaje":"error"})

if __name__ == "__main__":
    app.run(debug=True)
