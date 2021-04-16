import datetime
import google.oauth2.id_token
from flask import Flask, render_template, request
from google.auth.transport import requests
from flask import Flask, render_template
from google.cloud import datastore

datastore_client = datastore.Client()
firebase_request_adapter = requests.Request()


#name_key = datastore_client.key("Name", "Name1")
#name_task = datastore.Entity(key=name_key)
#datastore_client.put(name_task)

#manufacturer_key = datastore_client.key("Manufacturer", "Manufacturer1")
#manufacturer_task = datastore.Entity(key=manufacturer_key)
#datastore_client.put(manufacturer_task)

#geometryShader_entity = datastore.Entity(key = datastore_client.key('geometryShader'))
#datastore_client.put(geometryShader_entity)

#tesselationShader_entity = datastore.Entity(key = datastore_client.key('tesselationShader'))
#datastore_client.put(tesselationShader_entity)

#shaderInt16_entity = datastore.Entity(key = datastore_client.key('shaderInt16'))
#datastore_client.put(shaderInt16_entity)

#sparseBinding_entity = datastore.Entity(key = datastore_client.key('sparseBinding'))
#datastore_client.put(sparseBinding_entity)

#textureCompressionETC2_entity = datastore.Entity(key = datastore_client.key('textureCompressionETC2'))
#datastore_client.put(textureCompressionETC2_entity)

#vertexPipelineStoresAndAtomics_entity = datastore.Entity(key = datastore_client.key('vertexPipelineStoresAndAtomics'))
#datastore_client.put(vertexPipelineStoresAndAtomics_entity)

def getClientInfo():
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    claims = google.oauth2.id_token.verify_firebase_token(id_token,firebase_request_adapter)
    return claims

def addGPU(result):
    gpu_key = datastore_client.key("Name",result['name'])
    gpu_task = datastore.Entity(key=gpu_key)
    gpu_task.update({
        'Name': result['name'],
        'Manufacturer': result['manufacturer'],
        'DateIss': result['dateIss'],
        'GeometryShader': result['geometryShader'],
        'TesselationShader': result['tesselationShader'],
        'ShaderInt16': result['shaderInt16'],
        'SparseBinding': result['sparseBinding'],
        'TextureCompressionETC2': result['textureCompressionETC2'],
        'VertexPipelineStoresAndAtomics': result['vertexPipelineStoresAndAtomics'],
    })
    datastore_client.put(gpu_task)



def fetchGPUByName(search):
    query = datastore_client.query(kind='Name')
    query.add_filter("Name", "=", search)
    gpus = query.fetch()
    return gpus

def fetchGPUAll():
    query = datastore_client.query(kind='Name')
    query.order = ["-Name"]
    gpus = query.fetch()
    return gpus


app = Flask(__name__)

@app.route('/', methods=['POST'])
def save():
    #claims = getClientInfo()
    result = request.form
    res = fetchGPUByName(result['name'])
    gpus = fetchGPUAll()
    if sum(1 for _ in res) ==0:
        addGPU(result)
        err=""
    else:
        err="GPU already exists"
    return render_template('index.html',error=err, gpus=gpus)#,user_data=claims


@app.route('/viewgpu')
def viewGPU():
    result = request.args
    res = fetchGPUByName(result['name'])
    return render_template('viewgpu.html', gpus=res, gpuname=result['name'])


@app.route('/')
def root():
     gpus = fetchGPUAll()
     return render_template('index.html', gpus=gpus)#,user_data=claims


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
