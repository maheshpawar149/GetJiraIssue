import sys;
import requests,json;


def main():
	Jira_Tickets=["EAP-3","EAP-4","EAP-5","EAP-6","EAP-7"];

	for i in range(len(Jira_Tickets)):
		headers={'Authorization':'Basic YWRtaW46Qm9uZUJvbmUxJA=='}
		response = requests.get('http://10.20.2.237:8181/rest/api/2/issue/'+Jira_Tickets[i],headers=headers);
	
		json_data=json.loads(response.content);

		#for i in json_data:
			#print ("%s: %s" % (i,json_data[i]))

		
		print Jira_Tickets[i];
		statusVal=json_data['fields']['status']['name']
		
		if (statusVal=="Request In Execution"):
			print "Request Found";
			UserName=str(json_data['fields']['creator']['name']);
			Usermail=str(json_data['fields']['creator']['emailAddress']);
			GroupName=str(json_data['fields']['customfield_10209']['name']);
			RequestType=str(json_data['fields']['issuetype']['name']);
			DurationValue=str(json_data['fields']['customfield_10207']);
			EnvValue=str(json_data['fields']['customfield_10208']['value']);
			
			print "+++++++++++++++++++++++++++++++++++++++++++++"
			print UserName;
			print Usermail;
			print GroupName;
			print RequestType;
			print statusVal;
			print DurationValue;
			print EnvValue;			
			print "+++++++++++++++++++++++++++++++++++++++++++++"
			print "CALL 'ENVAllocation_Script.py' HERE with above parameters!!!";

			print "Result of the Script passes to JiraComments";
			#print "Request Processed for %s,%s,%s,%s,%s,%s,%s"%(UserName,Usermail,GroupName,RequestType,statusVal,DurationValue,EnvValue);

			headers={'Authorization':'Basic YWRtaW46Qm9uZUJvbmUxJA==','content-type' : 'application/json'} #'X-Atlassian-Token': 'nocheck',
					#,'content-type': 'application/json'}
			#headers = {'content-type' : 'application/json'}
			#data={"body": "TEST Comment",}
			# data=[ {"body": "TEST Comment",
  	# 			"visibility": {
  	# 				 "type": "role",
  	# 				 "value": "Administrators"
  	# 				 }
  	# 			}],

			data={"body": "Request Processed for %s,%s,%s,%s,%s,%s,%s"%(UserName,Usermail,GroupName,RequestType,statusVal,DurationValue,EnvValue),
					"visibility": {
						"type": "role",
						"value": "Administrators"
						}
					}
			response = requests.post('http://10.20.2.237:8181/rest/api/2/issue/'+Jira_Tickets[i]+'/comment',headers=headers,data=json.dumps(data)); #auth=auth
			
			

		#else:
			#print "No request Found in Jira Project!!!."


main();
##***End of File***

			
