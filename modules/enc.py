# import Crypto;
# #from Crypto.Cipher import AES
# obj=AES.new("key1",AES.MODE_CFB,'key2');
# msg="admin:BoneBone1$";
# ciT=obj.encrypt(msg);
# print obj;print
# print ciT

# obj2=AAES.new("key1",AES.MODE_CFB,'key2');
# obj2.secrypt(ciT);
# print obj2;


# from simplecrypt import encrypt, decrypt
# ciphertext=encrypt("key","admin:BoneBone1$");
# print ciphertext;

# mytext=decrypt('key',ciphertext)

# print mytext;
import sys;
sys.path.append('.');
sys.path.append('dist-packages');
import logging;

myLogger = logging.getLogger('myapp')
handler = logging.FileHandler('envStatusLog.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
myLogger.addHandler(handler) 
myLogger.setLevel(logging.INFO)
myLogger.info('***********************************');
myLogger.info('***Starting Script***');


from cryptography.fernet import Fernet
# cipher_key = Fernet.generate_key()
# #cipher_key="key";
# print "Cipher Key: %s"%cipher_key;



# text = 'admin:BoneBone1$';
# "Cipher Text/Secret: %s"%text;
# encrypted_text = cipher.encrypt(text)


with open("key2.txt",mode="r") as userFile:
	data=userFile.read().splitlines();


cipher_key=data[0];
encrypted_text=data[1];

cipher = Fernet(cipher_key)
print "Cipher : %s"%cipher;

print"Encrypted TEXT: %s"% encrypted_text


decrypted_text = cipher.decrypt(encrypted_text)

print "Decrypted TEXT: %s"%decrypted_text;



