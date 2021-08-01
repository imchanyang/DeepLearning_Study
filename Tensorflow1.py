import tensorflow as tf

# 키 = [170, 180, 175, 160]
# 신발 = [260, 270, 265, 255]

키 = 170
신발 = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)


def cost():
    return (신발 - (키 * a + b)) ** 2


opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(1000):
    opt.minimize(cost, var_list=[a, b])
    print(a.numpy(), b.numpy())


Height = 180
predictSize = Height*a + b

print(predictSize.numpy())


