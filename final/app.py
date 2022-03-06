#!/usr/bin/env python
# coding: utf-8

# In[5]:


import flask

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run()
    
import numpy as np
import pickle

model = pickle.load(open('D:/python/jupyter/H8_065/H8Deployment/model/model_regression.pkl', 'rb'))

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in flask.request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = {0: 'not placed', 1: 'placed'}

    return flask.render_template('main.html', prediction_text='Saleprice {} to predict'.format(output[prediction[0]]))

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




