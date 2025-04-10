import torch
import torch.nn as nn
import torch.optim as optim

# 生成測試數據 (y = 3x + 2)
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]], dtype=torch.float32)
y_train = torch.tensor([[5.0], [8.0], [11.0], [14.0], [17.0]], dtype=torch.float32)

# 定義線性回歸模型
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 一個輸入，一個輸出
    
    def forward(self, x):
        return self.linear(x)

# 初始化模型、損失函數和優化器
model = LinearRegressionModel()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 訓練模型
num_epochs = 1000
for epoch in range(num_epochs):
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# 輸出最終的權重和偏置
w, b = model.linear.weight.item(), model.linear.bias.item()
print(f'Learned parameters: w = {w:.3f}, b = {b:.3f}')

#GPT-4o生成 https://chatgpt.com/canvas/shared/67f7283975a48191b99b44a311b943ef
