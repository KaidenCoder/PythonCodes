
#ipAddress = input("Please enter an IP address: ")
input_prompt = ("Please enter an IP address. An IP address consists of 4 numbers, "
                "separated from each other with a full stop: ")
ipAddress = input(input_prompt)
if ipAddress[-1] != '.':
    ipAddress += '.'                

segment = 1
segment_length = 0
#character = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} chracters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

if character != '.':            
    print("segment {} contains {} characters".format(segment, segment_length))