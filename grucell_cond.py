
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
    self._cell = cell
    self._output_size = self._cell.output_size

  @property
  def state_size(self):
    return self._cell.state_size

  @property
  def output_size(self):
    return self._output_size

  def zero_state(self, batch_size, dtype):
    with ops.name_scope(type(self).__name__ + "ZeroState", values=[batch_size]):
      return self._cell.zero_state(batch_size, dtype)

  def __call__(self, inputs, state, scope=None):
    output, res_state = self._cell(inputs, state, self._context)
    return output, res_state

class GRUCellCond(RNNCell):
  """Gated Recurrent Unit cell (cf. http://arxiv.org/abs/1406.1078)."""

  def __init__(self, num_units, input_size=None, activation=tanh, reuse=None):
    if input_size is not None:
      logging.warn("%s: The input_size parameter is deprecated.", self)
    self._num_units = num_units
    self._activation = activation
    self._reuse = reuse