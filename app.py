#app.py

#import Flask
from flask import Flask, render_template, request
#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/predict/', methods=['GET','POST'])
def predict():
    
    if request.method == "POST":
        
        #get form data
        sepal_length = request.form.get('sepal_length')
        sepal_width = request.form.get('sepal_width')
        petal_length = request.form.get('petal_length')
        petal_width = request.form.get('petal_width')
        
        
        return render_template('predict.html')
    pass
