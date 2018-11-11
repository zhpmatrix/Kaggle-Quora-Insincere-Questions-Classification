#t2t-datagen --t2t_usr_dir=script --problem=my_problem --data_dir=./data

NUM=0
TRAIN=./train/$NUM

if [ ! -d $TRAIN ];then
	mkdir $TRAIN
fi

#t2t-trainer --t2t_usr_dir=script --problem=my_problem --data_dir=./data --model=transformer_encoder --hparams_set=transformer_tiny --train_steps=20000 --output_dir=$TRAIN

#t2t-avg-all --model_dir=train/1/ --output_dir=train/merge_all/ 

t2t-decoder --t2t_usr_dir=script --problem=my_problem --data_dir=./data --model=transformer_encoder --hparams_set=transformer_tiny --output_dir=train/$NUM --decode_from_file=rawdata/dev_big_10000.csv --decode_to_file=decoder/$NUM.lc


#t2t-exporter --t2t_usr_dir=script --problem=my_problem --data_dir=./data --model=lstm_seq2seq_attention --hparams_set=lstm_attention --output_dir=$TRAIN
