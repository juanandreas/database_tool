from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database=os.getenv("POSTGRES_DB", "mydatabase"),
        user=os.getenv("POSTGRES_USER", "myuser"),
        password=os.getenv("POSTGRES_PASSWORD", "mypassword")
    )
    return conn

@app.route("/")
def home():
    return jsonify({"message": "Flask Server is Running!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
