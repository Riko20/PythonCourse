from string import punctuation
import string, re
import functools

#Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.
def words_deleting():
    f = open("C:/Users/Dragonagek/PycharmProjects/Homework1/text1.txt", "r")
    fintext = open("C:/Users/Dragonagek/PycharmProjects/Homework1/finishedtext.txt", "w")
    new = []               # list со словами, которые будем удалять, проверяем его на чет
    newlist = []           # список окончательно измененных предложений.
    mainlist = []          # список в котором содержатся предложения с файла


    for line in f:
        regex = re.compile('[%s]' % re.escape(string.punctuation))                       #удаление пунктуации и добавление предложений в лист
        b = regex.sub('', line)
        mainlist.append(b)

    for lines in mainlist:
        index = 0
        a = True
        l = lines.split()
        copylist = l.copy()                              # этот список является копией слов с предложений, с которого будут удаляться ненужные слова. Был создан для сохранения итерации
        for word in l:
            if len(word)>=3 and len(word) <= 5:
                index += 1
                copylist.remove(word)
                new.append(word)

        while a:
            if len(new) % 2 == 0:
                new.clear()
                a = False

            else:
                wordik = new.pop(index-1)
                copylist.insert(index-1, wordik)
                new.clear()
                a = True

        newlist.append(copylist)

    for elem in newlist:
        fintext.write("%s\n" % ' '.join(elem))


    f.close()
    fintext.close()

words_deleting()

