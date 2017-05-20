#!/usr/bin/python
__author__ = "Daniel Fernando Santos Bustos"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Daniel Santos"
__email__ = "dfsantosbu@unal.edu.co"
__status__ = "Production"

"""
    =======================================
    Hello I'm Daniel, I think that open
    source is the right way to do things
    for that reason I share the project,
    I hope that this  be useful for
    your job.
    If you want  something similar don't
    hesitate to fork and star the project.
    Regards Daniel Santos.
    =======================================
"""

from flask import Flask, render_template, jsonify
from api_blueprint import api


app = Flask(__name__)
app.register_blueprint(api)
"""
    Create no heavy request at the init of the application
"""


@app.route('/')
def browser ():
    try:
        return render_template('browser.html')
    except Exception as e:
        return render_template('500.html',error=e)

@app.route('/about/')
def index():
    return render_template('about.html')

@app.route('/content/')
def content():
    try:
        return render_template('content.html')
    except Exception as e:
        return render_template('500.html',error=e)

if __name__ =="__main__":
    print(__doc__)
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
