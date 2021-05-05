from googletrans import Translator

translator = Translator()

def translate(text, source, destination):

    translation = translator.translate(text.split(" "), dest=destination, src=source)

    dic = {}
    for t in translation:
        dic[t.origin] = t.text

    return dic



