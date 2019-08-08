import pwn

greeting_msg = "You have now entered the Duck Web and you're in for a honkin good time. Can you figure out my trick"
xor_string = ')\x06\x16O+50\x1eQ\x1b[\x14K\b]+VGWP\x16MQQ]'

print pwn.xor(greeting_msg, xor_string)