"""Offline example using the public implementation; see README for evidence scope."""
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Generated measurements demonstrate the notebook's baseline path only.
# This is not the UCI benchmark or a biological model.
rng = np.random.default_rng(42)
num_features = ['Length', 'Diameter', 'Height', 'Whole_weight',
                'Shucked_weight', 'Viscera_weight', 'Shell_weight']
cat_features = ['Sex']
frame = pd.DataFrame(rng.uniform(.1, 1., (60, 7)), columns=num_features)
frame['Sex'] = np.resize(['M', 'F', 'I'], 60)
frame['Rings'] = 2. + 5. * frame['Length'] + rng.normal(0, .1, 60)
X_train, X_test, y_train, y_test = train_test_split(
    frame[num_features + cat_features], frame['Rings'], test_size=.2, random_state=42)
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(drop='first', sparse_output=False), cat_features)])
baseline = Pipeline([('pre', preprocessor), ('model', LinearRegression())])
baseline.fit(X_train, y_train)
result = {'fixture': 'generated measurements', 'train_rows': len(X_train),
          'test_rows': len(X_test),
          'mae': float(mean_absolute_error(y_test, baseline.predict(X_test)))}
import json
print(json.dumps(result, indent=2))
