# namegender [![Build Status](https://travis-ci.org/samuorous/namegender.svg?branch=master)](https://travis-ci.org/samuorous/namegender) [![Coverage Status](https://coveralls.io/repos/github/samuorous/namegender/badge.svg?branch=master)](https://coveralls.io/github/samuorous/namegender?branch=master)
Predict the gender of a name based on statistical data.

# Install
```bash
pip install namegender
```

# Usage
```python
>>> import namegender
>>> namegender.predict('Otto')
{'name': 'Otto', 'gender': 'male', 'probability': 99.68185288877577, 'samples': 31432}
>>> namegender.predict_list(['Otto', 'Jane'])
[
  {'gender': 'male', 'samples': 31432, 'name': 'Otto', 'probability': 99.68185288877577}, 
  {'gender': 'female', 'samples': 370379, 'name': 'Jane', 'probability': 99.69382713382778}
]
```

# Sources
* https://github.com/ropensci/genderdata
* https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-data-by-state-and-district-of-
* https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data
* http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/nlp/corpora/names/0.html
* https://usa.ipums.org/usa/
* https://www.nappdata.org/napp/
