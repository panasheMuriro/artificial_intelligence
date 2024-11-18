import tensorflow as tf

scalar = tf.constant(3)
print("scalar: ", scalar)

vector = tf.constant([1.0,2.0,3.0])
print("Vector: ", vector)

matrix = tf.constant(([1,2], [3,4]))
print("Matrix: ", matrix)

tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3-D Tensor:", tensor_3d)



# // basic math ops

vector_a = tf.constant([1.0,2.0])
vector_b = tf.constant([3.0, 5.0])
res = tf.add(vector_a, vector_b)
print(res)