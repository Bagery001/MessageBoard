from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html.jinja2', messages=messages)

@app.route('/post/add/', methods=['POST'])
def add_post():
    message = request.form['message']
    timestamp = datetime.datetime.now()
    messages.append((message, timestamp))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)