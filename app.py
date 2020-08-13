from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)

@app.route('/')
def front():
   return render_template('front.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      sia_obj=SentimentIntensityAnalyzer()
      s_dic=sia_obj.polarity_scores(result)
      sentiment=None
      if s_dic['compound']>=1:
              sentiment='positive'
      elif s_dic['compound']<=1:
          sentiment='negative'
      else:
          sentiment='neutral'
      return render_template("result.html",sentiment = sentiment)

if __name__ == '__main__':
   app.run(debug = True)