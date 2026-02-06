from flask import Flask, request
from flask_restx import Api, Resource
from flask_restx import reqparse

from analysis import get_student_insights

from db_config import get_connection
from analysis import (
    fetch_all_performance,
    fetch_weak_subjects,
    fetch_student_performance,
    fetch_top_performers
)

from backend.db_config import get_connection

app = Flask(__name__)
api = Api(
    app,
    title="Student Performance Analyzer API",
    version="1.0",
    description="APIs for analyzing student academic performance"
)

ns = api.namespace(
    "analytics",
    description="Student performance analytics endpoints"
)

weak_parser = reqparse.RequestParser()
weak_parser.add_argument(
    "threshold",
    type=int,
    default=40,
    help="Percentage below which subjects are considered weak",
    location="args"
)



# ---------- BASIC CHECK ----------

@app.route("/", methods=["GET"])
def home():
    return {
        "message": "Student Performance Analyzer API is running"
    }


# ---------- GET APIs ----------

@api.route("/performance")
class Performance(Resource):
    def get(self):
        return fetch_all_performance()


@ns.route("/weak-subjects")
class WeakSubjects(Resource):
    @ns.expect(weak_parser)
    def get(self):
        args = weak_parser.parse_args()
        threshold = args["threshold"]

        data = fetch_weak_subjects(threshold)
        for row in data:
            row["avg_percentage"] = float(row["avg_percentage"])

        return data




@app.route("/student-performance", methods=["GET"])
def student_performance():
    name = request.args.get("name")

    if not name:
        return {"error": "Student name is required"}, 400

    data = fetch_student_performance(name)
    return data


@app.route("/top-performers", methods=["GET"])
def top_performers():
    limit = request.args.get("limit", default=3, type=int)
    data = fetch_top_performers(limit)
    return data


# ---------- POST APIs (ADD DATA ONLY WHEN CALLED) ----------

@app.route("/add-student", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data.get("name")
    student_class = data.get("class")
    section = data.get("section")

    if not name or not student_class:
        return {"error": "Name and class are required"}, 400

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

    return {"message": "Student added successfully"}, 201

@app.route("/insights/student", methods=["GET"])
def student_insights():
    name = request.args.get("name")

    if not name:
        return {"error": "Student name is required"}, 400

    insights = get_student_insights(name)

    if not insights:
        return {"error": "No data found for this student"}, 404

    return insights



# ---------- RUN SERVER ----------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


