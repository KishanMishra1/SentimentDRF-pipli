from joblib import load

class Predict:
    vector = load('/Users/kishanmishra/Desktop/Sentiment-DRP/Main/API/vectors.joblib')
    models = load('/Users/kishanmishra/Desktop/Sentiment-DRP/Main/API/model.joblib')

    def predict(self,a):
        text = [a['String']]
        #print(type(text))
        vec = self.vector.transform(text)
        prediction = self.models.predict(vec)
        prediction = int(prediction)

        if prediction > 0:
            prediction = "Positive"
        else:
            prediction = "Negative"
        return prediction