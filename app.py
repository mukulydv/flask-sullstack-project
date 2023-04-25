from flask import Flask, render_template , jsonify

app = Flask(__name__)

Jobs =[
    {'id':'Job1', 'title':'Full Stack Developer', 'location':'Amritapuri', 'salary':'Rs.15,00,000', 'mailId':'campus@am.amrita.edu'},
    {'id':'Job2', 'title':'Backend Developer', 'location':'Coimbatore','salary':'Rs.12,00,000' ,'mailId':'univhq@amrita.edu'},
    {'id':'Job3', 'title':'ML Engineer', 'location':'Bengaluru', 'salary':'Rs.20,00,000','mailId':'info@blr.amrita.edu'}
    
]

@app.route("/")
def hello_mukul():
    return render_template('home.html', 
                           jobs=Jobs,
                           company_name="Amrita")

@app.route("/api/jobs")
def get_jobs():
    return jsonify(jobs=Jobs)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

    
