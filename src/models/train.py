import pandas as pd
import numpy as np
from random import uniform
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs, make_classification

def lvq_fit(train, target, lrate, b, max_epoch):
  train = np.array([x for x in train.to_numpy()])
  target = target.to_numpy()
  label, train_idx = np.unique(target, return_index=True)
  weight = train[train_idx].astype(np.float64)
  train = np.asarray([e for i, e in enumerate(zip(train, target)) if i not in train_idx], dtype='object')
  train, target = train[:, 0], train[:, -1]
  epoch = 0

  while epoch < max_epoch:
    for i, x in enumerate(train):
      distance = [sum((w - x) ** 2) for w in weight]
      min = np.argmin(distance)
      sign = 1 if target[i] == label[min] else -1
      weight[min] += sign * lrate * (x - weight[min])
    lrate *= b
    epoch += 1

  return weight, label


