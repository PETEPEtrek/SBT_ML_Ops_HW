#!/bin/bash

apt-get update
apt-get install -y g++ python3 libopenblas-dev
apt-get install -y libgtest-dev

echo "All necessary packages have been installed!"
