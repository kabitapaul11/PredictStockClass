from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""

    LOG.info(f"Scaling Payload: {payload}")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = f"<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

# TO DO:  Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
    
    input looks like:
                      {
           "Operating Income":{  
      "0":5.186600e+09
   },
   "Net Income":{  
      "0":3.751480e+09
   },
   "EPS":{  
      "0":2.56
   },
   "EPS Diluted":{  
      "0":2.53
   },
   "EBIT Margin":{  
      "0":0.1974
   },
   "EBIT":{  
      "0":5.189088e+09
   },
   "Consolidated Income":{  
      "0":3.828060e+09
   },
   "Earnings Before Tax Margin":{  
      "0":0.1599
   },
   "Net Profit Margin":{  
      "0":0.1241
   },
   "Weighted Average Shares Diluted Growth":{  
      "0":-0.0305
   }
    result looks like:
    { "prediction": [ 36.22848783701204 ] }
    """


    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"inference payload DataFrame: {inference_payload}")
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    clf = joblib.load("stock_final_project_prediction.joblib")
    app.run(host='0.0.0.0', port=8080, debug=True)
