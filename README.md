# Kaggle-Quora-Insincere-Questions-Classification

[Kaggle新赛](https://www.kaggle.com/c/quora-insincere-questions-classification)-基于BERT的fine-tuning方案baseline

submit.csv是测试集的预测结果

代码和项目[基于BERT的中文tagging](https://github.com/zhpmatrix/bert-sequence-tagging)一样，仅提供关键fine-tuning代码和运行脚本


基于bert的验证集的结果：

|class| precision | recall | f1-score |
|-----| ------ | ------ | ------ |
|0| 0.98 | 0.98 | 0.98 |
|1| 0.65 | 0.62 | 0.63 |
|micro avg| 0.96 | 0.96 | 0.96 |
|macro avg| 0.81 | 0.80 | 0.81 |
|weighted avg| 0.96 | 0.96 | 0.96 |


基于tensor2tensor的验证集结果：

|class| precision | recall | f1-score |
|-----| ------ | ------ | ------ |
|0| 0.98 | 0.96 | 0.96 |
|1| 0.23 | 0.19 | 0.21 |
|micro avg| 0.92 | 0.92 | 0.92 |
|macro avg| 0.59 | 0.57 | 0.58 |
|weighted avg| 0.91 | 0.92 | 0.91 |
