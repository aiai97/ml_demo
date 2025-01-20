import numpy as np

# 初始化数据
x = np.random.randn(10, 1)  # 输入数据
y = 2 * x + np.random.randn()  # 生成y, 确保它是与x大小一致的数组
w = 0.0  # 初始权重
b = 0.0  # 初始偏置
learning_rate = 0.01  # 学习率


# 梯度下降函数
def descend(x, y, w, b, learning_rate):
    dldw = 0.0
    dldb = 0.0
    N = x.shape[0]

    # 计算梯度
    for xi, yi in zip(x, y):
        dldw += -2 * xi * (yi - (w * xi + b))
        dldb += -2 * (yi - (w * xi + b))

    # 更新权重和偏置
    w = w - learning_rate * (1 / N) * dldw
    b = b - learning_rate * (1 / N) * dldb

    return w, b


# 训练过程
for epoch in range(600):  # 训练 400 次
    w, b = descend(x, y, w, b, learning_rate)
    yhat = w * x + b  # 预测值
    loss = np.divide(np.sum((y - yhat) ** 2), x.shape[0])  # 计算损失函数（MSE）

    print(f'Epoch {epoch}: Loss = {loss}, w = {w}, b = {b}')
