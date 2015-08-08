#!/usr/bin/env python

__author__ = 'Shaun Rong'
__version__ = '0.1'
__maintainer__ = 'Shaun Rong'
__email__ = 'rongzq08@gmail.com'
import itertools

def gen_input_op():
    input_para = [[0, 1, 2]] * 8
    #input_para = [[0, 1, 2]] * 10
    return itertools.product(*input_para)


def op_cal(op):
    number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    #number_array = np.arange(1, 12)
    r = 0
    sep = [-1]
    operator = []
    #Step 1. find separation index of number_array
    for index, operation in enumerate(op):
        if operation != 0:
            sep.append(index)
            operator.append(operation)
    sep.append(len(number_array))
    #Step 2. Separate number_array into sub arrays
    number_list = []
    for i in range(len(sep) - 1):
        number_list.append(number_array[sep[i]+1:sep[i+1]+1])

    #debug example

    #print sep
    #print number_list

    #debug end

    #Step 3. create number from number_list, store them into s_list
    s_list = []
    for number in number_list:
        s = 0
        for i, d in enumerate(number):
            s += d * (10 ** (len(number) - i - 1))
        s_list.append(s)

    #print s_list

    #Step 4. Do the operation from operator list and s_list
    r += s_list[0]
    for index, op in enumerate(operator):
        if op == 2:
            r -= s_list[index + 1]
        if op == 1:
            r += s_list[index + 1]

    return r


def hot_date_with_itertools():
    operation = gen_input_op()
    summary = {}
    for op in operation:
        r = op_cal(op)
        summary[str(op)] = r
    return summary

if __name__ == '__main__':
    summary = hot_date_with_itertools()
    for key, value in summary.iteritems():
        if value == 100:
            print key
    # Example -- look into middle results
    #operation = list(gen_input_op())
    #print operation[200]
    #op_cal(operation[200])