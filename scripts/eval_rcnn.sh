export NGPUS=8
python -m torch.distributed.launch --nproc_per_node $NGPUS tools/test_net.py --config-file configs/kitti/pob/rcnn.yaml