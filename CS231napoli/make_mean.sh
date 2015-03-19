#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

TOOLS=/Users/alaruba/CS231/caffe/build/tools

$TOOLS/compute_image_mean train_lmdb \
  imagenet_mean.binaryproto

echo "Done."
