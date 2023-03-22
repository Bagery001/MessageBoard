from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html.jinja2')

@app.route('/post/add/', methods=['POST'])
def add_post():
    content = request.form['content']
    if content:
        messages.append((datetime.now(), content))
    return redirect(url_for('index'))

@app.context_processor
def inject_messages():
    sorted_messages = sorted(messages, key=lambda x: x[0], reverse=True)
    return dict(messages=sorted_messages)

if __name__ == '__main__':
    app.run(debug=True)
