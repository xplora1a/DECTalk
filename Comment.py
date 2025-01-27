import serial
import time



prompts = [
    "Hello! We'd love to hear your thoughts on today's digital technology exhibition.",
    "Welcome! Your feedback helps us make our exhibits better. Please share your insights.",
    "Thank you for stopping by. We'd appreciate a moment of your time to let us know how we're doing.",
    "Hi there! How are you enjoying the exhibition? Your opinion matters to us.",
    "Your voice counts! Let us know which displays caught your attention and why.",
    "We hope you're having a great time. Please tell us what you think of our exhibition.",
    "Ready to share your thoughts? We'd love to know what you liked best from our digital experience!",
    "Thank you for visiting! Share your impressions with us.",
    "We're all ears! Tell us what sparked your curiosity.",
    "Got a moment? Help us with your valuable feedback.",
    "Your visit is important to us. Please take a second to let us know what you think.",
    "Spot something you love? Tell us about it!",
    "Hi! Your feedback creates better experiences. Please share your thoughts.",
    "Hello there! We can improve future technology showcases with your quick feedback.",
    "Are you enjoying the show? Let us know what stands out for you.",
    "We're glad you're here! A short comment from you helps us.",
    "Where can we improve? Your suggestions help us design the best exhibitions possible.",
    "Hope the exhibits inspired you! Please tell us how we can enhance your experience.",
    "Your feedback helps us innovate. Share your perspective.",
    "Are we meeting your expectations? Let us know what you really think!"
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