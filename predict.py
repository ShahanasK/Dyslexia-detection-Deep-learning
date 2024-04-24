#variables
num_classes =2
batch_size = 50
epochs = 9
#------------------------------

import os, cv2
from keras.models import Sequential
from keras.engine.saving import load_model
import numpy as np

def read_dataset1(path):
    data_list = []
    file_path = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    return (np.asarray(data_list, dtype=np.float32))


# ------------------------------
# construct CNN structure
from keras import backend as K
model = Sequential()
proj_path=r"C:\Users\Admin\Music\web\web\static\\"
def predictcnn(fn):
    dataset=read_dataset1(fn)
    dataset=dataset / 255
    (mnist_row, mnist_col, mnist_color) = 48, 48, 1
    dataset = dataset.reshape(dataset.shape[0], mnist_row, mnist_col, mnist_color)
    K.clear_session()
    mo = load_model(proj_path + "model1.h5")
    yhat_classes = mo.predict_classes(dataset, verbose=0)
    K.clear_session()
    return yhat_classes


# label_list = ["Dyslexic", "Normal"]
# pred = predictcnn(r"C:\Users\Admin\Music\web\web\static\Train\Dyslexic\1_7.png")
# print("Folder index : ", pred)
# idx = pred[0]
# val= label_list[idx]
# print("Prediction : ", val)
