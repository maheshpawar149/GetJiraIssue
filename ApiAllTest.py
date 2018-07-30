import sys;
import requests,json;
from requests.auth import HTTPBasicAuth

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
#headers={'Authorization':'Basic YWRtaW46Qm9uZUJvbmUxJA==','Cache-Control': 'no-cache,no-store, no-transform','Content-Security-Policy': 'frame-ancestors','Content-Type': 'application/json;charset=UTF-8'}
#headers={ 'Authorization':'Basic cmFqZXNoX2s6Qm9uZUJvbmUxJA=='};
headers={'Authorization':'Basic cmFqZXNoX2s6Qm9uZUJvbmUxJA==','Cache-Control': 'no-cache,no-store, no-transform','Content-Security-Policy': 'frame-ancestors','Content-Type': 'application/json;charset=UTF-8'}
auth=HTTPBasicAuth('rajesh_k','BoneBone1$');

response = requests.get(server+'/rest/api/2/issue/'+Jira_Tickets+'?expand=changelog',headers=headers);
json_data=json.loads(response.content);
#print json_data['fields']['priority']['name'];
#print json_data['fields']['assignee']['name'];
print "***************";

Jira_Tickets='EAP-7';
data={"update":{"summary":[{"set":"New Summary"}],"comment":[{"add":{"body":"New Comment"}}]}}
#data={"update":{"summary":[{"set":"New Summary"}]}};
data=json.dumps(data);
response=requests.put(server+'/rest/api/2/issue/'+Jira_Tickets,headers=headers,data=data)
print response.content;
print "***************";
sys.exit();


response = requests.get('http://10.20.3.0:8181/rest/api/2/user?username=rajesh_k',headers=headers)
data=json.loads(response.content);
#print data;
print data['timeZone'];


## 2. For Comment
dataC={"body": "h5 ADDING Some Comments"}
dataC=json.dumps(dataC);
response = requests.post(server+'/rest/api/2/issue/'+Jira_Tickets+'/comment',headers=headers,data=dataC);
print response.content;

print "***************";

sys.exit();

print "***************";
## 1. For Assignee
data={"fields": {"assignee": { "name": "MahEnvTeam2" }}}
data=json.dumps(data);
response = requests.put(server+'/rest/api/2/issue/'+Jira_Tickets,headers=headers,data=data);
print response.content;

print "***************";
## 2. For Comment
dataC={"body": "h5. ADDING Some Comments"}
response = requests.post(server+'/rest/api/2/issue/'+Jira_Tickets+'/comment',headers=headers,data=dataC);
print response.content;

print "***************";
## 3. For Status
dataT={"transition": {"id":"161"}}
response = requests.post(server+'/rest/api/2/issue/'+Jira_Tickets+'/transitions?expand=transitions.fields',headers=headers,data=dataT);
print response.content;


sys.exit();
























#data={"fields":{"priority": {"id": "Critical"}}};
#data={"priority": {"name": "Critical"}};
#data={"update":{"priority":[{"set":{"id":1}}]}};
#data={    "fields": {       "priority":       {           "id": "1"       }    }};
#data={"update":{"priority":[{"set":{"name" : "Minor"}}]}}
#data=
#data={"update":{"customfield_10208":[{"value": "CUT05"}]}};
#data={"fields": {"customfield_10400": [{"set": "BBBB"}]}};
#data={"fields": {"customfield_10400": "BBB"}};
#data={"fields": {"customfield_10400": [{"set": "BBBB"}]}};
#data={"fields": {"customfield_10400": "BBBB"}};
#data={"fields": {"customfield_10400": "CCCCCCCC"}	};


#data={"fields": {"customfield_10208": [{ "value" : "CUT05"}]}};
data={
    "fields": {
      "customfield_10208": { 
        "value": "CUT13"
      }
    }
  }
#data={"fields": {"customfield_10208": {"value": "CUT01"}}}

#data={"fields": {"customfield_10208": { "value": "CUT05" }}}
#data=json.dumps({"fields":{"customfield_10208": { "value": "CUT05" }}});
data={"fields": {"customfield_10208": { "value": "CUT13" }}}
data=json.dumps(data);
response = requests.put('http://10.20.3.0:8181/rest/api/2/issue/'+Jira_Tickets[i],headers=headers,data=data);
print response.content;	
print "***************";

response = requests.get(server+'/rest/api/2/issue/'+Jira_Tickets[i]+'?expand=changelog',headers=headers);
json_data=json.loads(response.content);
print json_data['fields']['customfield_10208']['value'];


sys.exit()



def updatejira(Jira_Tickets,dataC,dataD,dataT):
	print "in update";
	dataC=json.dumps(dataC);
	dataD=json.dumps(dataD);
	dataT=json.dumps(dataT);

	##for decription
	response = requests.put(server+'/rest/api/2/issue/'+Jira_Tickets,headers=headers,data=dataD);
	print response.content;	

	##for comments
	if (dataC!=""):
		print "Adding Comment"
		response = requests.post(server+'/rest/api/2/issue/'+Jira_Tickets+'/comment',headers=headers,data=dataC);
		#print response.content;
		
	##for transition
	if (dataT!=""):
		print "Changing Status"
		response = requests.post(server+'/rest/api/2/issue/'+Jira_Tickets+'/transitions?expand=transitions.fields',headers=headers,data=dataT);
		#print response.content;
	
	#break;
	
def main():
	global headers;
	dataC="";dataD="";dataT="";success="";
	#headers={'Authorization':'Basic YWRtaW46Qm9uZUJvbmUxJA=='}
	headers={'Authorization':'Basic YWRtaW46Qm9uZUJvbmUxJA==','content-type' : 'application/json'} 
	
	Jira_Tickets=['CEA-13'];
	for i in range(len(Jira_Tickets)):
		response = requests.get(server+'/rest/api/2/issue/'+Jira_Tickets[i]+'?expand=changelog',headers=headers);
		##response = requests.get('http://10.20.2.237:8181/rest/api/2/issue/Test-3?fields=description',headers=headers);
		json_data=json.loads(response.content);
		log_length=len(json_data['changelog']['histories']);
		statusVal=json_data['changelog']['histories'][log_length-1]['items'][0]['toString'];
		UserName=str(json_data['changelog']['histories'][log_length-1]['author']['name']);
		Usermail=str(json_data['changelog']['histories'][log_length-1]['author']['emailAddress']);
		GroupName=str(json_data['fields']['customfield_10209']['name']);
		#RequestType=str(json_data['fields']['issuetype']['name']);
		DurationValue=str(json_data['fields']['customfield_10207']);
		EnvValue=str(json_data['fields']['customfield_10208']['value']);
		
		
		print "************************";
		print Jira_Tickets[i];
		print statusVal;
		desc=str(json_data['fields']['description']);
		print desc;
		print "************************";


		s=desc.split("|");
		print s[3]

		sys.exit();


		if (statusVal=="New Request for Environment"):
			print "NEW Request";
			data={"update": {"description": [{"set": "||{color:#008000}REQUEST IS IN PROCESS{color}||\n\n |h5. FROM: | |h6. %s,%s,|\n|h5. ENV: | |h6. %s|\n|h5. FOR: | |h6. %s hrs|"%(UserName,GroupName,EnvValue,DurationValue),}]}}			
			updatejira(Jira_Tickets[i],dataC,"","");

		elif (statusVal=="Request In Execution"):
			print "Request Found";
			ReqCat="ENV_Request";
			success=False;
			if(success==True):
				dataC={"body": "||{color:#008000}START USING ENV(/){color}||\n\n FROM: %s,%s,\nENV: %s\nFOR:%s hrs"%(UserName,GroupName,EnvValue,DurationValue),}
				dataD={"update": {"description": [{"set": "||{color:#008000}REQUEST APPROVED START USING ENV(/){color}||\n\n |h5. FROM: | |h6. %s,%s,|\n|h5. ENV: | |h6. %s|\n|h5. FOR: | |h6. %s hrs|"%(UserName,GroupName,EnvValue,DurationValue),}]}}
				dataT={"transition": {"id":"201"}}
			elif(success==False):
				error_msg="Found Error:"
				dataC={"body": "||{color:red}%s(x){color}||\n FROM: %s,%s,\nENV: %s\nFOR:%s hrs"%(error_msg,UserName,GroupName,EnvValue,DurationValue),}
				dataD={"update": {"description": [{"set": "||{color:red}%s(x){color}||\n\n |h5. FROM: | |h6. %s,%s,|\n|h5. ENV: | |h6. %s|\n|h5. FOR: | |h6. %s hrs|"%(error_msg,UserName,GroupName,EnvValue,DurationValue),}]}}
				dataT={"transition": {"id":"131"}}

			updatejira(Jira_Tickets[i],dataC,dataD,dataT);

		elif(statusVal=="Env Released"):
			print "In Env Released Request";
			ReqCat="Release_Request";
			if(success==True):
				dataC={"body": "||{color:#008000}ENV RELEASED(/){color}||\n\n FROM: %s,%s,\nENV: %s\nFOR:%s hrs"%(UserName,GroupName,EnvValue,DurationValue),}
				dataD={"update": {"description": [{"set": "||{color:#008000}ENV RELEASED(/){color}||\n\n |h5. FROM: | |h6. %s,%s,|\n|h5. ENV: | |h6. %s|\n|h5. FOR: | |h6. %s hrs|"%(UserName,GroupName,EnvValue,DurationValue),}]}}
				dataT={"transition": {"id":"111"}}
			elif(success==False):
				error_msg="Found Error:Try Again"
				dataC={"body": "||{color:red}%s(x){color}||\n FROM: %s,%s,\nENV: %s\nFOR:%s hrs"%(error_msg,UserName,GroupName,EnvValue,DurationValue),}
				dataD={"update": {"description": [{"set": "||{color:red}%s(x){color}||\n\n |h5. FROM: | |h6. %s,%s,|\n|h5. ENV: | |h6. %s|\n|h5. FOR: | |h6. %s hrs|"%(error_msg,UserName,GroupName,EnvValue,DurationValue),}]}}
				#######CHECK TRASNS ID
				dataT={"transition": {"id":"201"}}
			updatejira(Jira_Tickets[i],dataC,dataD,"");

		elif(statusVal=="Request Extension"):
			ReqCat="Extend_Request";
			print "Request Extension Request";
			dataC={"body": "||{color:orange}WAITING FOR APPROVAL FROM ENV TEAM (/){color}||\n FROM: %s,%s,\nENV: %s\nFOR:%s hrs"%(UserName,GroupName,EnvValue,DurationValue),}
			dataD={"update": {"description": [{"set": "||{color:orange}WAITING FOR APPROVAL FROM ENV TEAM (/){color}||\n\n |h5. FROM: | |h6. %s,%s,|\n|h5. ENV: | |h6. %s|\n|h5. FOR: | |h6. %s hrs|"%(UserName,GroupName,EnvValue,DurationValue),}]}}
			updatejira(Jira_Tickets[i],dataC,dataD,"");

		else:
			print("No Update");
			#break;

main();
