import os
from flask import Flask, flash, redirect, render_template, request, session, abort, redirect, url_for, g, jsonify

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

print(os.environ['APP_SETTINGS'])

port = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    error = None
    return render_template("index.html", error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)