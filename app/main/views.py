from flask import render_template,request,redirect,url_for
from . import main


@main.route('/')
def root():
     title = 'Home - Welcome to 60seconds pitch'
     return render_template('index.html', title =title)





    
   

