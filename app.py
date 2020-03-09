from flask import Flask, render_template


#This tells you where the app is being called from, in this case 'name'
app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home Page")
#using Jinja to render home file into html file

#when this url is called, perform this function
@app.route('/about')
def about():
    return render_template('about.html)', title ="About Page")
