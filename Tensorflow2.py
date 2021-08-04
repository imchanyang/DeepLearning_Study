# My first Deep Learning project
# 대학 합격 예측 AI 만들기

# 1. 딥러닝 model 디자인하기
# 2. model compile 하기
# 3. 데이터 전처리
# 4. model 학습(fit) 시키기
# 5. 학습시킨 모델로 예측해보기

import numpy as np
import pandas as pd
import tensorflow as tf

# 딥러닝 모델
# Sequential쓰면 신경말 레이어들을 쉽게 만들 수 있다
# 숫자는 노드의 개 관습적으로 2의 제곱수를 넣어준다 마지막은 결과이니 1개의 노드로 만들어준다
model = tf.keras.models.Sequential([
    # 활성홤수를 넣는다 activation
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    # 예측결과 0~1사이로 출력하기 위해서 (확률)
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# binary_crossentropy는 결과가 0과 1사이의 분류/확률 문제에서 씀
# accuracy 모델의 정답흏
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 데이터 전처리


data = pd.read_csv('gpascore.csv')

# 비어있는 칸수를 보는데 컬럽별로 본다
# print(data.isnull().sum())
# 비어있는 행을 삭제한다.
# data = data.dropna()
# 비어있는 칸에 값을 추가한다
# data = data.fillna(100)

# 비어있는 칸에 평균을 넣는다
data = data.fillna(data['gre'].mean())

# values로 넣어주면 리스트로 만들어준다
y데이터 = data['admit'].values

x데이터 = []

# data.iterrows() data라는 데이터 프레임을 가로 한줄씩 출력(행)
for i, rows in data.iterrows():
   x데이터.append([rows['gre'], rows['gpa'], rows['rank']])

# 학습
# x데이터 : gre, gpa, rank y데이터 : 합불
# epochs : 몇번 학습시킬지
# 리스트를 바로 못넣는다 np.array사용
model.fit(np.array(x데이터), np.array(y데이터), epochs=2000)

# 예측
예측값 = model.predict([[700, 3.70, 3], [400, 2.20, 1]])
print(예측값)


