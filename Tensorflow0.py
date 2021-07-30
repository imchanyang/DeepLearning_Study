import tensorflow as tf

Tensor1 = tf.constant([3, 4, 5])
Tensor2 = tf.constant([6, 7, 8])

Tensor3 = tf.constant([[1, 2], [3, 4]])
Tensor4 = tf.constant([[1, 2], [3, 4]])

print(tf.matmul(Tensor3, Tensor4))

Tensor5 = tf.zeros([2, 2, 3])
print(Tensor5)


W = tf.Variable(1.0)
print(W)

W.assign(2.0)
print(W.numpy())

