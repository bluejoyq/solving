# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def sigmoid(val):
    return 1 / (1 + math.exp(-val))

def softmax(vals):
    # 문제는 나중에 해결.
    exp_vals = [math.exp(val) for val in vals]
    sum_of_exp_vals = sum(exp_vals)
    
    val_length = len(exp_vals)
    for val_idx in range(val_length):
        exp_vals[val_idx] = exp_vals[val_idx] / sum_of_exp_vals

    return exp_vals
    

    
def feed_foward(input_value,weight, bias, activation):
    #pre_values = [input_value * weight + bias for input_value in input_values] 
    pre_value = input_value * weight + bias
    return activation(pre_value)

def hidden_layer(image,hidden_idx,I,weight, bias):
    pre_vals = [feed_foward(image[input_idx], weight[input_idx][hidden_idx], bias[hidden_idx], sigmoid) for input_idx in range(I)]  
    return sum(pre_vals)

def output_layer((hidden_layer_values, output_idx, O, weight, bias):
    pre_vals = [feed_foward(image[input_idx], weight[input_idx][hidden_idx], bias[hidden_idx], softmax) for input_idx in range(I)]  
    return sum(pre_vals)   

def predict(I,H,O,image,weights, biases):
    hidden_layer_values = [0] * H
    for hidden_idx in range(H):
        hidden_layer_values[hidden_idx] = hidden_layer(image, hidden_idx, I, weights[0], biases[0])
    
    output_layer_values = [0] * O
    for output_idx in range(O):
        output_layer_values[output_idx] = output_layer(hidden_layer_values, output_idx, O, weights[1], biases[1])

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
        predict(I,H,O, image,[weight_1, weight_2], [bias_1, bias_2])

model()