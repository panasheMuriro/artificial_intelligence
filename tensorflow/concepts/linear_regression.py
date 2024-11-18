# Objectives
# Understand the concept of linear regression and how it applies to machine learning.
# Build a linear regression model using TensorFlow.
# Train and evaluate the model on a dataset.


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
X = np.random.rand(100, 1).astype(np.float32)
y = 3.5 * X + np.random.randn(100, 1) * 0.2

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])