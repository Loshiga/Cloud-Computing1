import datetime
import google.oauth2.id_token
from flask import Flask, render_template, request
from google.auth.transport import requests
from flask import Flask, render_template
from google.cloud import datastore

datastore_client = datastore.Client()
firebase_request_adapter = requests.Request()


name_key = datastore_client.key("Name", "Name1")
name_task = datastore.Entity(key=name_key)
datastore_client.put(name_task)

manufacturer_key = datastore_client.key("Manufacturer", "Manufacturer1")
manufacturer_task = datastore.Entity(key=manufacturer_key)
datastore_client.put(manufacturer_task)

geometryShader_entity = datastore.Entity(key = datastore_client.key('geometryShader'))
datastore_client.put(geometryShader_entity)

tesselationShader_entity = datastore.Entity(key = datastore_client.key('tesselationShader'))
datastore_client.put(tesselationShader_entity)

shaderInt16_entity = datastore.Entity(key = datastore_client.key('shaderInt16'))
datastore_client.put(shaderInt16_entity)

sparseBinding_entity = datastore.Entity(key = datastore_client.key('sparseBinding'))
datastore_client.put(sparseBinding_entity)

textureCompressionETC2_entity = datastore.Entity(key = datastore_client.key('textureCompressionETC2'))
datastore_client.put(textureCompressionETC2_entity)

vertexPipelineStoresAndAtomics_entity = datastore.Entity(key = datastore_client.key('vertexPipelineStoresAndAtomics'))
datastore_client.put(vertexPipelineStoresAndAtomics_entity)

app = Flask(__name__)
@app.route('/')
def root():
     return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
