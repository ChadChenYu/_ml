from micrograd.engine import Value
import random

def f(x, y, z):
    x, y, z = Value(x), Value(y), Value(z)
    result = (x * x + y * y + z * z - 2 * x - 4 * y - 6 * z + 8)
    return result

def gradientDescent(f, x_init, y_init, z_init, lr=0.1, epochs=100):
    x = Value(x_init)
    y = Value(y_init)
    z = Value(z_init)

    for i in range(epochs):
        loss = f(x, y, z)
        loss.backward()
        x.data -= lr * x.grad
        y.data -= lr * y.grad
        z.data -= lr * z.grad

        x.grad = 0
        y.grad = 0
        z.grad = 0

        print(f"Epoch {i+1}: x = {x.data:.3f}, y = {y.data:.3f}, z = {z.data:.3f}, f(x, y, z) = {loss.data:.3f}")

    return (x.data, y.data, z.data, loss.data)

gradientDescent(f, 0, 0, 0)

#使用AI處理:https://chatgpt.com/share/67cf0bbf-fb08-8003-b592-30b46881d36a
