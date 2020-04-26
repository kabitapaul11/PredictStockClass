#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{  
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
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
