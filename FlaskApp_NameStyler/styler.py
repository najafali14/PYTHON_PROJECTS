from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def Home():
  data = None
  if request.method=='POST':
    name = request.form.get('uname')
    
    color = request.form.get('uname1')
    color1 = color.lower()
    print(color1)
    data= [name,color1]
    
    return render_template('index.html', data=data)
  else:
    pass
  return render_template('index.html')
if __name__ == '__main__':
  app.run(debug=True)
