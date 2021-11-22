
# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.ops.rnn_cell_impl import _RNNCell as RNNCell
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import variable_scope as vs
from tensorflow.python.ops.math_ops import tanh, sigmoid
from tensorflow.contrib.rnn.python.ops.core_rnn_cell_impl import _linear, _checked_scope

class CondWrapper(RNNCell):
  def __init__(self, cell, context):
    self._context = context