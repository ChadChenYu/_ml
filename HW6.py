import math

class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
    
    def sigmoid(self):
        s = 1 / (1 + math.exp(-self.data))
        out = Value(s, (self,), 'sigmoid')
        
        def _backward():
            self.grad += s * (1 - s) * out.grad
        out._backward = _backward
        
        return out
    
    def exp(self):
        x = math.exp(self.data)
        out = Value(x, (self,), 'exp')
        
        def _backward():
            self.grad += x * out.grad
        out._backward = _backward
        
        return out
#由AI幫忙完成 https://chatgpt.com/share/67f72104-5bdc-8003-9002-2be1424e24c8
