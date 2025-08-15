import pymysql

from flask import Flask, render_template
from controllers import routes


app = Flask(__name__, template_folder='views')

routes.init_app(app)


if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    app.run(host='localhost', port=5000, debug=True)
