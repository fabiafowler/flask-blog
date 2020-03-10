from flask import Flask, render_template
from application import app

#if the app is being run from the file rather than being imported, run the app 
if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')

#when this url is called, perform this function
