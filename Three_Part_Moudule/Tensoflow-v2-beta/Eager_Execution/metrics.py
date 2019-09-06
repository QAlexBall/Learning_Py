import tensorflow as tf

m = tf.keras.metrics.Mean("loss")
m(0)
m(5)
print(m.result())

m([8, 9])
print(m.result())
