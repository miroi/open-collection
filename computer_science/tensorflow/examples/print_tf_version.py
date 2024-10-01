# https://www.tensorflow.org/tutorials/quickstart/beginner#set_up_tensorflow
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
print("TensorFlow version:", tf.__version__)
