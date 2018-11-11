# coding=utf-8
from tensor2tensor.utils import registry
from tensor2tensor.data_generators import problem, text_problems

from utils import util
util.gpu_config(0)

@registry.register_problem
class MyProblem(text_problems.Text2ClassProblem):
    @property
    def approx_vocab_size(self):
        return 2**13
    @property
    def num_classes(self):
        return 2
    @property
    def is_generate_per_split(self):
        # generate_data will shard the data into TRAIN and EVAL for us.
        return False

    @property
    def dataset_splits(self):
        """Splits of data to produce and number of output shards for each."""
        # 10% evaluation data
        return [{
            "split": problem.DatasetSplit.TRAIN,
            "shards": 9,
        }, {
            "split": problem.DatasetSplit.EVAL,
            "shards": 1,
        }]
    def generate_samples(self, data_dir, tmp_dir, dataset_split):
        del data_dir
        del tmp_dir
        del dataset_split
        
        import pandas as pd
        data = pd.read_csv('rawdata/train_big.csv',sep=',',error_bad_lines=False)
        train_num = data.shape[0]
        for i in range(train_num):
            en  = data.iloc[i][1]
            zh = data.iloc[i][2]#numpy.int64, diff with int.
            yield {
                "inputs": en,
                "label": int(zh)
            }

