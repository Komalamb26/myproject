from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage
students = []

# 🔹 Step 7: Home route (for testing server)
@app.route('/')
def home():
    return "Server is working!"

# 🔹 POST: Add student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    # Safety check (optional but good)
    if not data:
        return jsonify({"message": "No data provided"}), 400

    student = {
        "id": data.get("id"),
        "name": data.get("name"),
        "age": data.get("age"),
        "course": data.get("course")
    }

    students.append(student)

    return jsonify({
        "message": "Student added successfully",
        "student": student
    }), 201


# 🔹 GET: All students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


# 🔹 GET: Single student
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


# 🔹 Run server (slightly improved)
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)