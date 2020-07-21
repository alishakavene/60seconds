from flask import Flask, render_template
import os
app = Flask(__name__)



@app.route('/')
def root():
     return render_template('pitch.html', data=pitch_data)

     