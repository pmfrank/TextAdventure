import tensorflow as tf

@tf.function
def f(x, y):
    return x ** 2 + y

x = tf.constant([2,3])
y = tf.constant([3,-2])

print(f(x,y))
