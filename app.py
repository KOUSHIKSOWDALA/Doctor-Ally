from flask import Flask, request
import requests
import sys
sys.path.append('nlp/')
from pro import clean_text_using_nlp
from open import report_gen
from smt import gmail_transfer


app = Flask(__name__)

input_text = """
    Uh, doctor..., I been feelin really... um... unwell for some days. Uh, like... like I have this, um, continous headache. The doctor asked how long this had been happening, and the patient replied, Uh... maybe, um, like a week or so? It’s like... it comes and goes, but mostly... um, it stays in the front of my head.The doctor inquired if it was worse at a specific time of day, to which the patient said, Yes, yes... um... mostly mornings. And sometimes... um, when I work for long hours, uh... it like gets real bad. The doctor then asked about other symptoms like nausea or dizziness, and the patient responded, Uh, yes, sometimes... um... I feel like spinning. And... and once, I think I... um, throwed up after the headache got worse. The doctor probed further, asking about sleep issues, and the patient hesitated before saying, No... um, I think I sleep okay, but sometimes, uh... I wake up in... uh, the middle of night with... uh... this pain.The doctor then asked if the patient spent a lot of time on screens, and the patient admtted, Yes, yes, I do, um... for work. It's like... um, I use it for... uh, 8 hours or more. But I take breaks, um, sometimes. The doctor acknowledged this and suggested checking the patient’s blood pressure and eyes, adding that it might be spain or sinus-related. The patient seemed worried and said, Okay, doctor. I... um, hope it’s nothing serious...The doctor reassured them, saying, Don't worry. We'll find the cause and, um, treat it. Let's start with the basics.
"""



@app.route('/')
def hello():
    clean = clean_text_using_nlp(input_text)

    resp = requests.post('https://text-correction-ccu9.onrender.com/correct',json={'text':clean})
    
    data = report_gen(resp.text)

    gmail_transfer(request.form.get('email'), request.form.get('name'), data)
    
    
    print(data)
    return ''
if __name__ == '__main__':
    app.run(debug=True)