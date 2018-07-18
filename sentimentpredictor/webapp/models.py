
import pickle
class Mlmodel:
    def __init__(self, model, vector):
        self.model=model
        self.vector=vector

    def get_model_type(self):
        print("Model is : {}".format(type(self.model)))

    def get_vector_type(self):
        print("Vector is : {}".format(type(self.vector)))

    def get_predictions(self, features):
        sentiment_dict={1: 'Positive', 0: 'Negative'}
        features_transformed=self.vector.transform(features)
        predictions=self.model.predict(features_transformed)
        prediction_labels=list([])
        for pred in predictions:
            prediction_labels.append(sentiment_dict[pred])
        return(predictions,prediction_labels)
