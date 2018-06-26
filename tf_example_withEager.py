
"""
INFO:

Simple tutorial on how to enable standard like python-debubig in Tensorflow library, 
through 'eager execution mode'. Script allows you to check dynamic all values of 
variables and even convert the to numpy array, without te need of graph execution

"""

import tensorflow as tf
import numpy as np
import pdb

# Enable eager execution - for enabling standard debugging
tf.enable_eager_execution()

a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
c = tf.matmul(a, b)


print ("Values of tensor \'a\' : ", a)  
print ("Type of tensor \'a\' : ", type(a))  #  EagerTensor type
print ("")
print ("Values of tensor \'b\' : ", b)
print ("Type of tensor  \'b\' : ", type(b))  #  EagerTensor type
print ("")
print ("Values of tensor \'c\' : ", c)
print ("Type of tensor \'c\' : ", type(c))  #  EagerTensor type
print ('')

# convert EagerTensor to numpy
print ("New type of matrix \'a\' ", type(np.array(a)))  # convert to numpy array

# Enable dubbing for dynamic check of variables
pdb.set_trace()
