import os # فراخوانی کتاب خانه برای کار به سطح پایین تر سیستم عامل
from flask import Flask # شی اصلی فلسک باری بارگزاری فایل های حیاطی پروژه
from flask_sqlalchemy import SQLAlchemy # کتاب خانه برای استفاده  orm
from flask_migrate import Migrate # کتاب خانه ای برای راخت تر کاردن کار با orm
from flask_login import LoginManager # کتاب خانه ای برای مدیریت کاربران در دیتابیس
from flask_bcrypt import Bcrypt # کتاب خانه ای برای رمز گزاری بعضی از اطلاعات مهم مربوط به کاربران


app = Flask(__name__) # بارگزاری شی اصلی مربوط به کل پروژه با توجه به نام پروژه

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # آدرس مربوط به پروژه در سطح فایل سیستم برای مدیریت بهتر فایل های استاتیک

app.config['SECRET_KEY'] = 'sdaw' # کلمه کلیدی برای رمزگزاری اطلاعت مهم مربوط به کوکی ها و سشن ها که برای پروژه اصلی باید تغییر کند.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(BASE_DIR, 'CAVC_Project.db') # اطلاعات مربوط به دیتابیس.
db = SQLAlchemy(app) # ایجاد شی مربوط به دیتابیس برای کار کردن با orm

migrate = Migrate(app, db) # ایجاد شی مربوط به مایگریت برای راحت تر کردن کار با دیتابیس

login_manager = LoginManager(app) # ایجاد شی برای مدیریت کتاب خانه مربوط به کاربران وارد شده در وب سایت
bcrypt = Bcrypt(app) # ایجاد شی مربوط به امنیت کاربران

# ایمپورت کردن تابع های ویو برای ثبت در پروژه اصلی و شناسایی آنها
from .index.routes import index_Blueprint
from .users.routes import users
from .package.routes import package_Blueprint

app.register_blueprint(index_Blueprint)
app.register_blueprint(users)
app.register_blueprint(package_Blueprint)
