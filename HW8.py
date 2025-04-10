import torch

def optimize_function():
    # 定義變數並啟用梯度計算
    x = torch.tensor(0.0, requires_grad=True)
    y = torch.tensor(0.0, requires_grad=True)
    z = torch.tensor(0.0, requires_grad=True)
    
    lr = 0.01  # 學習率
    num_iterations = 1000  # 迭代次數
    
    for _ in range(num_iterations):
        # 定義目標函數
        f = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8
        
        # 計算梯度
        f.backward()
        
        with torch.no_grad():
            # 梯度下降更新變數值
            x -= lr * x.grad
            y -= lr * y.grad
            z -= lr * z.grad
            
            # 清空梯度
            x.grad.zero_()
            y.grad.zero_()
            z.grad.zero_()
    
    print(f"x = {x.item():.3f}, y = {y.item():.3f}, z = {z.item():.3f}")
    print(f"f(x, y, z) = {f.item():.3f}")

optimize_function()
#由GPT-4o生成https://chatgpt.com/canvas/shared/67f7277d38648191a7e55a5fc18ff31b
