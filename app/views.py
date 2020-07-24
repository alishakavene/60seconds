from flask import render_template
import os
from app import app


@app.route('/')
def root():
     title = 'Home - Welcome to 60seconds pitch'
     return render_template('index.html', title =title)





    
   

