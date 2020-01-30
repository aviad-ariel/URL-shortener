from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
from algo import *
from StatsManager import *
import requests

app = Flask(__name__)
manager = StatsManager()
manager.start_jobs()

#if in debug mode proxy requests to the dev server otherwise (production) render the built vue template
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

#encode route, gets the url in the request body and return the hash_id (final shortened url = example.com/hash_id)
@app.route('/api', methods = ['POST'])
def index():
    if request.method == 'POST':
        with sqlite3.connect('url.db') as db:
            return jsonify(url_shorter(request.get_json(), db.cursor()))

#decode route 
@app.route('/<hash_id>')
def redirect_route(hash_id):
    with sqlite3.connect('url.db') as db:
        url = decode_url(hash_id, db.cursor())
        if url:
            manager.add(True)
            return redirect("http://" + url, code=302)
        else:
            manager.add(False)
            return redirect('http://localhost:5000/', code=404)

@app.route('/stats')
def stats():
    return manager.get()
    
if __name__ == '__main__':
    app.run(debug=False)