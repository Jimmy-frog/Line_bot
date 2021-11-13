
# 下載egrok套件
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip

# 呼叫ngrok
sudo chmod u+x ngrok
./ngrok http --region ap 8080