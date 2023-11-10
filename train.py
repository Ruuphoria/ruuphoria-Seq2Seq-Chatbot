
import tensorflow as tf
import model
import pprint
import _pickle as cPickle
from glob import glob
import math
import sys
import numpy as np
from utils import TextLoader, UNK_ID
from model import DialogueModel

pp = pprint.PrettyPrinter()

flags = tf.app.flags