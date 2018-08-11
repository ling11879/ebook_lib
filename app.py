from flask import Flask, render_template

app = Flask(__name__)


@app.route('/dashboard')
def index():

    return render_template('dashboard.html', title='Dashboard')


if __name__ == '__main__':
    app.run()
