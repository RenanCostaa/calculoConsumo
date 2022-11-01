import logging
from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__)

class veiculo:    

    @app.route("/", methods=['GET','POST'])
    def index():  
        dict = {}
        try:
            gasolina = json.loads(open('combustiveis.json','r').readlines()[0])
            print(gasolina)
            logging.info("validacao request GET/POST")
            if request.method == 'POST':
                logging.info("is Post")
                carro_usuario = request.form['input_name_car']
                km_liter = float(request.form['input_km_ltr'])
                dist_viagem = float(request.form['input_dist_viagem'])
                dict = {
                    "CARRO" : carro_usuario,
                    "KM/L" : km_liter,
                    "DISTANCIA": dist_viagem
                }

        except:
            logging.error("exception on request")
            pass

        return render_template('index.html') 

if app == __name__:
    app.run(debug=True)
