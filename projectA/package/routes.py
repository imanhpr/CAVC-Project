from flask import Blueprint , flash , redirect , url_for , render_template , request , jsonify
from flask_login import login_required , current_user
from projectA.forms import Package_form
from hashlib import md5
from projectA.models import Package 
from projectA import db

package_Blueprint = Blueprint('package_Blueprint',__name__)



@package_Blueprint.route('/package', methods=['POST', 'GET'])
@login_required
def package_view():
    form = Package_form()
    md5()
    if form.validate_on_submit():
        package_hash_var = f'{current_user.username} - {form.package_name.data}'
        new_package = Package(
            package_name=form.package_name.data,
            package_hash=md5(package_hash_var.encode("utf-8")).hexdigest(),
            current_version=form.c_version.data,
            force_version=form.f_version.data,
            username_id=current_user.id,
        )
        db.session.add(new_package)
        db.session.commit()
        flash('New Package Created !',category='success')
        return redirect(url_for('package_Blueprint.manage_package_view'))
    return render_template('package.html', form=form)


@package_Blueprint.route('/package/<path:package_hash_url>')
def package_hash_get(package_hash_url):
    try:
        package = Package.query.filter_by(
            package_hash=package_hash_url).first()
    except:
        return jsonify(error='package_Blueprint not found')

    if request.args.to_dict() == dict():
        return jsonify(
        package_name=package.package_name,
        current_version=package.current_version,
        force_version=package.force_version
    ) ############ need to try except block  ###################
    else:
        if request.args.get('client_version'):
            try:
                client_version = int(request.args.get('client_version'))
            except:
                return jsonify(error='client_version must be integer value')

            if package.current_version == client_version:
                available_update = False
                force_update = False
            elif package.force_version >= client_version:
                available_update = True
                force_update = True
            elif package.force_version < client_version and package.current_version > client_version:
                available_update = True
                force_update = False
            else:
                return jsonify(error='invalid cliant version')
            return jsonify(
                package_name=package.package_name,
                current_version=package.current_version,
                force_version=package.force_version,
                available_update=available_update,
                force_update=force_update
            )
        else:
            return jsonify(error='arg not found !')
    


@package_Blueprint.route('/dashboard')
@login_required
def dashboard_view():
   return render_template('base_user_dashboard.html')


@package_Blueprint.route('/managepackage')
@login_required
def manage_package_view():
    user_packages = Package.query.filter_by(username_id=current_user.id).all()
    return render_template('manage_package.html', user_packages=user_packages)

@package_Blueprint.route('/managepackage/edit/<string:package_hash_url>', methods = ['POST','GET'])
@login_required
def edit_package(package_hash_url):
    package = Package.query.filter_by(package_hash= package_hash_url ,username_id=current_user.id).first_or_404()
    form = Package_form()
    if form.validate_on_submit():
        package.package_name = form.package_name.data
        package.current_version = form.c_version.data
        package.force_version = form.f_version.data
        db.session.commit()
        flash('package updated !', category='success')
        return redirect(url_for('package_Blueprint.manage_package_view'))
    form.package_name.data = package.package_name
    form.c_version.data = package.current_version
    form.f_version.data = package.force_version
    return render_template('package.html' ,form=form)
   