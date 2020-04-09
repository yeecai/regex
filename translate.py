from translate import Translator
import sys, os
path = "/home/reeman/Public/ReemanWeb/robot_web_ui/src"
fn = os.path.join(path + sys.argv[1])


translator = Translator(from_lang="chinese", to_lang="english")


# todoooooo, read line, translate and readline!!!
line = {}
with open(fn, "r+") as f:
    line = f.readline()
    translation = translator.translate(line.key)
    line[key].writeline()
