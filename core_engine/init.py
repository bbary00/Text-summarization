from flask import Flask, render_template,request
from transforming1 import summarize
app = Flask(__name__)

@app.route('/')
def complete():
   return render_template('index.html')

@app.route('/', methods = ['POST'])
def summary():
   text=request.json.get("text")
   sentences=request.json.get("sentences")
   percent=request.json.get("percent")
   summ = summarize(text, percent)
   return(summ, 201)

if __name__ == '__main__':
   app.run(debug = True)