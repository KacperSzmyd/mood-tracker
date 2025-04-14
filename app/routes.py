from flask import Blueprint, render_template, redirect, request
from .models import Mood, db
from datetime import datetime

main = Blueprint("main", __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mood = request.form['mood']
        new_entry = Mood(mood=mood, date=datetime.now())
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/')
    
    entries = Mood.query.order_by(Mood.date.desc()).all()
    return render_template("index.html", entries=entries)