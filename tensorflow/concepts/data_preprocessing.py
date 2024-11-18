# Objectives
# Learn the basics of the Dataset API for efficient data handling.
# Load and preprocess data (batching, shuffling, and mapping).
# Prepare a dataset for training with TensorFlow.


# Why Data Preprocessing is Important
# Real-world data is often messy, requiring cleaning, normalization, and transformation. 
# Preprocessing ensures that your model can learn effectively and efficiently. 
# The Dataset API in TensorFlow is optimized for handling large data, allowing you to build scalable and efficient data pipelines.


# Basic Data Transformations
# Once you load data into a dataset, you can transform it by applying operations like batching, shuffling, and mapping.
import tensorflow as tf

# 1. Batching
# Batching groups your data into smaller sets, which is useful for feeding data into your model in chunks.


data = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
labels = tf.constant([0, 1, 0])
dataset = tf.data.Dataset.from_tensor_slices((data, labels))


def normalize(features, label):
    features = features / 255.0  # Example for image normalization
    return features, label


# Shuffling, batching, and mapping
dataset = dataset.shuffle(buffer_size=10).batch(2).map(normalize)

# Display the processed data
for features, label in dataset:
    print("Features:", features.numpy())
    print("Label:", label.numpy())