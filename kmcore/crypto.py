from Crypto.Cipher import AES
from binascii import hexlify,unhexlify

key=b'625202f9149maomi'
iv=b'5efd3f6060emaomi'

def padding_pkcs5(value):
  BS=AES.block_size
  return str.encode(value+(BS-len(value)%BS)*chr(BS-len(value)%BS),encoding='utf-8')

def encrypt(raw):
  raw=padding_pkcs5(raw)
  aes=AES.new(key=key,iv=iv,mode=AES.MODE_CBC)
  return hexlify(aes.encrypt(bytes(raw))).decode('utf-8','ignore')

def decrypt(raw):
  aes=AES.new(key=key,iv=iv,mode=AES.MODE_CBC)
  return aes.decrypt(unhexlify(raw)).decode('utf-8','ignore')