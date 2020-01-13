from flask import Blueprint , render_template
from flask_login import current_user

# ثبت بلوپرینت مربوط به بخش ایندکس برای مرتب کردن و استاندارد بودن پروژه
index_Blueprint = Blueprint('index_Blueprint',__name__)
# index view
# از این قسمت برای رندر کردن صفحه اصلی وب سایت استفاده میشود.
@index_Blueprint.route("/")
def index():
    return render_template('land.html')