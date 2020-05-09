from flask import Flask, render_template, request, redirect, url_for
from cachetools import cached, TTLCache
import sys, os
sys.path.append(os.path.join(sys.path[0], 'static', 'py'))
import recherche as r
import chargerFichier as cf

app = Flask(__name__)

index = None

@app.before_first_request
def read_index():
    global index
    index = r.getIndex()

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/search', methods=["GET","POST"])
def search():
    req = request.args.get('textToSearch')
    if(req == ''):
        return redirect(url_for('index'))
    resList2 = r.recherche(req, index)
    top10 = r.getTop10pages(resList2)
    return render_template('search.html', textToSearch=req, resList=top10)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, threaded=True)
