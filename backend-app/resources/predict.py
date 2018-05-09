from flask_restful import Resource, reqparse
import pandas as pd
import os


data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

class Predict(Resource):

    def get(self):
        # returns all the available models
        pass
    
    def post(self, name):
        # runs a model based on the input and returns the predictions
        pass