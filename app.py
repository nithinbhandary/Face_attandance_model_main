from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
import subprocess
from mysql.connector import connection, Error
from datetime import datetime, date
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', selected_date='', no_data=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return render_template('index.html')
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

def create_connection():
    """ create a database connection to the MySQL database """
    try:
        conn = connection.MySQLConnection(user='root', password='',
                                          host='127.0.0.1', database='attendance')
        if conn.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/backhome')
def backhome():
    return render_template('index.html', selected_date='', no_data=False)

@app.route('/attendance_view')
def attendance_view():
    return render_template('attendance.html', selected_date='', no_data=False)

@app.route('/takeattendance')
def takeattendance():
    subprocess.run(["python", "attendance_taker.py"])
    return render_template('index.html', no_data=False)

@app.route('/add_student')
def add_student():
    subprocess.run(["python", "get_faces_from_camera_tkinter.py"])
    return render_template('index.html', no_data=False)

@app.route('/delete_student', methods=['POST'])
def delete_student():
    rollno = request.form.get('roll_no')
    name = request.form.get('sname')
    subprocess.run(["python", "delete_face.py", rollno, name])
    return render_template('remove.html', no_data=False, name='', roll_no='')

@app.route('/get_attendance_data')
def get_attendance_data():
    conn = create_connection()
    data = attendance_details()
    # formatted_data = [(row[0], str(row[1]), row[2].strftime('%Y-%m-%d'), row[3]) for row in data]
    

    formatted_data = [(row[0], str(row[1]), datetime.strptime(row[2], '%Y-%m-%d').strftime('%Y-%m-%d'), row[3]) for row in data]

    data_df = pd.DataFrame(formatted_data, columns=['name', 'time', 'date', 'roll_no'])

    cursor = conn.cursor()
    cursor.execute("SELECT count(name) as count FROM studentdetails")
    total_student = cursor.fetchone()[0]

    stcursor = conn.cursor()
    stcursor.execute("SELECT name, roll_no, COUNT(*) AS attendance FROM attendance GROUP BY name, roll_no;")
    all_day = stcursor.fetchall()

    cursorcount = conn.cursor()
    cursorcount.execute("SELECT COUNT(DISTINCT date) AS unique_dates_count FROM attendance")
    total_att = cursorcount.fetchone()[0]
    conn.close()

    total_records = total_student
    present_count = len(data_df)
    absent_count = total_records - present_count

    overall = {
        'present': present_count,
        'absent': absent_count
    }

    student_attendance = pd.DataFrame(all_day, columns=['name', 'roll_no', 'attendance']).groupby('name')['attendance'].mean() * 100 / total_att
    student_names = student_attendance.index.tolist()
    student_percentages = student_attendance.values.tolist()

    students = {
        'names': student_names,
        'attendance': student_percentages
    }

    return jsonify({'overall': overall, 'students': students})

@app.route('/get_today_attendance_data')
def get_today_attendance_data():
    attendance_data = attendance_details()
    # formatted_data = [(row[0], str(row[1]), row[2].strftime('%Y-%m-%d'), row[3]) for row in attendance_data]
    

    formatted_data = [(row[0], str(row[1]), datetime.strptime(row[2], '%Y-%m-%d').strftime('%Y-%m-%d'), row[3]) for row in attendance_data]

    today_attendance = {
        'students': {
            'names': [row[0] for row in formatted_data],
            'roll_no': [row[3] for row in formatted_data]
        }
    }

    return jsonify(today_attendance)

@app.route('/search_rollno')
def search_rollno():
    return render_template('remove.html', rollno='', name='', no_data=False)

@app.route('/search_rollno', methods=['POST'])
def search_student():
    rollno = request.form.get('rollno')
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM studentdetails WHERE roll_no = %s", (rollno,))
    name = cursor.fetchone()
    conn.close()

    if not name:
        return render_template('remove.html', roll_no='', name='', no_data=True)
    return render_template('remove.html', roll_no=rollno, name=name[0], no_data=False)

@app.route('/attendance', methods=['POST'])
def attendance():
    selected_date = request.form.get('selected_date')
    selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
    formatted_date = selected_date_obj.strftime('%Y-%m-%d')

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT roll_no, name, time FROM attendance WHERE date = %s", (formatted_date,))
    attendance_data = cursor.fetchall()
    conn.close()

    if not attendance_data:
        return render_template('attendance.html', selected_date=selected_date, no_data=True)
    return render_template('attendance.html', selected_date=selected_date, attendance_data=attendance_data)

def attendance_details():
    formatted_date = datetime.today().strftime('%Y-%m-%d')
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, time, date, roll_no FROM attendance WHERE date = %s", (formatted_date,))
    attendance_data = cursor.fetchall()
    conn.close()
    return attendance_data

@app.route('/classes')
def view_classes():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT class, COUNT(*) as total_students FROM studentdetails GROUP BY class")
    class_summaries = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('classes.html', class_summaries=class_summaries)

@app.route('/class/<class_name>')
def view_class_details(class_name):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
    SELECT 
        s.name, 
        s.roll_no,
        IFNULL((COUNT(a.date) / (SELECT COUNT(DISTINCT date) FROM attendance) * 100), 0) AS attendance
    FROM 
        studentdetails s
    LEFT JOIN 
        attendance a ON s.roll_no = a.roll_no
    WHERE 
        s.class = %s
    GROUP BY 
        s.name, s.roll_no
    """
    
    cursor.execute(query, (class_name,))
    class_details = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(class_details)

if __name__ == '__main__':
    app.run(debug=True)
