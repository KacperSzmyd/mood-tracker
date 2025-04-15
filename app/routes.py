from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    flash,
    url_for,
    Response,
)
from flask_login import login_required, current_user
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import csv
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
    values = [m.mood for m in moods]

    colors = []
    for mood in values:
        if mood <= 3:
            colors.append("red")
        elif mood <= 6:
            colors.append("orange")
        else:
            colors.append("green")

    now = datetime.now()
    week_ago = now - timedelta(days=7)
    last_week_moods = [m.mood for m in moods if m.date >= week_ago]

    avg = sum(last_week_moods) / len(last_week_moods) if last_week_moods else None

    plt.figure(figsize=(10, 5))
    plt.scatter(dates, values, c=colors, s=80)
    plt.xticks(rotation=45)
    plt.ylim(0, 10.5)
    plt.title("Mood Tracker")
    plt.xlabel("Date")
    plt.ylabel("Mood (1–10)")
    plt.tight_layout(pad=2)

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template("chart.html", plot_url=plot_url, avg=avg)


@main.route("/export")
@login_required
def export():
    moods = Mood.query.filter(Mood.user_id == current_user.id).order_by(Mood.date).all()

    if not moods:
        flash("No mood data to export.")
        return redirect(url_for("main.index"))

    def generate():
        data = [["Date", "Mood (1-10)"]]
        for item in moods:
            data.append([item.date.strftime("%Y-%m-%d %H:%M"), item.mood])
        output = io.StringIO()
        writer = csv.writer(output)

        for row in data:
            writer.writerow(row)

        return output.getvalue()

    return Response(
        generate(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=moods.csv"},
    )
