# Python 3

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import random


def mat_mult_and_bias(values,weight, bias):
    result = mat_mult(values,weight)
    c = len(result)
    for cc in range(c):
        result[cc] += bias[cc]
    return result

def mat_mult(values,weight):
    r = len(values)
    if type(weight[0]) != list:
        return [sum([values[rr][kk] * weight[kk] for kk in range(len(values[0]))]) for rr in range(r)]
    c = len(weight[0])
    if type(values[0])!=list:
        return [sum([values[kk] * weight[kk][cc] for kk in range(len(values))]) for cc in range(c)]

    k = len(values[0])
    result = [[0] * c for rr in range(r)]
    for rr in range(r):
        for cc in range(c):
            for kk in range(k):
                result[rr][cc] += values[rr][kk] * weight[kk][cc]
    return result
    
def layer(values,weight, bias, activation):
    pre_value = mat_mult_and_bias(values,weight, bias) 
    return activation(pre_value)

def col_sum_arr(arr):
    # make np.sum
    try:
        return [sum([arr[j][idx] for j in range(arr)]) for idx in range(len(arr[0]))]
    except:
        return [sum(arr)]
def trans_arr(arr): 
    # roates input arr
    try:
        return list(map(list,zip(*arr)))
    except:
        return [[val] for val in arr]
class Affine:
    def __init__(self,weight, bias):
        self.weight = weight
        self.bias = bias
        self.in_val = None
        self.dWeight = None
        self.dBias = None
    
    def forward(self,in_val):
        self.in_val = in_val
        out = mat_mult_and_bias(in_val, self.weight, self.bias)
        return out

    def backward(self, dOut):
        trans_weight = trans_arr(self.in_val)
        dIn_val = mat_mult(dOut, trans_weight)
        self.dWeight = mat_mult(trans_weight, dOut)
        self.dBias = col_sum_arr(dOut)
        return dIn_val
def sigmoid(vals):
    sig_vals = [1 / (1 + math.exp(-val)) for val in vals]
    return sig_vals
class Sigmoid:
    def __init__(self):
        self.out = None
    def forward(self,in_val):
        out = sigmoid(in_val)
        self.out = out
        return out
    def backward(self, dOut):
        dIn_val = dOut* (1.0 - self.out) * self.out
        return dIn_val

def softmax(vals):
    # 문제는 나중에 해결.
    exp_vals = [math.exp(val) for val in vals]
    sum_of_exp_vals = sum(exp_vals)
    
    val_length = len(exp_vals)
    for val_idx in range(val_length):
        exp_vals[val_idx] = exp_vals[val_idx] / sum_of_exp_vals

    return exp_vals

class Softmax:
    def __init__(self):
        self.out = None
    def forward(self,in_val):
        # 추가 구현 필요
        self.out = softmax(in_val)
        return self.out
    
    def backward(self, answer_hot_encode):
        dIn_val = [self.out[idx] - answer_hot_encode[idx] for idx in range(len(self.out))]
        return dIn_val
        
class Net:
    def __init__(self,ouput_size, input_size, layer_sizes):
        self.output_size = ouput_size
        self.input_size = input_size
        layer_length = len(layer_sizes)
        self.weights = [0] * (layer_length)
        self.biases = [0] * (layer_length)
        self.layers = [0] * (layer_length * 2 - 1)
        self.last_layer = 0
        for layer_idx in range(layer_length):
            r,c = layer_sizes[layer_idx]
            # 편향 및 가중치 초기화
            self.weights[layer_idx] = [[random.uniform(-1,1) for cc in range(c)] for rr in range(r)]
            self.biases[layer_idx] = [random.uniform(-1,1) for cc in range(c)]
            
        # 레이어 초기화
        self.layers[0] = Affine(self.weights[0], self.biases[0])
        self.layers[1] = Sigmoid()
        self.layers[2] = Affine(self.weights[1], self.biases[1])
        self.last_layer = Softmax()
    
    def sum_squares_error(self,custom_answer,answer_one_hot_encode):
        return 0.5 * sum([(custom_answer[i] - answer_one_hot_encode[i])**2 for i in range(ANSWER_SIZE)])

    def cross_entropy_error(self,custom_answer,answer_one_hot_encode):
        d = 1e-7
        return -sum([answer_one_hot_encode[i] * math.log(custom_answer[i] + d) for i in range(ANSWER_SIZE)])
    
    def predict(self, in_val):
        for layer in self.layers:
            in_val = layer.forward(in_val)
        out = self.last_layer.forward(in_val)
        return out
    
    def gradient(self,answer_one_hot):
        dOut = self.last_layer.backward(answer_one_hot)
        for layer in reversed(self.layers):
            dOut = layer.backward(dOut)
        # 갱신
        for idx in range(len(self.layers)):
            self.weights[idx] = self.layers[idx][0].dW
            self.biases[idx] = self.layers[idx][0].dB
        return None
    def train(self, in_val, answer):
        
        out = self.predict(in_val)
        answer_one_hot = [0] * self.output_size
        answer_one_hot[answer] = 1
        loss = self.cross_entropy_error(out, answer_one_hot)
        self.gradient(answer_one_hot)
        return loss
    

def predict(I,H,O,image,weights, biases):

    hidden_layer_values = layer(image, weights[0], biases[0], sigmoid)

    output_layer_values = layer(hidden_layer_values, weights[1], biases[1], softmax)
    tmp = max(output_layer_values)
    
    return output_layer_values.index(tmp)
def model():
    N = int(input()) # 이미지 개수
    I, H, O = map(int, input().split())
     
    images = [0] * N
    for idx in range(N):
        images[idx] = list(map(float,input().split()))
        
    weight_1 = [0] * I
    for idx in range(I):
        weight_1[idx] = list(map(float, input().split()))
        
    bias_1 = list(map(float,input().split()))
    
    weight_2 = [0] * H
    for idx in range(H):
        weight_2[idx] = list(map(float, input().split()))
        
    bias_2 = list(map(float,input().split()))
    
    for image in images:
        result = predict(I,H,O, image,[weight_1, weight_2], [bias_1, bias_2])
        print(result)

        
ANSWER_SIZE = 10


def init():
    N, M = map(int, input().split())
    # 이따 바꿔
    net = Net(10,25, [(25, 100), (100,10)])
    for i in range(10):
        raws = list(map(float,input().split()))
        in_val = raws[:25]
        answer = int(raws[25])
        tmp = net.train(in_val, answer)
        print(tmp)
init()