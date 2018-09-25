from flask import Flask, render_template, send_from_directory

app = Flask(__name__,static_url_path='/static')

app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return "error", 404

from app.api.controllers import api as api_controller
app.register_blueprint(api_controller)