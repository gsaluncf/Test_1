from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    dict = request.form
    for key in dict:
        print ( key  + ' ' +dict[key])
    return render_template('suduko.html')


@app.route('/')
def hello_world():  # put application's code here
    suduko_numbers = []
    for i in range (81):
        suduko_numbers.append(i)
    return render_template('suduko.html', values=suduko_numbers)


if __name__ == '__main__':
    app.run(debug=True)
