from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    title='Inklut'
    return render_template('frontend.html', title=title, now=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
