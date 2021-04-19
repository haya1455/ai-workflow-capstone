# IBM AI Enterprise Workflow Capstone
Files for the IBM AI Enterprise Workflow Capstone project. 

# directory
```
├── CAPSTONE.ipynb
├── Dockerfile
├── EDA.ipynb
├── README.md
├── __pycache__
│   └── monitoring.cpython-37.pyc
├── app.py
├── data
│   ├── cs-production
│   ├── cs-train
│   └── ts-data
├── logs
│   ├── predict-2021-4.log
│   ├── predict-test.log
│   └── train-test.log
├── models
│   ├── sl-all-0_1.joblib
│   ├── sl-eire-0_1.joblib
│   ├── sl-france-0_1.joblib
│   ├── sl-germany-0_1.joblib
│   ├── sl-hong_kong-0_1.joblib
│   ├── sl-netherlands-0_1.joblib
│   ├── sl-norway-0_1.joblib
│   ├── sl-portugal-0_1.joblib
│   ├── sl-singapore-0_1.joblib
│   ├── sl-spain-0_1.joblib
│   ├── sl-united_kingdom-0_1.joblib
│   ├── test-all-0_1.joblib
│   └── test-united_kingdom-0_1.joblib
├── requirements.txt
├── run-model-train.py
├── run-tests.py
├── src
│   ├── WORKSPACE.ipynb
│   ├── __pycache__
│   ├── config.py
│   ├── cslib.py
│   ├── logger.py
│   ├── model.py
│   └── monitoring.py
├── templates
│   └── index.html
└── unittests
    ├── ApiTests.py
    ├── LoggerTests.py
    ├── ModelTests.py
    ├── __init__.py
    └── __pycache__

12 directories, 36 files
```

# Test
You can run all tests, MODEL, API, LOGGER, by running the following run-tests.py.
```sh
$ python run-tests.py
```
# Train
You can train model.
```python
$ python run-model-train.py
```

# Build and run docker continer
```sh
#build the image
$ docker build -t capstone-app .

#Run the container
$ docker run -p 4000:8080 capstone-app
```

# API
Requests and responses for prediction.
```python
# requests
{'query': {'country': 'all', 'year': '2018', 'month': '4', 'day': '1'}, 'type': 'dict', 'mode': 'test'}

#POSR
requests.post('http://127.0.0.1:{}/predict'.format(port), json=request_json)

# responce
{'y_pred': [117270.77932], 'y_proba': None}
```

