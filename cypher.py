text='hello'
custom_key='happy'
def cypher(message,key,direction=1):
  key_index=0;
  alphabet='abcdefghijklmnopqrstuvwxyz'
  final_message=' '
  for char in message.lower():
    if not char.isalpha():
      final_message+=char
    else:
      key_char=key[key_index%len(key)]
      key_char+=1
      
