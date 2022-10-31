from dis import dis
import logging
from flask import Flask, render_template, request, redirect
import _json

app = Flask(__name__)

class veiculo:    
    @app.route("/", methods=['GET','POST'])
    def index():
        dict = {}
        try:
            logging.info("validacao request GET/POST")
            if request.method == 'POST':
                logging.info("is Post")
                carro_usuario = request.form['input_name_car']
                km_liter = request.form['input_km_ltr']
                dist_viagem = request.form['input_dist_viagem']
                dict = {
                    "CARRO" : carro_usuario,
                    "KM/L" : km_liter,
                    "DISTANCIA": dist_viagem
                }
        except:
            logging.eror("exception on request")
            pass

        
        print(dict) 
        return render_template('index.html')

if app == __name__:
    app.run(debug=True)
