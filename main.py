import os
import json
import ipdb

from flask import Flask, jsonify, render_template, Response
from openai import OpenAI

app = Flask(__name__)
my_secret = os.environ['OPENAI_KEY']
OPENAI_API_KEY = my_secret


@app.route('/')
def index():
  return render_template('index.html', )


@app.route('/generateimages/<prompt>')
def generate(prompt):
  client = OpenAI(api_key=OPENAI_API_KEY)
  print("prompt :", prompt)
  response = client.images.generate(model="dall-e-2",
                                    prompt=prompt,
                                    n=3,
                                    size="256x256")
  print(response)
  # ipdb.set_trace()
  interpreted_response = [image.url for image in response.data]
  json_response = json.dumps(interpreted_response)
  return Response(json_response, status=200, mimetype='application/json')


app.run(host='0.0.0.0', port=81)
