from flask import Flask, jsonify, request
from db_config import get_connection
from analysis import (
    fetch_all_performance,
    fetch_weak_subjects,
    fetch_student_performance,
    fetch_top_performers
)

app = Flask(__name__)


# ---------- BASIC CHECK ----------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Student Performance Analyzer API is running"
    })


# ---------- GET APIs ----------

@app.route("/performance", methods=["GET"])
def get_performance():
    data = fetch_all_performance()
    return jsonify(data)


@app.route("/weak-subjects", methods=["GET"])
def weak_subjects():
    threshold = request.args.get("threshold", default=40, type=int)
    data = fetch_weak_subjects(threshold)
    return jsonify(data)


@app.route("/student-performance", methods=["GET"])
def student_performance():
    name = request.args.get("name")

    if not name:
        return jsonify({"error": "Student name is required"}), 400

    data = fetch_student_performance(name)
    return jsonify(data)


@app.route("/top-performers", methods=["GET"])
def top_performers():
    limit = request.args.get("limit", default=3, type=int)
    data = fetch_top_performers(limit)
    return jsonify(data)


# ---------- POST APIs (ADD DATA ONLY WHEN CALLED) ----------

@app.route("/add-student", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data.get("name")
    student_class = data.get("class")
    section = data.get("section")

    if not name or not student_class:
        return jsonify({"error": "Name and class are required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students (name, class, section)
    VALUES (%s, %s, %s);
    """
    cursor.execute(query, (name, student_class, section))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Student added successfully"}), 201


# ---------- RUN SERVER ----------

if __name__ == "__main__":
    app.run(debug=True)

