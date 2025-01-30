from flask import Flask
from routes.user_routes import user_bp
from db.database import get_db

app = Flask(__name__)

# //connecting to the database
db = get_db()

# //connect to routers
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)
