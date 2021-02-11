# hash_table = list([0 for _ in range(10)])
# print(hash_table)
#
# def hash_func(key):
#     return key % 5
#
# data = 'Andy'
# def storage(data,value):
#     key = ord(data[0])
#     hash_adress = hash_func(key)
#     hash_table[hash_adress] = value

hash_table = list([0 for _ in range(8)])
def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data,value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
read_data('Dave')

print(hash_table)

#SHA-1 해쉬에서 안전한 알고리즘
import hashlib

data = 'encode'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
# hash_object.update(b'test')  위에꺼랑 같음
hex_dig = hash_object.hexdigest()
print (hex_dig)