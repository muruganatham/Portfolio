from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/internship')
def internship():
    return render_template('internship.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/skill')
def skill():
    return render_template('skill.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/achieve')
def achieve():
    return render_template('achieve.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
