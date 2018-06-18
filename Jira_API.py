import glob,os,base64,requests

def GetUserPass():
	from cryptography.fernet import Fernet
	with open("ConflConfig.json",mode="r") as userFile:
		data=userFile.read().splitlines();
	#For member User
	cipher_key=data[0];
	encrypted_text=data[1];
	
	cipher = Fernet(cipher_key)
	decrypted_text = cipher.decrypt(encrypted_text)
	userpass=base64.b64encode(decrypted_text);	
	return userpass;

#for infile in glob.glob(os.path.join('Logs/*.txt'))
files =glob.glob('Logs/*');
files.sort(key=os.path.getmtime);
#print (files);
#print files[0]
#print("\n".join(files))

##Reading File
# with open(files[0]) as f:
# 	for line in f:
# 		print line.strip()

# f=open(files[0]);
# #next=f.read(1)
# next =f.readline();
# while next!="":
# 	print (next)
# 	next=f.readline();
print files[0];
in_file=open(files[0],'r')

fileData=[];
contents=in_file.readlines();
print contents;


nowEnvStr="- CLSNOW ENV SPACE USAGE";
nowCoreDBStr="- CLSNOW CORDB SPACE USAGE";
nowCoreDBLogStr="- CLSNOW CORDBLOG SPACE USAGE";
nowEnvDataL=[];nowCoreDBDataL=[];nowCoreDBLogDataL=[];
for i in range(len(contents)):
	fileData.append(contents[i].strip('\n'))
	
in_file.close()

for i in range(len(fileData)):
	try:
		if nowEnvStr in fileData[i]:		
			i=i+4;		
			while fileData[i]!="":			
				nowEnvDataL.append(fileData[i]);
				i=i+1;
		
		if nowCoreDBStr in fileData[i]:
			i=i+4;	
			while fileData[i]!="":
				nowCoreDBDataL.append(fileData[i]);
				i=i+1;

		if nowCoreDBLogStr in fileData[i]:
			i=i+4;	
	 		while fileData[i]!="":
	 			nowCoreDBLogDataL.append(fileData[i]);
	 			i=i+1;

	except IndexError as e:
		pass
	
print "nowEnvDataL"; print "*************";print nowEnvDataL;
print "nowCoreDBDataL"; print "*************";print nowCoreDBDataL;
print "nowCoreDBLogDataL"; print "*************";print nowCoreDBLogDataL;

#print nowEnvDataL;
#for i in len(nowEnvDataL):

##Reading & updating Excel
userpass=GetUserPass();
urlIP= 'http://10.20.3.112:8091';
headers={'Authorization':'Basic %s'% userpass }
filePath="CLSNow_Dev_Environment_Allocation_Status.xlsx";
response = requests.get(urlIP+'/download/attachments/917506/'+filePath,headers=headers);

# print fileData[0:3];
# print "CLSNOW Env:"
# print fileData[5:11];
# print "CLSNOW CoreDB:"
# print fileData[17:23];
# print "CLSNOW CoreDBLog"
# print fileData[29:35];

