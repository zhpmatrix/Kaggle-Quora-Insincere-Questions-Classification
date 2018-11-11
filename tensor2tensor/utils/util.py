import xml.dom.minidom
from tqdm import tqdm
import pandas as pd
from sklearn.metrics import classification_report

def gpu_config(gpu_num):
    import tensorflow as tf
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

def get_test_data(test_file, save_file):
    writer = open(save_file, 'w')
    with open(test_file, 'r') as f:
        texts = f.readlines()
        for i,text in enumerate( texts ):
            if i == 0:
                continue
            id_for_dot = text.find(',')
            q = text[id_for_dot+1:]
            writer.write(q)
    writer.close()

def get_dev_data(dev_file, save_file):
    data = pd.read_csv(dev_file, header=None, sep=',') 
    writer = open(save_file, 'w')
    for i in range(data.shape[0]):
        q = data.iloc[i][1]
        writer.write(q+'\n')
    writer.close()

def get_eval(real_file, pred_file, test_num):
    real_data = pd.read_csv(dev_file, header=None, sep=',')
    label_map = {0:'0', 1:'1'}
    real_labels = []
    for i in range(test_num):
        a = real_data.iloc[i][2]
        real_labels.append(label_map[a])

    pred_labels = []
    with open(pred_file, 'r') as f:
        labels = f.readlines()
    for label in labels:
        pred_labels.append(label.strip().split('_')[-1])
    print(classification_report(real_labels, pred_labels))

if __name__ =='__main__':
    test_file = '../rawdata/test.csv'
    save_file = '../rawdata/test_.csv'
    #get_test_data(test_file, save_file) 
    
    dev_file = '../rawdata/dev_big.csv'
    save_file = '../rawdata/dev_big_.csv'
    #get_dev_data(dev_file, save_file) 

    pred_file = '../decoder/0.lc'
    test_num = 10000
    get_eval(dev_file, pred_file, test_num)
