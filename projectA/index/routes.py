from flask import Blueprint , render_template
from flask_login import current_user

index_Blueprint = Blueprint('index_Blueprint',__name__)

@index_Blueprint.route("/")
def index():
    return render_template('land.html')