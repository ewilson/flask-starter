from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello_world():
    name = request.args.get('name')
    name = name if name else 'World'
    return render_template('hello.html', name=name)


@app.route('/goodbye/<user>')
def goodbye(user):
    return render_template('bye.html', user=user)


@app.route('/form-example', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        return render_template('form.html', info={'firstname': first_name, 'lastname': last_name})


if __name__ == '__main__':
    app.run(debug=True)
