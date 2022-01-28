from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Inklut'
    return render_template('pages/frontend.html', title=title, now=datetime.utcnow())

@app.route('/multimedia')
def multimedia():
    title = 'Productos Digitales'
    return render_template('pages/multimedia.html', title=title, now=datetime.utcnow())

@app.route('/faq')
def faq():
    title = 'Preguntas Frecuentes'
    return render_template('pages/faq.html', title=title, now=datetime.utcnow())

@app.route('/contacto')
def contacto():
    title = 'Contacto'
    return render_template('pages/contacto.html', title=title, now=datetime.utcnow())

# Error 404
@app.route('/<error>')
@app.errorhandler(404)
def page_not_found(error):
    return render_template('components/errors/404.html', error=error), 404

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
