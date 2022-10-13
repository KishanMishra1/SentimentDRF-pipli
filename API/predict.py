from joblib import load

class Predict:
    vector = load('API/vectors.joblib')
    models = load('API/model.joblib')

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