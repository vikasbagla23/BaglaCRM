from datetime import datetime, timedelta

name = "Vinod Kumar"

birthday = datetime(2026, 11, 23)

start_date = birthday - timedelta(days=3)
end_date = birthday + timedelta(days=3)

hindi_message = f"""
🎁 प्रिय {name} जी,

आपका जन्मदिन आने वाला है।

BAGLA READYMADE CENTRE की ओर से आपको Birthday Week Special Offer के तहत सभी खरीदारी पर अतिरिक्त 5% छूट प्रदान की जा रही है।

यह ऑफर {start_date.strftime('%d %B')} से {end_date.strftime('%d %B')} तक मान्य रहेगा।

हम आपका स्वागत करने के लिए उत्सुक हैं।
"""

english_message = f"""
🎁 Dear {name},

Your birthday is approaching.

As part of the Birthday Week Special Offer from BAGLA READYMADE CENTRE, you are eligible for an EXTRA 5% DISCOUNT on all purchases.

This offer is valid from {start_date.strftime('%d %B')} to {end_date.strftime('%d %B')}.

We look forward to serving you.
"""

print(hindi_message)
print("-" * 60)
print(english_message)
