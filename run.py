from app import create_app
import os

app = create_app(static_folder="app/static")
app.static_folder = os.path.join(os.path.dirname(__file__), "static")

if __name__ == "__main__":
    app.run()
