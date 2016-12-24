"""
Author: roopal jain
"""

import pandas as pd
file = 'titanic_data.csv'
full_data = pd.read_csv(file)

outcomes=full_data['Survived']
data=full_data.drop('Survived', axis=1)

def accuracy_score(truth, pred):
    if len(truth)==len(pred):
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"


def prediction_calc(data):
    
    predictions = []
    for _, passenger in data.iterrows():        
        if passenger['Sex']=="female" and passenger['Pclass']<=2 :
         predictions.append(1)
        elif passenger['Sex']=="male" and passenger['Age']<10 and passenger['Pclass']>1 and passenger['SibSp']<=2:
         predictions.append(1)
        else:
         predictions.append(0)
    return pd.Series(predictions)
            
predictions = prediction_calc(data)

print accuracy_score(outcomes, predictions)