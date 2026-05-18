from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import db

app = Flask(__name__)
CORS(app)

students = db.students
attendance = db.attendance


@app.route('/')
def home():

    return send_from_directory('.', 'index.html')


@app.route('/style.css')
def serve_css():

    return send_from_directory('.', 'style.css')


@app.route('/script.js')
def serve_js():

    return send_from_directory('.', 'script.js')


@app.route('/backgroundimgschool.png')
def serve_image():

    return send_from_directory('.', 'backgroundimgschool.png')


# ADD STUDENT
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


# MARK ATTENDANCE
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


# GET STUDENTS
@app.route('/get_students', methods=['GET'])
def get_students():

    student_data = list(
        students.find({}, {"_id": 0})
    )

    return jsonify(student_data)


# GET ATTENDANCE
@app.route('/get_attendance', methods=['GET'])
def get_attendance():

    attendance_data = list(
        attendance.find({}, {"_id": 0})
    )

    return jsonify(attendance_data)


if __name__ == '__main__':
    app.run()
