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
    owner_name = request.form['vehicle_owner']
    vehicle_name = request.form['vehicle_name']
    vehicle_number = request.form['vehicle_number']
    entry_date = request.form['entry_date']
    exit_date = request.form['exit_date']

    cursor = db.cursor()
    cursor.execute("SELECT * FROM vehicles WHERE vehicle_number = %s", (vehicle_number,))
    existing_vehicle = cursor.fetchone()

    if existing_vehicle:
        message = "Vehicle number already exists"
        cursor.close()  # Close the cursor before returning
        return render_template('index.html', message=message)
    else:
        cursor.close()  # Close the cursor before executing another query
        cursor = db.cursor()  # Reopen the cursor
        cursor.execute("INSERT INTO vehicles (owner_name, vehicle_name, vehicle_number, entry_date, exit_date) VALUES (%s, %s, %s, %s, %s)", (owner_name, vehicle_name, vehicle_number, entry_date, exit_date))
        db.commit()
        cursor.close()
        return render_template('sub.html')




if __name__ == '__main__':
    app.run(debug=True)
