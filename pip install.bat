
echo "upgrade pip install..."
python -m pip install --upgrade pip

echo "Install Python QT..."
#PyQt
pip install PyQt5
pip install PyQt5-tools
pip install requests

#imgProcess
echo "Install Python imgage process package..."

pip install matplotlib
pip install opencv-python
pip install numpy


echo "Install PyTorch..."
#PyTorch
pip install torch
pip install torchvision

pip install gitpython

pause