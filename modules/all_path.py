import inspect;
import openpyxl,sys ,subprocess ,glob ,base64 ,datetime ,time ,os ,signal ,getpass ,logging ,requests ;

path=['openpyxl','base64','datetime','time','os','signal','getpass','logging','requests'];

# for i in range(len(path)):
# 	print inspect.getfile(path[i]);
# 	print


print inspect.getfile(openpyxl);
#inspect.getfile(sys);
print inspect.getfile(subprocess);
print inspect.getfile(glob);
print inspect.getfile(base64);
#inspect.getfile(datetime);
#inspect.getfile(time);
print inspect.getfile(os);
#inspect.getfile(signal);
print inspect.getfile(getpass);
print inspect.getfile(logging);
print inspect.getfile(requests);

# inspect.getfile();

