telephones = """+351 123 321 123; 
    +351 220 121 212;
    +351 921 124 356;
    +351 919 919 828;
    +44 0 113 32 242
    """

new_telephones = telephones.replace("+351", "00351")

print("Before: %s" % telephones)
print("After: %s" % new_telephones)
