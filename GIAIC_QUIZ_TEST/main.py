from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')
@app.route('/step00_helloworld', methods=['POST','GET'])
def step00_helloworld():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')
    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "A", "C", "B", "C", "A", "A", "A", "D", "B"]
    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step00_helloworld.html', marks=marks,ql=ql)

@app.route('/step00a_json_objects',methods=['POST','GET'])
def step00a_json_objects():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["A", "A", "A", "D", "C", "A", "B", "C", "C", "C"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step00a_json_objects.html',marks=marks,ql=ql)
  
@app.route('/step00b_syntax_error',methods=['POST','GET'])
def step00b_syntax_error():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["A", "A", "B", "A", "A", "B", "A", "D", "B", "D"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step00b_syntax_error.html',marks=marks,ql=ql)

@app.route('/step00c_type_error',methods=['POST','GET'])
def step00c_type_error():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["D", "A", "B", "D", "D", "B", "A", "B", "D", "A"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step00c_type_error.html',marks=marks,ql=ql)

@app.route('/step00d_assignability_error',methods=['POST','GET'])
def step00d_assignability_error():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["D", "A", "A", "B", "D", "D", "D", "A", "C", "C"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step00d_assignability_error.html',marks=marks,ql=ql)

@app.route('/step01_strong_typing',methods=['POST','GET'])
def step01_strong_typing():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "B", "D", "B", "C", "B", "C", "C", "C", "B"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step01_strong_typing.html',marks=marks,ql=ql)

@app.route('/step02_const_let',methods=['POST','GET'])
def step02_const_let():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["A", "D", "C", "D", "B", "D", "C", "B", "C", "A"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step02_const_let.html',marks=marks,ql=ql)

@app.route('/step03a_modules',methods=['POST','GET'])
def step03a_modules():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "B", "B", "D", "B", "B", "B", "C", "A", "A"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step03a_modules.html',marks=marks,ql=ql)

@app.route('/step03b_native_ECMAScript_modules',methods=['POST','GET'])
def step03b_native_ECMAScript_modules():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["C", "B", "C", "B", "B", "D", "D", "D", "A", "A"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step03b_native_ECMAScript_modules.html',marks=marks,ql=ql)

@app.route('/step03c_import_inquirer_ECMAScript_module',methods=['POST','GET'])
def step03c_import_inquirer_ECMAScript_module():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["A", "C", "A", "A", "A", "B", "A", "B", "A", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step03c_import_inquirer_ECMAScript_module.html',marks=marks,ql=ql)

@app.route('/step03d_chalk',methods=['POST','GET'])
def step03d_chalk():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "A", "B", "C", "B", "C", "A", "C", "C", "B"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step03d_chalk.html',marks=marks,ql=ql)

@app.route('/step04_unions_literals',methods=['POST','GET'])
def step04_unions_literals():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "B", "C", "D", "C", "A", "B", "B", "A", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step04_unions_literals.html',marks=marks,ql=ql)

@app.route('/step05a_objects',methods=['POST','GET'])
def step05a_objects():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "A", "A", "A", "B", "A", "A", "A", "A", "C"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step05a_objects.html',marks=marks,ql=ql)

@app.route('/step05b_object_aliased',methods=['POST','GET'])
def step05b_object_aliased():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["A", "A", "A", "A", "B", "A", "A", "A", "A", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step05b_object_aliased.html',marks=marks,ql=ql)

@app.route('/step05c_structural_typing_object_literals',methods=['POST','GET'])
def step05c_structural_typing_object_literals():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "A", "D", "A", "A", "A", "A", "A", "A", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step05c_structural_typing_object_literals.html',marks=marks,ql=ql)

@app.route('/step05d_nested_objects',methods=['POST','GET'])
def step05d_nested_objects():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "B", "A", "B", "B", "C", "B", "A", "D", "B"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step05d_nested_objects.html',marks=marks,ql=ql)

@app.route('/step05e_intersection_types',methods=['POST','GET'])
def step05e_intersection_types():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["A", "A", "C", "C", "B", "C", "D", "A", "C", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step05e_intersection_types.html',marks=marks,ql=ql)

@app.route('/step05f_any__unknown_never_types',methods=['POST','GET'])
def step05f_any__unknown_never_types():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["C", "B", "D", "C", "D", "C", "D", "A", "A", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step05f_any__unknown_never_types.html',marks=marks,ql=ql)

@app.route('/step06_explict_casting',methods=['POST','GET'])
def step06_explict_casting():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["C", "D", "A", "B", "C", "A", "A", "B", "B", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step06_explict_casting.html',marks=marks,ql=ql)

@app.route('/step07a_enum',methods=['POST','GET'])
def step07a_enum():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "C", "C", "C", "A", "A", "C", "A", "A", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step07a_enum.html',marks=marks,ql=ql)

@app.route('/step07b_const_enum',methods=['POST','GET'])
def step07b_const_enum():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "D", "C", "A", "D", "D", "B", "B", "D", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step07b_const_enum.html',marks=marks,ql=ql)

@app.route('/step08_arrays',methods=['POST','GET'])
def step08_arrays():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ['B', 'B', 'B', 'A', 'C', 'A', 'A', 'D', 'A', 'B']

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step08_arrays.html',marks=marks,ql=ql)

@app.route('/step09a_functions',methods=['POST','GET'])
def step09a_functions():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A"]

    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step09a_functions.html',marks=marks,ql=ql)

@app.route('/step09b_function_optional_parameter',methods=['POST','GET'])
def step09b_function_optional_parameter():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')
    

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["A", "A", "A", "A", "A", "A", "B", "C", "B", "D"]
    
    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step09b_function_optional_parameter.html',marks=marks,ql=ql)

@app.route('/step09c_function_default_parameter',methods=['POST','GET'])
def step09c_function_default_parameter():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "C", "C", "A", "C", "A", "C", "B", "A", "D"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step09c_function_default_parameter.html',marks=marks,ql=ql)

@app.route('/step09d_function_rest_parameter',methods=['POST','GET'])
def step09d_function_rest_parameter():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["C", "A", "B", "B", "A", "C", "C", "D", "A", "A"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step09d_function_rest_parameter.html',marks=marks,ql=ql)

@app.route('/step09e_async',methods=['POST','GET'])
def step09e_async():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "C", "A", "A", "B", "B", "C", "B", "B", "C"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step09e_async.html',marks=marks,ql=ql)

@app.route('/step09f_function_overloads',methods=['POST','GET'])
def step09f_function_overloads():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "B", "C", "A", "B", "C", "B", "D", "B", "B"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step09f_function_overloads.html',marks=marks,ql=ql)

@app.route('/step10_tuples',methods=['POST','GET'])
def step10_tuples():
  ql = [ ]
  marks = 0
  if request.method == 'POST':
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    q6 = request.form.get('q6')
    q7 = request.form.get('q7')
    q8 = request.form.get('q8')
    q9 = request.form.get('q9')
    q10 = request.form.get('q10')
    name = request.form.get('name')

    ql = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,name]
    correct_answers = ["B", "A", "D", "A", "B", "A", "C", "B", "B", "B"]


    for i in range(len(correct_answers)):
      if ql[i] == correct_answers[i]:
          marks += 5
  return render_template('step10_tuples.html',marks=marks,ql=ql)


if __name__ == '__main__':
  app.run()
