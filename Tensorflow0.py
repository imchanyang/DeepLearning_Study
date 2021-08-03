import tensorflow as tf

# 텐서플로우 상수
Tensor1 = tf.constant([3, 4, 5])
Tensor2 = tf.constant([6, 7, 8])

Tensor3 = tf.constant([[1, 2], [3, 4]])
Tensor4 = tf.constant([[1, 2], [3, 4]])

# 텐서플로우 행렬 곱
print(tf.matmul(Tensor3, Tensor4))

# 0으로 채우기
Tensor5 = tf.zeros([2, 2, 3])
print(Tensor5)

# 텐서플로우 변수
W = tf.Variable(1.0)
print(W)

# 변수값 할당
W.assign(2.0)
print(W.numpy())

