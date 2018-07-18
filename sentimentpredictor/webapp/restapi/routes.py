from webapp.restapi import bp
from webapp.models import Mlmodel
from flask import current_app, jsonify, request
import pandas as pd

@bp.route('/predictmany', methods=['GET', 'POST'])
def predictmany():
    sentiment_dict={1: 'Positive', 0: 'Negative'}
    model=current_app.config['APPMODEL']
    try:
        test_data = request.get_json()
    except Exception as e:
        raise e
    else:
        test_df= pd.read_json(test_data, orient='records')
        predictions,prediction_labels=model.get_predictions(test_df['comment'])
        """
        print(predictions)
        print(prediction_labels)
        """
        test_df['prediction']=predictions
        test_df['prediction-label']=prediction_labels
        response=jsonify(predictions=test_df.to_json(orient="records"))
        response.status_code = 200
        return(response)
        """
        return "HELLO"
        """
