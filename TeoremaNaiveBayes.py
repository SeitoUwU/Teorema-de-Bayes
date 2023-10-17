import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn .nodel_selection import train_test_split
import matplotlib.pyplot as plt

from matplotlib import colors

%matplotlib inline
plt. rcParams['figure.figsize'] = (16,9)
plt. style. use('ggplot')