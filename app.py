from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'




@app.route('/', methods=['GET', 'POST'])
def index():
    if 'notes' not in session:
        session['notes'] = []

    if request.method == 'POST':
        note = request.form.get('note')
        notes = session['notes'].copy()
        notes.append(note)
        session['notes'] = notes
    return render_template('home.html', notes=session['notes'])

if __name__ == '__main__':
    app.run(debug=True)
