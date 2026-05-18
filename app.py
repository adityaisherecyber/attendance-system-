from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db

app = Flask(__name__)
CORS(app)

students = db.students

attendance = db.attendance


@app.route('/')
def home():

    return jsonify({
        "message": "Attendance Server Running"
    })


@app.route('/add_student', methods=['POST'])
def add_student():

    data = request.json

    student = {

        "name": data['name'],

        "roll_no": data['roll_no'],

        "class": data['class']
    }

    students.insert_one(student)

    return jsonify({
        "message": "Student Added Successfully"
    })


@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():

    data = request.json

    attendance_data = {

        "student_name": data['student_name'],

        "roll_no": data['roll_no'],

        "class": data['class'],

        "status": data['status']
    }

    attendance.insert_one(attendance_data)

    return jsonify({
        "message": "Attendance Marked Successfully"
    })


@app.route('/get_students', methods=['GET'])
def get_students():

    student_data = list(
        students.find({}, {"_id": 0})
    )

    return jsonify(student_data)


@app.route('/get_attendance', methods=['GET'])
def get_attendance():

    attendance_data = list(
        attendance.find({}, {"_id": 0})
    )

    return jsonify(attendance_data)


if __name__ == '__main__':

    app.run(debug=True)