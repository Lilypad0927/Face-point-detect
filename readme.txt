------  Guide  ------

- FIRST PART -

cmd line sequence

(1)Add image path to imagelist.txt
python print_path.py

(2)Detect Face - result in bbox.txt
FacePartDetect.exe data imagelist.txt bbox.txt

(3)Change bbox.txt content to fit TestNet - result in bbox2.txt
python face_to_point.py

(4)Eye , nose and mouth - result in result.bin
TestNet.exe bbox2.txt image2 Input result.bin

- SECOND PART -

Open Matlab and ensure image2 is in working directory

(1)run show_result.m - result in show_result
show_result.m