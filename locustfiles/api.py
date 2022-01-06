from locust import HttpUser, task, constant_pacing, constant_throughput

class NUser(HttpUser):
    wait_time = constant_pacing(60)

    def on_start(self):
  	  # Send login request
        headers = {'streamkast-channel-id': 'eb279f3b-3259-47a6-9382-986a736db7f6'}
        response = self.client.post("/authorizations/-/test", headers=headers, json={"authorizationTestToken": "adminsecret"})
        self.authToken = response.json()['accessToken']
        self.client.headers = {
            "Authorization": "Bearer "+self.authToken,
            "streamkast-channel-id": "eb279f3b-3259-47a6-9382-986a736db7f6"
        }
      
    
    @task
    def health(self):
        print("CLient header for /health \n",self.client.headers)
        rep = self.client.get("/health")
        print("************** Status Code = ",rep.status_code,"**********")
        print(rep.text)
        print("*****************************************************")

    
    @task
    def fqdn(self):
        print("CLient header for /fqdn \n",self.client.headers)
        rep = self.client.get("/fqdn/zero.lt.streamkast.dev")
        print("************** Status Code = ",rep.status_code,"**********")
        print(rep.text)
        print("*****************************************************")


    @task
    def me(self):
        print("CLient header for /me \n",self.client.headers)
        rep = self.client.get("/me")
        print("************** Status Code = ",rep.status_code,"**********")
        print(rep.text)
        print("*****************************************************")
    

    @task
    def events(self):
        print("CLient header for /events \n",self.client.headers)
        rep = self.client.get("/events")
        print("************** Status Code = ",rep.status_code,"**********")
        print(rep.text)
        print("*****************************************************")
    
    
    # @task
    # def events_all(self):
    #     headers = self.client.headers.copy()
    #     headers['Authorization'] = "Bearer t1.eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NDEyOTQ0MTIsImV4cCI6MTY0MTM4MDgxMiwiY2hhbm5lbElkIjoiYWxsIiwidXNlcklkIjoiMWRiM2RlMTYtYWI5Ni00NzBhLWJmNTQtYzMzZmFkYThjYjI1In0.Uwytk0xLJuvXMfm5I66v21TStspq6yxrtKgNG2PJzoSfNWsGRZKqk5cB8MZ2jmqXeObNIvb477Q7RjgmZiHuEQ"
    #     headers['streamkast-channel-id'] = "all"
    #     print("CLient header for /all Events \n",headers)
    #     rep = self.client.get("/events", headers=headers)
    #     print("************** Status Code = ",rep.status_code,"**********")
    #     print(rep.text)
    #     print("*****************************************************")


    @task
    def events_id(self):
        print("CLient header for /ID Events \n",self.client.headers)
        rep = self.client.get("/events/cbe85f2f-6231-497f-aefd-dd54dd7697c1?includeFields=eventParticipant&includeFields=eventPurchase", headers=self.client.headers)
        print("************** Status Code = ",rep.status_code,"**********")
        print(rep.text)
        print("*****************************************************")



    