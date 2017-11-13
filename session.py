import tensorflow as tf
import numpy as np

with tf.name_scope("input"):
    input1 = tf.constant([1.0,2.0,3.0])
    input2 = tf.constant([1.0,2.0,3.0])

output = tf.add_n([input1, input2], name = "add")

#tf.summary.scalar('input1', input1)
#tf.summary.scalar('input2', input2)
tf.summary.scalar('output', output)

sess = tf.Session()
sess.run(output)

writer = tf.summary.FileWriter("log", tf.get_default_graph())
writer.close()