import tensorflow as tf

dataset = tf.data.Dataset.from_tensor_slices(tf.random_uniform([4, 10]))
print(dataset.output_types)
print(dataset.output_shapes)

print(tf.square(5))
