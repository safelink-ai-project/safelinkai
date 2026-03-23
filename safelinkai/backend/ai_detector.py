import pickle

model = pickle.load(open("backend/model/phishing_model.pkl", "rb"))

def ai_scan(features):

    prediction = model.predict([features])

    return int(prediction[0])