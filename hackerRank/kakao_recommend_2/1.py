# Python 3

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def sigmoid(vals):
    sig_vals = [1 / (1 + math.exp(-val)) for val in vals]
    return sig_vals

def softmax(vals):
    # 문제는 나중에 해결.
    exp_vals = [math.exp(val) for val in vals]
    sum_of_exp_vals = sum(exp_vals)
    
    val_length = len(exp_vals)
    for val_idx in range(val_length):
        exp_vals[val_idx] = exp_vals[val_idx] / sum_of_exp_vals

    return exp_vals
    
def mat_mult_and_bias(values,weight, bias):
    try:
        len(values[0])
    except:
        values = [values]
    rr = len(values)
    cc = len(weight[0])
    kk = len(values[0])
    result = [[0] * cc for r in range(rr)]
    for rr in range(len(values)):
        for cc in range(len(weight[0])):
            for k in range(kk):
                result[rr][cc] += values[rr][k] * weight[k][cc]
            result[rr][cc] += bias[cc]
    return result[0]

def layer(values,weight, bias, activation):
    pre_value = mat_mult_and_bias(values,weight, bias) 
    return activation(pre_value)

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
model()