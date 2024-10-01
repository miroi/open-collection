Tensorflow on hydra.jinr.ru
===========================

see https://github.com/tensorflow/tensorflow/issues/62075#issuecomment-2310327870

module add Python/v3.10.2
pip3 install Tensorflow==2.16.1
.
.
Installing collected packages: namex, libclang, flatbuffers, wrapt, wheel, urllib3, typing-extensions, termcolor, tensorfl          ow-io-gcs-filesystem, tensorboard-data-server, pygments, protobuf, opt-einsum, ml-dtypes, mdurl, markdown, idna, h5py, grp          cio, google-pasta, gast, charset-normalizer, certifi, absl-py, tensorboard, requests, optree, markdown-it-py, astunparse,           rich, keras, tensorflow
Successfully installed absl-py-2.1.0 astunparse-1.6.3 certifi-2024.8.30 charset-normalizer-3.3.2 flatbuffers-24.3.25 gast-0.6.0 google-pasta-0.2.0 grpcio-1.66.2 h5py-3.12.1 idna-3.10 keras-3.5.0 libclang-18.1.1 markdown-3.7 markdown-it-py-3.0.0 mdurl-0.1.2 ml-dtypes-0.3.2 namex-0.0.8 opt-einsum-3.4.0 optree-0.12.1 protobuf-4.25.5 pygments-2.18.0 requests-2.32.3 rich-13.8.1 tensorboard-2.16.2 tensorboard-data-server-0.7.2 tensorflow-2.16.1 tensorflow-io-gcs-filesystem-0.37.1 termcolor-2.4.0 typing-extensions-4.12.2 urllib3-2.2.3 wheel-0.44.0 wrapt-1.16.0

milias@hydra.jinr.ru:~/work/projects/open-collection/computer_science/tensorflow/.pip3 show tensorflow
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Name: tensorflow
Version: 2.16.1
Summary: TensorFlow is an open source machine learning framework for everyone.
Home-page: https://www.tensorflow.org/
Author: Google Inc.
Author-email: packages@tensorflow.org
License: Apache 2.0
Location: /lustre/home/user/m/milias/.local/lib/python3.10/site-packages
Requires: absl-py, astunparse, flatbuffers, gast, google-pasta, grpcio, h5py, keras, libclang, ml-dtypes, numpy, opt-einsum, packaging, protobuf, requests, setuptools, six, tensorboard, tensorflow-io-gcs-filesystem, termcolor, typing-extensions, wrapt
Required-by:


