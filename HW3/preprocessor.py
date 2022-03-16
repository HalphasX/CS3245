from typing import List

from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from unidecode import unidecode

class Preprocessor:
    '''
    Preprocessor class that in charge of preprocessing the corpus
    before performing indexing.

    Attributes:
        stemmer (nltk.stem) : Stemmer use for preprocessing.
    '''

    def __init__(self) -> None:
        self.stemmer = PorterStemmer()

    def preprocess_word(self, word) -> str:
        '''
        Take a word, normalize, stem, and turn the word
        into a lower case word.

        Argument:
            word (str): A word

        Return:
            A lower-case word after being stemmed
        '''
        return self.stemmer.stem(unidecode(word))

    def preprocess_file(self, file_path) -> List[str]:
        '''
        Take a file path and return the tokenized words for the document.

        Argument:
            file_path (str): Path to file.

        Return:
            list of tokenized lower case words in the file.
        '''
        with open(file_path, "r", encoding="utf8") as f:
            file = f.read()
        # Tokenize sentence
        sentences = sent_tokenize(file)

        # Tokenize, normalize, and store all the words
        raw_words = []
        for sentence in sentences:
            for word in word_tokenize(sentence):
                raw_words.append(unidecode(word))

        # Lower case, stemming, and remove non-alphanumeric words
        processed_words = [self.stemmer.stem(word) for word in raw_words]

        return processed_words
