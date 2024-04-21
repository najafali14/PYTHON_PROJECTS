from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=('GET','POST'))
def home():
  if request.method == 'POST':
    weight = request.form['weight']
    height = request.form['height']
    bmi = float(weight)/float(height)**2
    return render_template('home.html',bmi=bmi)

  return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
