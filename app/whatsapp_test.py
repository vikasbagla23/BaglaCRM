import pywhatkit

phone = "+918306821033"

message = """
🎉 TEST MESSAGE

BAGLA READYMADE CENTRE

WhatsApp automation is working successfully.
"""

pywhatkit.sendwhatmsg_instantly(
    phone,
    message,
    wait_time=20,
    tab_close=False
)