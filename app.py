from flask import Flask, render_template
from application import app

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')