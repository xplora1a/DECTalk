import serial
import time



prompts = [
    "We'd love to hear your thoughts on the digital technology exhibition.",
    "Welcome! Please share your insights.",
    "We'd appreciate your comments on our digital showcase.",
    "Hi there! How are you enjoying the exhibition?",
    "Let us know which displays caught your attention and why.",
    "Please tell us what you think of our exhibition.",
    "We'd love to know what you liked best from our digital experience!",
    "Thank you for visiting! Share your impressions with us.",
    "We're all ears! Tell us what sparked your curiosity.",
    "Got a moment? Help us with your valuable feedback.",
    "Please take a second to let us know what you think.",
    "Spot something you love? Tell us about it!",
    "Hi! Please share your thoughts.",
    "Do you remember working with equipment like this? Share your memories with us.",
    "Are you enjoying the show? Let us know!",
    "We're glad you're here! A short comment from you helps us.",
    "Hope the exhibits inspired you! Share your thoughts.",
    "Let us know what you really think!"
]

story1 = [
    "[:np] A California Shaggy Bear Tale for Seven DECtalk Software Voices",
    "by Dennis Klatt ",
    "[:np] Once upon a time, there were three bears. They lived in the great forest and tried to adjust to modern times.", 
    "[:nh] I'm papa bear. I love my family but I love honey best.",
    "[:nb] I'm mama bear. Being a mama bear is a drag.",
    "[:nk] I'm baby bear and I have trouble relating to all of the demands of older bears.",
    "[:np] One day, the three bears left their condominium to search for honey. While they were gone, a beautiful young lady snuck into the bedroom through an open window. ",
    "[:nw] My name is Wendy. My purpose in entering this building should be clear. I am planning to steal the family jewels.",
    "[:np] Hot on her trail was the famous police detective, Frank.",
    "[:nf] Have you seen a lady carrying a laundry bag over her shoulder?",
    "[:np] A woman kneeling with her left ear firmly placed against a large rock responded.",
    "[:nu] No. No one passed this way. I've been listening for earthquakes all morning, but have only spotted three bears searching for honey."
]

story2= [
    "[:phoneme arpabet speak on]",
    "[:np] A California Shaggy Bear Tale for Seven DECtalk Software Voices."
    "By Dennis Klatt.",
    "[:np] Once upon a time, there were three bears. They lived in the great forest and tried to adjust to modern times.",
    "[:nh] I'm papa bear. I love my family, but I love [\"]honey best.",
    "[:nb] I'm mama bear. Being a mama bear is a drag.",
    "[:nk] I'm baby bear and I have trouble relating to all of the demands of older bears.",
    "[:np] One day, the three bears left their condominium to search for honey. While they were gone, a beautiful young lady snuck into the bedroom through an open window.",
    "[:nw] My name is Wendy. My purpose in entering this building should be clear. I am planning to steal the family jewels.",
    "[:np] Hot on her trail was the famous police detective, Frank.",
    "[:nf] Have you seen a lady carrying a laundry bag over her shoulder?",
    "[:np] A woman, kneeling with her left ear firmly placed against a large rock, responded."
    "[:nu] [']No. No [/]one passed this [/ \\]way. I've been listening for [']earthquakes all morning, but have only spotted three bears searching for honey."
]

DECTalk = serial.Serial(port="/dev/USB0", baudrate=9600, bytesize=8, parity="N", stopbits=2, xonxoff=True, rtscts=True)
DECTalk.open()
for prompt in prompts:
    DECTalk.write(prompt)
    DECTalk.flush()
    time.sleep(5)

for line in story1:
    DECTalk.write(line)
    DECTalk.flush()
    time.sleep(5)

for line in story2: 
    DECTalk.write(line)
    DECTalk.flush()
    time.sleep(5)

DECTalk.close()