from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def Home():
  sp = None
  result = 0
  
  if request.method=='POST':
    sp = request.form.get('options')
    if sp == 'op3':
      result += 5
  if request.method=='POST':

    sp2 = request.form.get('options2')
    if sp2 == 'op3':
      result += 5
    if request.method=='POST':
      sp3 = request.form.get('options3')
      if sp3 == 'op2':
        result += 5
    if request.method=='POST':
      sp4 = request.form.get('options4')
      if sp4 == 'op2':
        result += 5
    if request.method=='POST':
      sp5 = request.form.get('options5')
      if sp5 == 'op4':
        result += 5

    return render_template('index.html',data=result)
  else:
    pass
  return render_template('index.html')
if __name__ == '__main__':
  app.run(debug=True)
