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
            print(gasolina['gasolina']['31/10'])
            logging.info("validacao request GET/POST")
            if request.method == 'POST':
                logging.info("is Post")
                carro_usuario = request.form['input_name_car']
                km_liter = float(request.form['input_km_ltr'])
                dist_viagem = float(request.form['input_dist_viagem'])
                date = request.form['input_date']
                valor_dia = float(gasolina['gasolina'][date])
                calculo = (dist_viagem/km_liter) * valor_dia
                dict = {
                    "CARRO" : carro_usuario,
                    "KM/L" : km_liter,
                    "DISTANCIA": dist_viagem,
                    "DATE" : date,
                    "VALOR DO DIA" : valor_dia,
                    "CALCULO" : round(calculo,2)
                }

        except:
            logging.error("exception on request")
            pass

        print(dict) 
        return render_template('index.html', dict = dict)

    

if app == __name__:
    app.run(debug=True)
