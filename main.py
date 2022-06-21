from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
# from flask_appconfig import AppConfig
# from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
# from .nav import nav
# from wtforms.fields import *
# from wtforms_validators import *
from google.cloud import storage
from datetime import datetime
import os

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

#
# nav.register_element('frontend_top', Navbar(
#     View('Flask-Bootstrap', '.index'),
#     View('Home', '.index'),
#     View('Forms Example', 'https://www.google.com'),
#     View('Debug-Info', 'https://wiki.samsul.web.id'), ))

app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html',
    name=os.environ.get('USER_NAME'),
    facebook_url=os.environ.get('FACEBOOK_URL'),
    alamat=os.environ.get('ALAMAT')
    )


if __name__ == '__main__':
    app.run(debug=True)
