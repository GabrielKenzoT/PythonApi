from flask import render_template, request, url_for, redirect
import urllib
import json

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/api', methods=['GET', 'POST'])
    @app.route('/api/<string:id>', methods=['GET', 'POST'])
    def api(id=None):
        url = 'https://ghibliapi.vercel.app/films'
        response = urllib.request.urlopen(url)
        apiData = response.read()
        animeList = json.loads(apiData)
        if id:
            animeInfo = []
            for anime in animeList:
                if anime['id'] == id:
                    animeInfo = anime 
                    break

            if animeInfo: 
                return render_template('apiinfo.html', animeInfo=animeInfo)
            else:
                return f'Filme com a ID {id} não foi encontrado.'
        else:
            return render_template('api.html', animeList=animeList)
