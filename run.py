#! /usr/bin/env python

from flask import Flask
import os
import time
import datetime
from flask import render_template
from app import app

@app.route("/profile")
def profile():
  return render_template('profile.html', time=time_info())

def time_info():
  now = time.strftime("%a %d %b %Y")
  return now


from app import app

app.run(debug=True,host="0.0.0.0",port=8080)
