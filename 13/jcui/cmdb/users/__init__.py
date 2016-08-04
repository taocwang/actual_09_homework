#enconding: utf-8


from flask import Flask
from fams import bp
from assets import app as assets

app = Flask(__name__)
app.secret_key = 'asdasd2342tdasfdasfasdasds'

app.register_blueprint(bp)
app.register_blueprint(assets)

import viers