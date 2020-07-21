from flask import render_template
import os
from app import app


@app.route('/')
def root():
     return render_template('pitch.html')
 

