from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
  if request.method=='POST':
    todo = request.form['todo']
    
    with open('data.csv','a') as todoData: # append data
      todoData.write(todo + '\n')
    with open('data.csv','r') as readTodo: # read data
      todo_list = readTodo.readlines()
  
    # print(todoData)
    todoData.close()

    return render_template('home.html',todo_list=todo_list)

  return render_template('home.html')
if __name__=='__main__':
  app.run(debug=True)
