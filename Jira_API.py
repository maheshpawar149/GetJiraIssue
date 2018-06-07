#import sys;
#import requests,json;


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
		print "+++++++++++++++++++++++++++++++++++++++++++++"
		if (statusVal=="Request In Execution"):
			print "Request Found";
			DurationValue=str(json_data['fields']['customfield_10207'])
			EnvValue=json_data['fields']['customfield_10208']['value']
			DurValue=json_data['fields']['customfield_10209']['name']

			print statusVal;
			print DurationValue;
			print EnvValue;
			print DurValue;
		#else:
			#print "No request Found in Jira Project!!!."

	
main();
##***End of File***

			
