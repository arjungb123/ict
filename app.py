from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'welcome to flaskkkkkk'
@app.route('/home')
def home():
    return 'welcome to home'
@app.route('/home/about')
def about():
    return 'about'
if(__name__=='__main__'):
    app.run(debug=True)