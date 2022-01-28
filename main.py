from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    title='Inklut'
    return render_template('frontend.html', title=title, now=datetime.utcnow())

@app.route('/multimedia')
def multimedia():
    return render_template('multimedia.html', now=datetime.utcnow())

@app.route('/faq')
def faq():
    return render_template('faq.html', now=datetime.utcnow())

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', now=datetime.utcnow())

# Error 404
@app.route('/<error>')
@app.errorhandler(404)
def page_not_found(error):
    return render_template('components/errors/404.html', error=error), 404

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
