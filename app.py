from flask import Flask, render_template, request, redirect, url_for
from database import add_patient as db_add_patient, get_patient, get_patients, create_table, get_patients_by_disease

app = Flask(__name__)

# Create database table when app starts
def initialize_database():
    create_table()

# Call this function directly when app starts
with app.app_context():
    initialize_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():  
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        disease_type = request.form['disease']
        db_add_patient(name, age, blood_group, disease_type)  # Use the renamed import
        return redirect(url_for('index'))
    return render_template('add_patient.html')

@app.route('/patient/<int:patient_id>')
def patient_details(patient_id):
    patient_data = get_patient(patient_id)
    if patient_data:
        patient = {
            'id': patient_data[0],
            'name': patient_data[1],
            'age': patient_data[2],
            'blood_group': patient_data[3],
            'disease_type': patient_data[4]
        }
        return render_template('patient_details.html', patient=patient)
    return redirect(url_for('index'))

@app.route('/reports', methods=['GET'])
def reports():
    disease_query = request.args.get('disease', '')
    
    if disease_query:
        patients_data = get_patients_by_disease(disease_query)
    else:
        patients_data = get_patients()
        
    patients = []
    for p in patients_data:
        patients.append({
            'id': p[0],
            'name': p[1],
            'age': p[2],
            'blood_group': p[3],
            'disease_type': p[4]
        })
    return render_template('reports.html', patients=patients, disease_query=disease_query)
@app.route('/reset', methods=['POST'])
def reset():
    reset_database()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
