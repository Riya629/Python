#encoding
message=input("Enter the message:")
if(len(message)>3):
    message=message[1:]+message[0]
    message="sec"+message
    message=message+"ret"
    
else:
    message=message[::-1]
print("Encoded message", message)


#decoding
message=input("enter the word you want to decode: ")
if(len(message)<3):
     message= message[::-1]
    
else:
    message=message[3:-3]
    message=message[-1]+message[:-1]
print("Decoded message",message)  


#encoding the message
message=input("Enter your messsage: ")
if(len(message)>3):
    message=message[1:]+message[0]
    message="sec"+message+"ret"
    
else:
    message=message[::-1]
print("encoded message:",message)

#decoding
message=input("Enter the encoded message:")
if(len(message)<3):
    message=message[::-1]
else:
    message=message[3:-3]
    message=message[-1]+message[:-1]
print("decoded message:",message)