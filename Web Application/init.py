from flask import Flask, render_template, request, jsonify
from transforming import summarize
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/summarization', methods=['POST'])
def summary():
   text = request.form['text']
   sent = request.form['sentence']
   summ = summarize(text, sent)
   print(summ)
   return jsonify(summ)



if __name__ == '__main__':
	app.run(debug=True)