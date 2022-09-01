# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import pprint
import _pickle as cPickle
from model import DialogueModel
from utils import TextLoader, UNK_ID, PAD_ID
from glob import glob

checkpoint = "/tmp/model.ckpt"