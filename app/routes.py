from flask import Blueprint, render_template, redirect, request, flash
from flask_login import login_required, current_user
from .models import Mood, db
from datetime import datetime

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        mood = request.form["mood"].strip()
        if not mood:
            flash("Mood cannot be empty.")
        else:
            new_entry = Mood(mood=mood, date=datetime.now(), user_id=current_user.id)
            db.session.add(new_entry)
            db.session.commit()
            flash("Mood saved successfully!")
            return redirect("/")

    entries = (
        Mood.query.filter(Mood.user_id == current_user.id)
        .order_by(Mood.date.desc())
        .all()
    )
    return render_template("index.html", entries=entries)
