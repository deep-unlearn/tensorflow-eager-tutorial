
"""
INFO: 

Standard way of checking values of variables through graph-execution
Check next code exasmpe for dynamic debbuging of variables 
(no need for execution of graphs)

"""

import tensorflow as tf
import pdb  # debbuging lib

a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
c = tf.matmul(a, b)

print type(a)  # tf.tensor
print type(b)  # tf.tensor
print type(c)  # tf.tensor - cannot see new values before graph execution  

# Activate line to check tensorflow tensors in detail
#pdb.set_trace()

# Construct a `Session` to execute the graph.
sess = tf.Session()

# Execute the graph to see value of tensor `c`, 'b', 'a'.
print ''
print 'Matrix c = ', sess.run(c)
print 'Matrix b = ', sess.run(b)
print 'Matrix a = ', sess.run(a)

