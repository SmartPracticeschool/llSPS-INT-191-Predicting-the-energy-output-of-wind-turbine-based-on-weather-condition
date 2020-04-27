#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,request,render_template
from keras.models import load_model
import numpy as np
global model, graph
import tensorflow as tf
graph =  tf.get_default_graph()
model = load_model('project.h5')
app = Flask(__name__)
@app.route('/')#when even the browser finds localhost:5000 then
def home():#excecute this function
    return render_template('index.html')#this function is returing the index.html file
@app.route('/login', methods =['POST']) #when you click submit on html page it is redirection to this url
def login():#as soon as this url is redirected then call the below functionality
    a = request.form['a']
    b = request.form['b']
    a = (float(a)-1307.684332)/1312.459242  #rescaling the user i/p(std scaling)
    b = (float(b)-7.557952)/4.227166
    
    total = [[a,b]]

    with graph.as_default():
        ypred = model.predict(np.array(total))
        y = ypred[0][0]
        print(ypred)
    # from html page what ever the text is typed  that is requested from the form functionality and is stored in a name variable
    return render_template('index.html' ,abc = y)#after typing the name show this name on index.html file where we have created a varibale abc
if __name__ == '__main__':
    app.run(debug = True)

