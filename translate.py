from googletrans import Translator

translator = Translator()

def translate(text, source, destination):

    translation = translator.translate(text.split(" "), dest=destination, src=source)

    lst = []
    for t in translation:
        dic = {}
        dic['word'] = t.origin
        dic['trans'] = t.text
        lst.append(dic)
    return lst



