from flask import Flask, render_template, request, redirect, url_for
from gevent.pywsgi import WSGIServer
import sys, os
sys.path.append(os.path.join(sys.path[0], 'static', 'py'))
import recherche as r
import chargerFichier as cf

app = Flask(__name__)

index = None
port = 5000

def read_index():
    print("Chargement de l'index en cours...")
    print("Cette opération peut prendre quelques minutes. Merci de patienter.")
    global index
    index = r.loadIndex()
    print("Chargement de l'index terminé !")
    print("Serveur démarré en localhost sur le port ", port)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/search', methods=["GET","POST"])
def search():
    req = request.args.get('textToSearch')
    if(req == ''):
        return redirect(url_for('index'))
    resList2 = r.recherche_debug(req, index)
    top10 = r.getTop10pages(resList2)
    return render_template('search.html', textToSearch=req, resList=top10)


if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    if len(sys.argv) > 1:
        port = int(sys.argv[1])            
    http_server = WSGIServer(('', port), app)
    print("Lancement du serveur")
    read_index()
    http_server.serve_forever()
