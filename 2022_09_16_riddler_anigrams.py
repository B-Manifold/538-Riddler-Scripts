#Script for solving the Anigrams Riddler Classic from 2022_09_16
#https://fivethirtyeight.com/features/can-you-build-the-biggest-anigram/


###importing and sorting (by length) the norvig dictionary of words with 4 or more characters
with open('norvig_4up_words.txt') as d:
    norvig = d.readlines()
    d.close()

i = 0

while i < len(norvig):
    norvig[i] = norvig[i].replace('\n','')
    i += 1

def len_sort(e):
    return len(e)

norvig.sort(key=len_sort)
##
##i = 0
##words4 = []
##
##while len(norvig[i]) == 4:
##    words4.append(norvig[i])
##    i += 1


########
#Functions useful for sorting through the dictionary
########

def if_intersect(worda, wordb):
    '''returns true if worda is an anagram of wordb with the addition of a letter

        note: len(wordb) = len(worda) + 1
        str, str -> bool'''
    worda = list(worda)
    wordb= list(wordb)
    for c in worda:
        try:
            wordb.remove(c)
        except ValueError:
            return False
        else:
            continue
    return True

def lengthplusone_pointer(word_length, norvig):
    '''returns the integer index value at which words of word_length + 1 start appearing in norvig


    int -> int'''
    i = 0
    while len(norvig[i]) <= word_length:
        i += 1
    return i

def word_hunter(word_length, norvig):
    '''returns a list of words of length word_length + 1 that can be formed from the words of length word_length within norvig

    int, list of strs -> list of strs'''
    unique_iwords = []
    for wordj in norvig[lengthplusone_pointer(word_length,norvig):lengthplusone_pointer(word_length+1,norvig)]:
        #print(wordj)
        for wordi in norvig[lengthplusone_pointer(word_length-1,norvig):lengthplusone_pointer(word_length,norvig)]:
            #print(wordi)
            if if_intersect(wordi, wordj):
                pair = [wordi,wordj]
                unique_iwords.append(pair)
                #print(pair)
                break
            else:
                continue
    return unique_iwords

def word_hunter_len(word_length, norvig):
    '''returns the number of unique words of length (word_length + 1) that can be formed from the words of length word_length within norvig

    int, list of strs -> list of strs'''
    unique_iwords = []
    print("There are " + str(len(norvig[lengthplusone_pointer(word_length,norvig):lengthplusone_pointer(word_length+1,norvig)])) + " " + str(word_length+1) +"-letter words to try in combination with " + str(len(norvig[lengthplusone_pointer(word_length-1,norvig):lengthplusone_pointer(word_length,norvig)])) + " " + str(word_length) + "-letter words.")
    for wordj in norvig[lengthplusone_pointer(word_length,norvig):lengthplusone_pointer(word_length+1,norvig)]:
        for wordi in norvig[lengthplusone_pointer(word_length-1,norvig):lengthplusone_pointer(word_length,norvig)]:
            if if_intersect(wordi, wordj):
                unique_iwords.append(wordi)
                break
            else:
                continue
    return len(unique_iwords)

########
#Script for finding words that can be anigramed from words with one fewer letter
########

i = 24
while i >= 10:
    #print("There are " + str(word_hunter_len(i,norvig)) + " unique " + str(i + 1) +"-letter words that can be anigramed from " + str(i) + "-letter words.")
    print(str(i+1) + "-letter anigramable words and their " + str(i) + "-letter pair")
    print(word_hunter(i,norvig))
    i = i -1
