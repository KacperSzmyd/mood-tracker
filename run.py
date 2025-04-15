from app import create_app, db
import os

app = create_app()
app.static_folder = os.path.join(os.path.dirname(__file__), "static")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
