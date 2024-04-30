from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        	# Get form data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        ph = request.form['ph']
        dob = request.form['dob']
        dod = request.form['dod']
        district = request.form['District']
        bloodtype = request.form['Blood type']
         
        		# Save form data to database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('INSERT INTO donors (firstname, lastname, ph, dob, dod, district, bloodtype) VALUES (?, ?, ?, ?, ?, ?, ?)',(firstname, lastname, ph, dob, dod, district, bloodtype))
        conn.commit()
        conn.close()
    else:
        return render_template('register.html')
