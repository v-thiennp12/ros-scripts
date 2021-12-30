
======================================================
sudo mv cuda-10.2/ /usr/local/

sudo mv driveworks-3.5/ /usr/local/

cd work/disk01/DATA/


=====================================================
run fusion + lane +visualizer

sudo find -name libopencv_imgcodecs.so.4.4
sudo find -name libcublas.so.10

nano ~/.bashrc


Terminal 1: Run Perception Node

cd ~/Desktop/Lane_Fusion/lane_detection_x86_20210710
./PerceptionSubnodes ./configs/subnodes/subnodes_config.yaml
Terminal 2: Run visualizer

cd ~/Desktop/Lane_Fusion/visualizer_release
./start_visualizer.sh
Terminal 3: Run Fusion SDK node

cd ~/Desktop/Lane_Fusion/ap_sensor_fusion-fusion_sdk_rti/fusion_sdk/build
./release/bin/lane_fusion_node ../lane_fusion/config/lane_fusion_params.yaml
Terminal 4: Publish Image from Video

cd ~/Desktop/Lane_Fusion/lane_detection_x86_20210710
./rti_dds_cameraImageData_publisher LINK_VIDEO ../data/configs/subnodesclear/sensor_manager_config.yaml

======================================================
cd visualizer_release/

source ~/.bashrc 

./start_visualizer.sh 

======================================================
cd lane_detection_x86_20210710/

./rti_dds_cameraImageData_publisher ../2021-07-09-14-55-14_20210709_Noon_demopath_INBOUND_mid.mp4 configs/subnodes/sensor_manager_config.yaml 

======================================================
cd ap_sensor_fusion-fusion_sdk_rti

mkdir build

cmake -DLOCAL_LIB_PATH=$LOCAL_LIB_PATH ..

cmake -DLOCAL_LIB_PATH=$LOCAL_LIB_PATH

make -j4

./release/bin/lane_fusion_node ../lane_fusion/config/lane_fusion_params.yaml 

=====================================================
cd lane_detection_x86_20210710/

./PerceptionSubnodes configs/subnodes/subnodes_config.yaml

=====================================================
Terminal 1: Run Perception Node
cd ~/Desktop/Lane_Fusion/lane_detection_x86_20210710
./PerceptionSubnodes ./configs/subnodes/subnodes_config.yaml

Terminal 2: Run visualizer
cd ~/Desktop/Lane_Fusion/visualizer_release
./start_visualizer.sh

Terminal 3: Run Fusion SDK node
cd ~/Desktop/Lane_Fusion/ap_sensor_fusion-fusion_sdk_rti/fusion_sdk/build
./release/bin/lane_fusion_node ../lane_fusion/config/lane_fusion_params.yaml

Terminal 4: Publish Image from Video
cd ~/Desktop/Lane_Fusion/lane_detection_x86_20210710
./rti_dds_cameraImageData_publisher LINK_VIDEO ../data/configs/subnodesclear/sensor_manager_config.yaml


