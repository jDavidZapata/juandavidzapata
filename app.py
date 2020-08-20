import os
from flask import Flask, flash, redirect, render_template, request, session, abort, redirect, url_for, g, jsonify

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

@app.route('/')
def home():
    error = None
    return render_template("index.html", error=error)

if __name__ == '__main__':
    app.run()