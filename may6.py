
def noYelling(texto):
    pontuacao = ['!', '?']
    while True:
        if texto[-1] in pontuacao and texto[-2] in pontuacao:
            texto = texto[:-1]
            continue
        else:
            break
    print(texto)

noYelling("What went wrong?????????")
output = "What went wrong?"

noYelling("Oh my goodness!!!")
output = "Oh my goodness!"

noYelling("I just!!! can!!! not!!! believe!!! it!!!")
output = "I just!!! can!!! not!!! believe!!! it!"
# Only change repeating punctuation at the end of the sentence.

noYelling("Oh my goodness!")
output = "Oh my goodness!"
# Do not change sentences where there exists only one or zero exclamation marks/question marks.

#like why did this took me so long wtf?????? 