sudo apt update || apt update
sudo apt upgrade || apt upgrade
sudo apt install supervisor || apt install supervisor
sudo apt install python3 || apt install python3
sudo apt install python3-pip || apt install python3-pip
sudo pip3 install -r requirements.txt || pip3 install -r requirements.txt
sudo systemctl enable supervisor || systemctl enable supervisor
sudo systemctl start supervisor || systemctl start supervisor
sudo mv locust.conf /etc/supervisor/conf.d/locust.conf || mv locust.conf /etc/supervisor/conf.d/locust.conf
sudo supervisorctl reread || supervisorctl reread
sudo supervisorctl update || supervisorctl update
sudo supervisorctl stop all || supervisorctl stop all
sudo supervisorctl status || supervisorctl status
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
