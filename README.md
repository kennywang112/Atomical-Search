1. git clone https://github.com/atomicals/atomicals-js.git
2. npm install -g yarn
3. yarn install
4. yarn run build
5. yarn cli wallet-init

1. yarn cli get-container-item "scientists" "xxx" 
if status = null, mint
2. yarn cli mint-item "#scientists" "xxx" "./JSON" item-xxx.json --satsbyte=20
wait for the block confirmed, then check again
3. yarn cli get-container-item "scientists" "xxx"
if status = pending, and candidate atomical id is yours, do pay
4. yarn cli transfer-builder --atomicalreceipt <atomical id> --owner funding --atomicalreceipttype d --satsbyte=30
5. choose a utxo amount that > 27777
then check again
6. yarn cli get-container-item "scientists" "xxx" 

## Run script
1. chmod +x script.sh
2. ./script.sh