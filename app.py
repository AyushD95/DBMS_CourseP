from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ayush@123",
    database="data_vehicle"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    vehicle_owner = request.form['vehicle_owner']
    vehicle_model = request.form['vehicle_model']
    vehicle_type = request.form['vehicle_type']
    vehicle_colour = request.form['vehicle_colour']
    vehicle_number = request.form['vehicle_number']
    parking_spot = request.form['parking_spot']
    purpose = request.form['purpose']
    entry_date = request.form['entry_date']
    entry_time = request.form['entry_time']
    exit_date = request.form['exit_date']
    exit_time = request.form['exit_time']


    cursor = db.cursor()  # Reopen the cursor
    cursor.execute("INSERT INTO vehicles (vehicle_owner,vehicle_model, vehicle_type, vehicle_colour, vehicle_number,parking_spot, purpose,  entry_date,entry_time, exit_date,exit_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (vehicle_owner,vehicle_model, vehicle_type, vehicle_colour, vehicle_number,parking_spot, purpose,  entry_date,entry_time, exit_date,exit_time))
    db.commit()
    cursor.close()
    return render_template('sub.html')




if __name__ == '__main__':
    app.run(debug=True)
