import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

wine = pd.read_csv('data/wine.csv')

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_jobs = -1, random_state = 42)
# ne_estimators = 100 결정트리개수 기본값, n_jobs=-1 cpu  core 할당 -1 전체 사용

scores = cross_validate(rf,X_train,y_train, return_train_score=True, n_jobs=-1)
# print(scores)
print(np.mean(scores['train_score']),np.mean(scores['test_score']))

rf.fit(X_train, y_train)
print(rf.predict(X_test[:5]))
print(rf.feature_importances_)