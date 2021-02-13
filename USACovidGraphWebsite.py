from flask import Flask, redirect, url_for, render_template, request, session, flash
from USACovidGraphs import show_graph

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/select_states', methods=['POST', 'GET'])
def select_states():
    if request.method == 'POST':
        state_one = request.form['stateone']
        state_two = request.form['statetwo']
        show_graph(state_one, state_two)
        return render_template('viewing_graphs.html', state_one=state_one, state_two=state_two)
    else:
        return render_template('graphs.html')


@app.route('/total_deaths')
def total_deaths():
    return render_template('total_deaths.html')


if __name__ == '__main__':
    app.run(debug=True)
