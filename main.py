from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='index'):
    return render_template(name + '.htm')

if __name__ == '__main__':
    app.debug = True
    app.run()