sudo apt update 
sudo apt upgrade 
sudo apt install supervisor 
sudo apt install python3 
sudo apt install python3-pip
sudo systemctl enable supervisor 
sudo systemctl start supervisor
sudo mv locust.conf /etc/supervisor/conf.d/locust.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status
