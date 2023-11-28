# YOLOV7-AC
The implemented core codes of YOLOV7-AC are open here, and the paper of YOLOV7-AC can be found at https://arxiv.org/abs/2302.06939. 

If you find our codes helpful, please star our project and cite our following papers: 

[1] Liu, K., Sun, Q., Sun, D., Peng, L., Yang, M., & Wang, N. (2023). Underwater target detection based on improved YOLOv7. Journal of Marine Science and Engineering, 11(3), 677. 

[2] Liu, K., Tang, H., He, S., Yu, Q., Xiong, Y., & Wang, N. (2021, January). Performance validation of YOLO variants for object detection. In Proceedings of the 2021 International Conference on bioinformatics and intelligent computing (pp. 239-243).

[3] Liu, K., & Wang, N. (2023). Ensemble Fusionof UnderwaterImage Enhancement (EFUIE) Model for Comprehensive Quality Improvement. Journal ofJiangsu Ocean University (Natural Science Edition),32(3):71-79. (In Chinese)



If you have any question，please check the issue of Frequency Asking Questions first. If you have any collaboration suggestion about our method, please contact wangnizhuan1120@gmail.com. 

Also, you can attend our YOLO-Series WeChat group by scanning the following QR code, and you can post messeages about YOLOV7-AC. 

                                             ![Alt text](./yolo-series.jpg)




The codes of various networks were tested in Pytorch 1.7 version or higher versions(a little bit different from 0.8 version in some functions) in Python 3.8 on Ubuntu machines (may need minor changes on Windows). For the comparison models, e.g., EfficientDet, YOLOV5, YOLOV6, retinanet, SSD, etc., more information could be found at the corresponding sub-folders.

Usage for YOLOV7-AC

i. Clone this repo to local
      
      
      git clone https://github.com/NZWANG/YOLOV7-AC

ii. Download the experiment dataset from the link below, and put it into the directory
      
      
      URPC:https://www.heywhale.com/home/competition/605ab78821e3f6003b56a7d8/content/0
      Brackish:https://www.kaggle.com/datasets/aalborguniversity/brackish-dataset

iii. Training
     
     
     python train.py --workers 0 --device 0 --batch-size 16 --data data/URPC.yaml --img 640 640 --cfg cfg/training/yolov7-AC.yaml --weights '' --name yolov7 --hyp data/hyp.scratch.p5.yaml
