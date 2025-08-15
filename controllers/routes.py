from flask import render_template, request, url_for, redirect
import urllib
import json

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/api', methods=['GET', 'POST'])
    def api():
        url = 'https://ghibliapi.vercel.app/films'
        response = urllib.request.urlopen(url)
        apiData = response.read()
        animeList = json.loads(apiData)

        return render_template('api.html', animeList=animeList)
