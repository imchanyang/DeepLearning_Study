import tensorflow as tf

# 키 = [170, 180, 175, 160]
# 신발 = [260, 270, 265, 255]

키 = 170
신발 = 260

# weight and bias
w = tf.Variable(0.1)
b = tf.Variable(0.2)


# cost function
def cost():
    return (신발 - (키 * w + b)) ** 2


# Adam optimizers and learning rate
opt = tf.keras.optimizers.Adam(learning_rate=0.1)


# 경사하강법 1000법
for i in range(1000):
    opt.minimize(cost, var_list=[w, b])
    print(w.numpy(), b.numpy())

# 학습된 모델로 예측해보기
Height = 175
predictSize = Height*w + b

print(predictSize.numpy())


