import sys;
import requests,json;

#Jira_Tickets=["EAP-3","EAP-4","EAP-5","EAP-6","EAP-7"];
global Jira_Tickets;
Jira_Tickets=["CEA-1","CEA-6","CEA-7","CEA-8","CEA-9","CEA-10","CEA-11","CEA-12",];
global server;
server="http://10.20.3.0:8181";
timeZonecal="";
dataC="";dataD="";dataT="";

#main();

Jira_Tickets='CEA-1'
#headers={'Authorization':'Basic YWRtaW46Qm9uZUJvbmUxJA==','content-type' : 'application/json'} 
headers={'Authorization':'Basic YWRtaW46Qm9uZUJvbmUxJA==','Cache-Control': 'no-cache,no-store, no-transform','Content-Security-Policy': 'frame-ancestors','Content-Type': 'application/json;charset=UTF-8'}
response = requests.get(server+'/rest/api/2/issue/'+Jira_Tickets+'?expand=changelog',headers=headers);
json_data=json.loads(response.content);
#print json_data['fields']['priority']['name'];
#print json_data['fields']['assignee']['name'];
print "***************";


## 1. For Assignee
data={"fields": {"assignee": { "name": "MahEnvTeam2" }}}
data=json.dumps(data);
response = requests.put('http://10.20.3.0:8181/rest/api/2/issue/'+Jira_Tickets,headers=headers,data=data);

print response.content;


## 2. For Comment
dataC={"body": "h5. ADDING Some Comments"}
response = requests.post(server+'/rest/api/2/issue/'+Jira_Tickets+'/comment',headers=headers,data=dataC);


## 3. For Status
dataT={"transition": {"id":"161"}}
response = requests.post(server+'/rest/api/2/issue/'+Jira_Tickets+'/transitions?expand=transitions.fields',headers=headers,data=dataT);
