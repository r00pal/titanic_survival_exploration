## Project: Titanic Survival Exploration

##Project Overview
Decision functions are created that attempt to predict survival outcomes from the 1912 Titanic disaster based on each passenger's features, such as sex and age. The algorithm accurately predicts data with accuracy of 80% of the passengers provided in the data


### Softwares and libraries

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Jupyter Notebook](http://ipython.org/notebook.html)


### Run

In a terminal or command window, navigate to the top-level project directory `titanic_survival_exploration/` (that contains this README) and run one of the following commands:

```bash
jupyter notebook titanic_survival_exploration.ipynb
```
or
```bash
ipython notebook titanic_survival_exploration.ipynb
```

This will open the Jupyter Notebook software and project file in your web browser.

### Data

The dataset used in this project is included as `titanic_data.csv`. This dataset is provided by Udacity and contains the following attributes:

**Features**
- `pclass` : Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
- `name` : Name
- `sex` : Sex
- `age` : Age
- `sibsp` : Number of Siblings/Spouses Aboard
- `parch` : Number of Parents/Children Aboard
- `ticket` : Ticket Number
- `fare` : Passenger Fare
- `cabin` : Cabin
- `embarked` : Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

**Target Variable**
- `survival` : Survival (0 = No; 1 = Yes)
