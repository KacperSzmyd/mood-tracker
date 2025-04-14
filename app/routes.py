from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_required, current_user
from datetime import datetime
import matplotlib.pyplot as plt
import io
import base64
from .models import Mood, db

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


@main.route("/chart")
@login_required
def chart():
    moods = Mood.query.filter(Mood.user_id == current_user.id).order_by(Mood.date).all()
    if not moods:
        flash("No mood data to show yet.")
        return redirect(url_for("main.index"))

    dates = [m.date.strftime("%Y-%m-%d %H:%M") for m in moods]
    values = list(range(1, len(moods) + 1))

    plt.figure(figsize=(12, 6))
    plt.plot(dates, values, marker="o", linestyle="-", color="royalblue")
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.title("Mood Tracker", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Mood Entry Number", fontsize=12)
    plt.tight_layout(pad=2.0)

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template("chart.html", plot_url=plot_url)
