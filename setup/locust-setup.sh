sudo apt update 
sudo apt upgrade 
sudo apt install supervisor 
sudo apt install python3 
sudo apt install python3-pip
sudo pip3 install -r requirements.txt
sudo systemctl enable supervisor 
sudo systemctl start supervisor
sudo mv locust.conf /etc/supervisor/conf.d/locust.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl stop all
sudo supervisorctl status
echo "
____________________________________________
*******************************************
Only start the process Which you want 

To Start Locust master on this master machine
use below command:
~$ sudo supervisorctl start locust-master

OR

To Start Locust Worker on this worker machine
use below command:
~$ sudo supervisorctl start locust-worker

******________********_________********
"
