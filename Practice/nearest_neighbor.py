from __future__ import print_function

import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("tmp/data", one_hot=True)

Xtr, Ytr = mnist.train.next_batch(5000)
Xte, Yte = mnist.train.next_batch(100)

xtr = tf.placeholder(tf.float32,[None,784])
xte = tf.placeholder(tf.float32,)