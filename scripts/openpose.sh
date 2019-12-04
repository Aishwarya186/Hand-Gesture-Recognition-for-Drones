#! /bin/bash
cd ../openpose
./build/examples/openpose/openpose.bin --image_dir $1 --write_json $2 --display 0 --render_pose 0
echo $1 $2
