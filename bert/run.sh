export BERT_BASE_DIR=/home/amax/zhanghaipeng/bert/model/uncased_L-12_H-768_A-12
export GLUE_DIR=/home/amax/zhanghaipeng/kaggle/bert/glue_data

CUDA_VISIBLE_DEVICES=0 	python bert-master/run_classifier.py \
	  --task_name=Quora \
	    --do_train=false \
	      --do_eval=true \
	        --data_dir=$GLUE_DIR/Quora \
		  --vocab_file=$BERT_BASE_DIR/vocab.txt \
		    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
		      --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
		        --max_seq_length=128 \
			  --train_batch_size=128 \
			    --eval_batch_size=8 \
			    --pred_batch_size=8 \
			    --learning_rate=2e-5 \
			      --num_train_epochs=3.0 \
			        --output_dir=./quora_output/ \
