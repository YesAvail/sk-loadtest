# sk-loadtest

### Repository for Streamkast load Testing Files

- Spreadsheet link - https://docs.google.com/spreadsheets/d/1IxYGV4qMNyfr3XgSvZdt07IXn2PMnaZqrheJPJURDRo/
- Folder link - https://drive.google.com/drive/folders/1cJgQkp-cKe46l4kuJNYOMkacaeV4rqvY


### To set up master or worker node/Machine/Client

__*Use below commands (Works in ubuntu env)*__


` git clone https://github.com/YesAvail/sk-loadtest.git `

` cd sk-loadtest/setup/ `

` sudo ./locust-setup.sh `

**After all the installation is done** use one of the below command: 

- To Start Locust master on this master machine
use below command:
` sudo supervisorctl start locust-master `

**_OR_**

- To Start Locust Worker on this worker machine
use below command:
` sudo supervisorctl start locust-worker `


*Whooola ! your machines have been set up for use*.