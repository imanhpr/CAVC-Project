from projectA import db, login_manager
from flask_login import UserMixin

# تابعی برای بدست اوردن شی کاربر با استفاده از ایدی کاربر.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
# حدول مربوبط به کاربران در دیتابیس
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# جدول مربوط به پکیج ها در دیتابیس.
class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    package_name = db.Column(db.String(100), nullable=False)
    package_hash = db.Column(db.String(120), unique=True, nullable=False)
    current_version = db.Column(db.Integer, nullable=True)
    force_version = db.Column(db.Integer,nullable=True)

    username_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_detail = db.relationship('User',backref=db.backref('package', lazy=True))
