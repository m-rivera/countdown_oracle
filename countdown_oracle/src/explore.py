import nltk
import itertools

true_words = nltk.corpus.words.words()

def permut_words(in_str):
    """
    Return all English words contained in the string of letters.

    Each letter is used only once.

    Parameters
    ----------
    in_str : str
        All of the input letters in one string
    Returns
    -------
    words : list of str
        The list of words in increasing order of size

    """

    letters=list(in_str)

    words = []

    for l in range(1,len(letters)+1):
        for candidate in itertools.permutations(letters,l):
            candidate_word = ''.join(candidate)
            if candidate_word in true_words:
                words.append(candidate_word)

    return words
