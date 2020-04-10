##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

import string

class Message(object):
    '''
    A type to hold information pertinant to encoding and decoding a simple
    message.

    Example Usage:
    >>> msg = Message('abcdefg')
    >>> msg.get_message_text()
    'abcdefg'
    >>> msg.apply_shift(2)
    'cdefghi'
    >>> msg.apply_shift(4)
    'efghijk'
    '''

    def __init__(self, text):
        '''
        Initializes a Message object.

        Inputs:
            - text (string): the text of the message. Any string allowed.

        Should have a single attribute:
            - self.message_text (a string, determined by input text)
        '''
        pass

    def __repr__(self):
        '''
        Textual representation of the object which could be used to
        recreate the object.
        '''
        pass

    def get_message_text(self):
        '''
        Used to safely access the data attribute message_text outside
        of the class.

        Outputs:
            - message_text (string)
        '''
        pass

    def change_message_text(self, new_text):
        '''
        Setter method to safely update and change the text of a message.

        Input:
            - new_text (string): new text to change the message to
        Output:
            - Nothing
        '''
        pass

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every upper and lower case letter to a corresponding
        upper and lower case letter which is shift forwards along the alphabet
        a distance "shift". The created dictionary should thus have 52 keys.
        Letters which are shifted beyond Z should wrap around back at the
        beginning of the alphabet.

        Input:
            - shift (int): The amount by which to shift every letter in the
                alphabet.
        Output:
            - (dict): maps every letter (string) to another letter (string)
        '''
        pass

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the shift amount
        given by "shift". Returns a new string of the encrypted message.

        Input:
            - shift (int): The amount by which to shift every letter in the
                message.
        Output:
            - (string): The message text with all letters shifted by the
                desired amount.
        '''
        pass


#---------------------------------
# Defining PlainMsg
#---------------------------------
class PlainMsg(Message):
    '''
    This subclass focuses on converting plaintext messages into encrypted
    messages and easily modifying the content.

    Example Usage:
    >>> msg = PlainMsg('Hello, World!', 4)
    >>> msg.get_encrypted_msg()
    'Lipps, Asvph!'
    >>> msg.change_shift(7)
    >>> msg.get_encrypted_msg()
    'Olssv, Dvysk!'
    '''

    def __init__(self, text, shift):
        '''
        Initializes a PlainMsg type object

        Inputs:
            - text (string): the message's text
            - shift (int): the amount the encrypted message to to be shifted

        A PlainMsg object inherits from Message and has 4 total attributes:
            - self.message_text (string, determined by input)
            - self.shift (integer, determined by input)
            - self.shift_dict (dictionary, created using shift)
            - self.encrypted_msg (string, created using shift)
        '''
        pass

    def get_shift(self):
        ''' 
        Safely access the self.shift attribute outside the class.

        Outputs:
            - (integer): the value of self.shift
        '''
        pass

    def change_shift(self, new_shift):
        '''
        Changes self.shift of the PlainMsg object and updates all other
        attributes which depend on self.shift.

        Input:
            - new_shift (integer): new value to shift all the letters by
        Output:
            - Nothing
        '''
        pass

    def get_encrypted_msg(self):
        '''
        Safely acces the self.encrypted_msg attribute outside the class

        Outputs:
            - (string): the value of self.encrypted_msg
        '''
        pass


# -------------------------------------
# Some helper functions for CipherMsg
# -------------------------------------
def load_words(file_name):
    """
    Returns a list of valid words, where all words are
    strings of lowercase characters.

    Outputs:
        - (list of strings): list of lowercase valid words

    You do not need to edit this function!
    """
    print('Loading valid word list from file...')
    f = open(file_name, 'r')
    wordlist = []
    for line in f:
        wordlist.extend([word.lower() for word in line.split(' ')])
    f.close()
    print(f'...{len(wordlist)} words loaded.')
    return wordlist

def get_words(phrase):
    '''
    Splits a phrase or sentence up into a list of individual words,
    stripping out any punctation along the way. Using the .split()
    method for strings may be useful but it can be done without as
    well.

    Input:
        - phrase (string): The string to be broken up into words
    Output:
        - (list of strings): list of the individual words from the
            phrase, with no punctuation included
    Usage:
    >>> get_words('Great scott! That man is insane!')
    ['Great', 'scott', 'That', 'man', 'is', 'insane']
    '''
    pass

def count_valid_words(potential_words, list_valid_words):
    '''
    Compares the list of potential words to the provided list of
    valid words, and returns a count of how many of the potential
    words are real words. Ensures that the capitalization of all
    words matches.

    Inputs:
        - potential_words (list of strings): list of the individual
            words to check if they are real words
        - list_valid_words (list of strings): list of valid words
            read in from the 'words.txt' file
    Output:
        - (integer): the number of words in potential_words which
            are found to be real valid words
    Usage:
    >>> valid_words = load_words('words.txt')
    >>> count_valid_words(['boop', 'bauoe', 'hello', 'tree'], valid_words)
    2
    '''
    pass

#---------------------------------
# Defining CipherMsg
#---------------------------------
class CipherMsg(Message):
    '''
    Class to handle taking already encrypted messages and
    brute-forcing all possible shifts to break the encryption.

    Example Usage:
    '''

    def __init__(self, text):
        '''
        Initializes a CipherMsg object.

        Input:
            - text (string): The messages encrypted text

        A CipherMsg object inherits from Message and has 4 attributes:
            - self.message_text (string, determined from input)
            - self.is_decrypted (bool, initially False)
            - self.best_shift (integer, initially None)
            - self.decoded_msg (string, initially None)
        '''
        pass

    def decrypt_msg(self, valid_words):
        '''
        Decryptes self.message_text by trying every possible shift value
        and finding the "best" one, where "best" here is the shift
        value that results in the greatest number of valid words found
        in the resulting decrypted message. If multiple shifts are
        equally "best", then any can be set as the decoded message.

        Updates the attributes of self.is_decrypted, self.best_shift,
        and self.decoded_msg after finding the best shift and decoding
        the message. 

        Input:
            - valid_words (list of string): the list of valid english
                words to compare potential messages to.
        Output:
            - (string): the decoded message string
        '''
        pass



#---------------------------------
# Story Time
#---------------------------------
def read_story(file_name):
    '''
    Reads in the file_name and outputs a string. Takes multiline files
    and stitches them back together in a single string with line-breaks
    embedded in the string.

    Input:
        - file_name (string): Name of file to read in
    Output:
        - (string): single string of entire file
    '''
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return ''.join(lines)

def decode_story(story_string):
    '''
    Determines the proper shift necessary to decode the encrypted story.
    Writes the resulting decrypted story to the file 'decoded_story.txt'.

    Inputs:
        - story_string (string): the story to be decrypted
    Outputs:
        - None, but a file is written
    '''
    pass
    





# If you have any testing code you want to run with the program
# insert it in the if statement below.
if __name__ == '__main__':
    pass
