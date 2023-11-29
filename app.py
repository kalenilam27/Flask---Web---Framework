### Building Url Dynamically 
####Variable Rules And URL Building

from flask import Flask,redirect,url_for
import pandas

app=Flask(__name__)

@app.route('/')
def Welcome():
    return "Welcome to my youtube channel"

@app.route('/success/<int:score>')
def success(score):
     return "<html><body><h1> The result is passed </h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
     return 'The person has failed and marks are' + str(score)
          
     ### result checker
@app.route('/results/<int:marks>')
def results(marks):
     result=''
     if marks >=50:
          result='success'
     else:
               result='fail'
     return redirect(url_for(result,score=marks))


if __name__ == "__main__":
     app.run(debug=True)
