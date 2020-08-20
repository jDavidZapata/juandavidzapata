from flask import Flask, flash, redirect, render_template, request, session, abort, redirect, url_for, g, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    error = None
    return render_template("index.html", error=error)