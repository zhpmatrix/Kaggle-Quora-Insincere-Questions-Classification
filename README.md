# Kaggle-Quora-Insincere-Questions-Classification

Kaggle新赛-基于BERT的fine-tuning方案baseline

submit.csv是测试集的预测结果

代码和项目[基于BERT的中文tagging](https://github.com/zhpmatrix/bert-sequence-tagging)一样，仅提供关键fine-tuning代码和运行脚本


验证集的一个结果：

|class| precision | recall | f1-score |
|-----| ------ | ------ | ------ |
|0| 0.98 | 0.98 | 0.98 |
|1| 0.65 | 0.62 | 0.63 |

|micro avg| 0.96 | 0.96 | 0.96 |
|macro avg| 0.81 | 0.80 | 0.81 |
|weighted avg| 0.96 | 0.96 | 0.96 |

