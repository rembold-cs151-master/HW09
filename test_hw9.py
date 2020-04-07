# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os
import random

import Prob1


class Test_Prob1:
    def test_Message_getters_setters(self):
        msg1 = 'Hello there!'
        msg2 = 'Why hi!'
        msg = Prob1.Message(msg1)
        assert msg.get_message_text() == msg1
        msg.change_message_text(msg2)
        assert msg.get_message_text() == msg2

    def test_Message_shift_dict(self):
        msg = Prob1.Message('Great')
        d = msg.build_shift_dict(10)
        checks = {'A':'K', 'a':'k', 'T':'D', 'x':'h'}
        for key in checks:
            assert d[key] == checks[key], f'Dictionary is improperly shifted. For a shift of 10, expected {key} to be shifted to {checks[key]} but instead is corresponding to {d[key]}.'

    def test_Message_apply_shift(self):
        msg1 = Prob1.Message('Human')
        msg2 = Prob1.Message('Hi! Welcome, one and all!')
        s1 = msg1.apply_shift(6)
        a1 = "Nasgt"
        s2 = msg2.apply_shift(10)
        a2 = "Rs! Govmywo, yxo kxn kvv!"
        assert s1 == a1, f'Shifting "Human" by 6 should have given "{a1}" but instead gave {s1}.'
        assert s2 == a2, f'Shifting "Hi! Welcome one and all!" by 10 should have given "{a2}" but instead gave {s2}. Are spaces and punctuation being properly ignored?'

    def test_PlainMsg_init(self):
        msg = Prob1.PlainMsg('Horton hears a Who', 2)
        encrypt = 'Jqtvqp jgctu c Yjq'
        student = msg.get_encrypted_msg()
        assert student == encrypt, f'Make sure the encrypted message is created immediately upon initialization!'

    def test_PlainMsg_change_shift(self):
        msg = Prob1.PlainMsg('Greetings from the North Pole',4)
        initial = msg.get_encrypted_msg()
        msg.change_shift(10)
        final = msg.get_encrypted_msg()
        assert initial != final, 'Did the encrypted message get updated when the shift was changed?'

    def test_get_words(self):
        sols = {
                'This is a great string of words!':['This', 'is', 'a', 'great', 'string', 'of', 'words'],
                "It's all too easy":['Its', 'all', 'too', 'easy'],
                }
        for key in sols:
            student = Prob1.get_words(key)
            assert student == sols[key], f'The string "{key}" should give words: {sols[key]} but is instead giving {student}.'

    def test_CipherMsg_decrypt(self):
        try:
            valid_words = Prob1.load_words()
        except TypeError:
            valid_words = Prob1.load_words('words.txt')
        sols = {
               'Tcxlsr mw kviex': 'Python is great',
               'Ktocji dn bmzvo': 'Python is great',
               'Utk, Zcu, Znxkk!!': 'One, Two, Three!!'
               } 
        for key in sols:
            student = Prob1.CipherMsg(key)
            student.decrypt_msg(valid_words)
            assert student.decoded_msg == sols[key], f'The message "{key}" should have decoded to "{sols[key]}" but instead gave {student}.'

    def test_Cipher_Story_Decoded(self):
        story = Prob1.read_story('story.txt')
        Prob1.decode_story(story)
        f = open('decoded_story.txt', 'r')
        lines = f.readlines()
        assert lines[2].strip() == 'My grandfather took me out to the wall.', 'Your story seems to be decoding improperly, or you are not correctly writing it to file.'

