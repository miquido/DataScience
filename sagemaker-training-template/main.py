import argparse
import os
import json
import pickle
import sys
import traceback
import joblib

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

output_path = '/opt/ml/output'
model_path = '/opt/ml/model'
hyperparameters_path = '/opt/ml/input/config/hyperparameters.json'
training_path = '/opt/ml/input/data/train'


def train():
    print('Train job started')
    try:
        # Read in any hyperparameters that the user passed with the training job
        with open(hyperparameters_path, 'r') as tc:
            trainingParams = json.load(tc)

        input_files = [ os.path.join(training_path, file) for file in os.listdir(training_path) ]
        raw_data = [ pd.read_csv(file, header=0) for file in input_files ]
        train_data = pd.concat(raw_data)

        # labels are in the last column
        train_X = train_data.ix[:,:-1]
        train_y = train_data.ix[:,-1:]

        # Here we only support a single hyperparameter. Note that hyperparameters are always passed in as
        # strings, so we need to do any necessary conversions.
        penalty = trainingParams.get('penalty', 'l2')

        clf = LogisticRegression(penalty=penalty)
        clf = clf.fit(train_X, train_y)
        f1 = f1_score(train_y, clf.predict(train_X))
        print("F1 = " + str(f1) + ";")

        # save the model
        with open(os.path.join(model_path, 'model.pkl'), 'wb') as out:
            pickle.dump(clf, out)
        print('Train job finished')
    except Exception as exc:
        trace = traceback.format_exc()
        #This should store error logs in CloudWatch
        print('Exception: ' + str(exc) + '\n' + trace, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    
    if sys.argv[1] == 'train':
        train()
        sys.exit(0)
    sys.exit(1)
