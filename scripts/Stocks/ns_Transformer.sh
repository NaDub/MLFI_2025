python -u run.py \
  --is_training 1 \
  --root_path ./dataset/stock_var/ \
  --data_path stock.csv \
  --model_id stock_60_24 \
  --model ns_Transformer \
  --data custom \
  --features MS \
  --seq_len 60 \
  --label_len 30 \
  --pred_len 24 \
  --e_layers 3 \
  --d_layers 2 \
  --factor 3 \
  --enc_in 22 \
  --dec_in 22 \
  --c_out 22 \
  --gpu 0 \
  --des 'Exp_h64_l3' \
  --p_hidden_dims 32 32 \
  --p_hidden_layers 2 \
  --train_epochs 30 \
  --learning_rate 0.02 \
  --patience 10 \
  --itr 1



# python -u run.py \
#   --is_training 1 \
#   --root_path ./dataset/stock_var/ \
#   --data_path stock.csv \
#   --model_id stock_36_24 \
#   --model ns_Transformer \
#   --data custom \
#   --features MS \
#   --seq_len 36 \
#   --label_len 24 \
#   --pred_len 24 \
#   --e_layers 2 \
#   --d_layers 1 \
#   --factor 3 \
#   --enc_in 22 \
#   --dec_in 22 \
#   --c_out 22 \
#   --gpu 0 \
#   --des 'Exp_h32_l2' \
#   --p_hidden_dims 32 32 \
#   --p_hidden_layers 2 \
#   --train_epochs 20 \
#   --learning_rate 0.03 \
#   --patience 15 \
#   --itr 1 #&

