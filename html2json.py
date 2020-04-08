import re, sys, os, codecs, json
from translate import Translator

path = "your file path"

reload(sys)
sys.setdefaultencoding('utf-8')

fn = os.path.join( path + sys.argv[1])
    
regex = r'<\s*Button[^>]*>(.*?)<\s*/\s*Button>'
with open(fn, "r") as f:
    text = f.read()
    html_str = re.sub(r'<br>', ' ' , text)
    relt = re.findall(regex, html_str)
    
list(set(relt))

data = {}

translator= Translator(from_lang="chinese",to_lang="english")

for x in range(len(relt)): 
    translation = translator.translate(relt[x])
    data[relt[x]]= translation
    result = json.dumps(data, ensure_ascii=False, indent=2)


with codecs.open("result.json", "w", 'utf-8') as f:
    f.write(result)
