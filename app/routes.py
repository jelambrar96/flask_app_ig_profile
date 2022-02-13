import json

from flask import render_template, request, redirect, jsonify
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models import Entry, Account, Profile

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# select

@app.route('/index_entries')
def index_entries():
    entries = Entry.query.all()
    return render_template('index_entries.html', entries=entries)
    

@app.route('/index_accounts')
def index_accounts():
    accounts = Account.query.all()
    return render_template("index_accounts.html", accounts=accounts)


@app.route('/index_profiles')
def index_profiles():
    profiles = Profile.query.all()
    return render_template("index profiles.html", profiles=profiles)


# inserts

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if not title or description:
            entry = Entry(title = title, description = description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"


@app.route('/add_profile', methods=['POST'])
def add_profile():
    if request.method == 'POST':
        form = request.form
        profile = form.get('profile')
        is_active = str(form.get('is_active')) == "on"
        if profile:
            p = Profile(profile=profile, is_active=is_active, is_favorite=False)
            db.session.add(p)
            db.session.commit()
            return redirect('/index_profiles')
    return "of the jedi"


@app.route('/add_account', methods=["POST"])
def add_account():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        is_active = str(form.get('is_active')) == "on"
        if username and password:
            # p = Profile(profile=profile, is_active=is_active)
            account = Account(username=username, password=password, is_active=is_active)
            db.session.add(account)
            db.session.commit()
            return redirect('/index_accounts')
    return "of the jedi"

# ---------------------------------------------------------------------
# update
# ---------------------------------------------------------------------

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "of the jedi"

@app.route('/update', methods=['POST'])
def update():
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')
    return "of the jedi"


@app.route('/update_profile/<int:id>')
def update_profile_route(id):
    if not id or id != 0:
        entry = Profile.query.get(id)
        if entry:
            return render_template('update_profile.html', profile=entry)
    return "of the jedi"


@app.route('/update_profile_data/<int:id>', methods=['POST'])
def update_profile(id):
    if request.method == 'POST':
        form = request.form
        profile = form.get('profile')
        if profile and not id or id != 0:
            entry = Profile.query.get(id)
            if entry and entry.profile != profile:
                entry.profile = profile
                db.session.commit()
        return redirect('/index_profiles')
    return "of the jedi"


@app.route('/update_account/<int:id>')
def update_account_route(id):
    if not id or id != 0:
        entry = Account.query.get(id)
        if entry:
            return render_template('update_account.html', account=entry)
    return "of the jedi"

@app.route('/update_account_data/<int:id>', methods=['POST'])
def update_account(id):
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        print(id)
        if username and password and not id or id != 0:
            entry = Account.query.get(id)
            if entry and (entry.username != username or entry.password != password):
                entry.username = username
                entry.password = password
                db.session.commit()
        return redirect('/index_accounts')
    return "of the jedi"

# ---------------------------------------------------------------------
# delete 
# ---------------------------------------------------------------------

@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')
    return "of the jedi"

@app.route('/delete_profile/<int:id>')
def delete_profile(id):
    if not id or id != 0:
        entry = Profile.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/index_profiles')
    return "of the jedi"

@app.route('/delete/<int:id>')
def delete_account(id):
    if not id or id != 0:
        entry = Account.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/index_accounts')
    return "of the jedi"

# ---------------------------------------------------------------------
# turn
# ---------------------------------------------------------------------

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')
    return "of the jedi"

@app.route('/turn_profile/<int:id>')
def turn_profile(id):
    if not id or id != 0:
        entry = Profile.query.get(id)
        if entry:
            entry.is_active = not entry.is_active
            db.session.commit()
        return redirect('/index_profiles')
    return "of the jedi"

@app.route('/turn_account/<int:id>')
def turn_account(id):
    if not id or id != 0:
        entry = Account.query.get(id)
        if entry:
            entry.is_active = not entry.is_active
            db.session.commit()
        return redirect('/index_accounts')
    return "of the jedi"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"

# ---------------------------------------------------------------------

@app.route('/select_profiles')
def select_profiles():
    profiles = Profile.query.all()
    return jsonify(profiles)


@app.route('/select_accounts')
def select_accounts():
    accounts = Account.query.all()
    return jsonify(accounts)


@app.route('/api/add_profile', methods=['GET', 'POST'])
def insert_profile():
    print("init")
    try:
        print(request.data.decode())
        content = json.loads(request.data.decode())
    except json.JSONDecodeError:
        print("decode")
        return jsonify({"success": False }), 400
    
    print(content)

    if content is None:
        print("none")
        return jsonify({"success": False }), 400
    
    try:
        profile = content['profile']
    except KeyError:
        print("no profile found")
        return jsonify({"success": False }), 400

    is_active = bool(content["is_active"]) if "is_active" in content.keys() else False
    is_favorite = bool(content["is_favorite"]) if "is_favorite" in content.keys() else False

    temp_profile = Profile(profile=profile, is_active=is_active, is_favorite=is_favorite)
    
    try:
        db.session.add(temp_profile)
        db.session.commit()
    except IntegrityError as ie:
        return jsonify({"success": False, "message": str(ie) }), 400

    return jsonify({"success": True }), 200