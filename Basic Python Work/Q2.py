# CMT309 - Courseowrk 1
# Lewis Francis C1826277
# ************************************************************************************
import re
def pluralize(word):
    '''
    Parameters
    ----------
    word : String
    Word which might be pluralised depending if it meets the criteria.

    Returns
    -------
    Returns a dictionary which contains the pluralised input (if the criteria is met) and if it was a success or not.

        
    '''
    # Normalising word so that all of the string is the same in terms of capitalisation
    normalisedWord = word.lower()
    # Creating the dictionary
    dictionary = {'plural': word, 'status': ''}
    # Opening proper_nouns.txt and stripping the nouns so that they can be used in the if search, this is important since I am comparing them to txtList and normalisedWord
    with open('proper_nouns.txt') as properNouns:
        txtList = [(line.strip()).split() for line in properNouns]
        if normalisedWord.split() in txtList and normalisedWord != '':
            dictionary['status'], dictionary['plural'] = 'proper_noun', word
            return dictionary
    # Checking if string is empty
    if word == '':
        dictionary['status'], dictionary['plural'] = 'empty_string', word
        return dictionary
    # Using re to search through normalisedWord and seeing if it is already plural, since we strongly assume that any word ending with s is already plural we see if the normalisedWord ends with s or not
    elif re.search('[a-z]s$', normalisedWord):
        dictionary['status'], dictionary['plural'] = 'already_in_plural', word
        return dictionary
    # Since all prerequisites are met we can assume that the word can be pluralised and therefore start using re.search to find if the inputted string fits any of the set conditions, if so then it is added to the dictionary and returned
    else:
        if re.search('[aeiou]$', normalisedWord):
            dictionary['status'], dictionary['plural'] = 'success', re.sub('$', 's', normalisedWord)
            return dictionary
        elif re.search('[^aeiou]y$', normalisedWord):
            dictionary['status'], dictionary['plural'] = 'success', re.sub('y$', 'ies', normalisedWord)
            return dictionary
        elif re.search('[a-z]f$', normalisedWord):
            dictionary['status'], dictionary['plural'] = 'success', re.sub('f$', 'ves', normalisedWord)
            return dictionary
        elif re.search('[a-z]sh$', normalisedWord):
            dictionary['status'], dictionary['plural'] = 'success', re.sub('$', 'es', normalisedWord)
            return dictionary
        elif re.search('[a-z]z$', normalisedWord):
            dictionary['status'], dictionary['plural'] = 'success', re.sub('$', 'es', normalisedWord)
            return dictionary
        elif re.search('[a-z]ch$', normalisedWord):
            dictionary['status'], dictionary['plural'] = 'success', re.sub('$', 'es', normalisedWord)
            return dictionary
        else:
            dictionary['status'], dictionary['plural'] = 'success', normalisedWord + 's'
            return dictionary


