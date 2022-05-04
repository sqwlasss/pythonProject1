"""
New day, new attempt. This one is called arc4ne, as A Rivest Cipher 4 Nephew
This encryption algorithm follows the goal to be more secure than the original one.
According to the science paper RC4 algorithm has a couple of known issues.
If the key has the length divisible to some power of two it is easily breakable.
Having the same key encrypting different messages also helps the attacker break the cipher.
First issue is solved by internally modifying the key in such way that it's length is always odd.
Second issue requires key to be different every time encryption is happening, this is why timestamps are used together
with traditional key in order to always have different keys. End user doesn't need to know anything about these internal
processes and can be sure that he can use his key on one device for encryption and on other device for decryption
without any issues.
In this algorithm modification I tried to cover these 2 vulnerabilities and added even additional layer of security.
As an algorithm with 1 key this one can be brute forced without any serious issues (find examples in science work),
that is why I added an external layer that uses 'scrypt' library. Its biggest upside for me is that it takes very long
time to encrypt or decrypt messages compared to common algorithms, so arc4ne has scrypt encryption as upper layer.
Having 'scrypt' allows to ignore brute force attacks, but if one wants to use arc4ne for wireless connection just like
for what another version of RC4 was used, there is an option to disable 'scrypt' layer.
Science paper link
https://wiki-files.aircrack-ng.org/doc/technique_papers/rc4_ksaproc.pdf
Is there a chance to implement one way function on top of that all? Long story short - no, without using other scripts
I can't achieve this. And the scope of this work is improve specified algorithm - RC4
"""
import time
import scrypt


def sstr(s):
    new = ""
    for x in s:
        new += x
    return new


class Arc4ne:
    def __init__(self):
        self.__init_private_vars()
        self.__use_scrypt = True

    def use_scrypt(self, bl):
        if isinstance(bl, bool) and bl is not None:
            self.__use_scrypt = bl
        else:
            raise Exception('Provide proper boolean!')

    def __init_private_vars(self):
        self.__plain_key = None
        # yes, I wanted a hardcoded value on top of other manipulations just because I wanted so.
        # in general we can add extra layers and add such mock values, but I wanted to cover general
        # issues, not make a god cipher
        self.__key_stage1_fragment = 'hesoyam'

    def set_key(self, k):
        if isinstance(k, str) and k is not None:
            self.__plain_key = k
        else:
            raise Exception('Provide proper string as key!')

    def get_key(self):
        return self.__plain_key

    def __stage1_encrypt(self, plain_text, key):
        S = list(range(256))
        j = 0
        out = []
        data = str(plain_text)

        # KSA Phases
        for i in range(256):
            j = (j + S[i] + ord(key[i % len(key)])) % 256
            S[i], S[j] = S[j], S[i]

        # PRGA Phase
        i = j = 0
        for char in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

        return sstr(out)

    def __stage1_decrypt(self, ciphered_text, key):
        S = list(range(256))
        j = 0
        out = []
        data = ciphered_text

        # KSA Phase
        for i in range(256):
            j = (j + S[i] + ord(key[i % len(key)])) % 256
            S[i], S[j] = S[j], S[i]

        # PRGA Phase
        i = j = 0
        for char in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

        return sstr(out)

    def __check_plain_key(self):
        if self.__plain_key is None:
            raise Exception('Before encrypting, first you will need to set the key! (obj.set_key("key"))')

    def __check_plain_text(self, plain_text):
        if not (isinstance(plain_text, str) and plain_text is not None):
            raise Exception('Provide proper string as the plain text!')

    def __is_odd(self, string):
        if len(str(string)) % 2 == 1:
            return True
        return False

    def __stage2_ecnrypt(self, plain_text, key):
        return scrypt.encrypt(plain_text, key)

    def __stage2_decrypt(self, plain_text, key):
        return scrypt.decrypt(plain_text, key)

    def __complete_timestamp_to_18(self, ts):
        length = len(ts)
        if length == 18:
            pass
        elif length == 17:
            ts = ts + ts[-1:]
        elif length == 16:
            ts = ts + ts[-2:]
        else:
            raise Exception(f'Length of %s was %i' % (ts, length))
        return ts

    def __complete_key_to_odd(self, key):
        return (key + key[-1:])

    def __shorten_timestamp(self, stage1_ciphered_timestamp):
        data = stage1_ciphered_timestamp
        last1_ts_char = data[-1]
        last2_ts_char = data[-2]
        last3_ts_char = data[-3]
        if last1_ts_char == last2_ts_char == last3_ts_char:
            data = data[:-2]
        elif last1_ts_char == last2_ts_char:
            data = data[:-1]
        return data

    def __check_and_fix_key_length(self, key):
        if not self.__is_odd(key):
            return self.__complete_key_to_odd(key)
        return key

    def encrypt(self, plain_text):
        # this will be the main method
        # this algorithm is for string encryption primarily and its success with other types will not be tested
        # health checks.
        self.__check_plain_key()
        self.__check_plain_text(plain_text)
        # time stamp during encryption; combining it with plain_key assures that cipher will be unique each time
        timestamp = time.time()
        # to encrypt timestamp I will use reversed plain_key
        reverse_plain_pre_key = self.__plain_key[::-1]
        # here and later, there will be checks for key to make sure they are of odd length
        reverse_plain_key = self.__check_and_fix_key_length(reverse_plain_pre_key)
        ciphered_time_stamp_pre1 = self.__stage1_encrypt(timestamp, reverse_plain_key)
        # I figured that length of timestamp is not more than 18, I will need this fixed length later
        ciphered_time_stamp = self.__complete_timestamp_to_18(ciphered_time_stamp_pre1)

        stage1_pre_key = self.__key_stage1_fragment + self.__plain_key + ciphered_time_stamp
        stage1_key = self.__check_and_fix_key_length(stage1_pre_key)
        stage1_ciphered = self.__stage1_encrypt(plain_text, stage1_key)
        # end of stage 1
        # we put ciphered timestamp before last character of stage1 ciphered
        stage2_plain = stage1_ciphered[:-1] + ciphered_time_stamp + stage1_ciphered[-1:]

        # now we use scrypt to encrypt stage 2, key will be plain key
        # at this stage we already have a ciphered text and there is an option to pass the 'scrypt' part
        # Once again, 'scrypt' is for making it hard to brute force
        if self.__use_scrypt:
            stage2_ciphered = self.__stage2_ecnrypt(stage2_plain, self.__plain_key)
            return stage2_ciphered
        else:
            return stage2_plain

    def decrypt(self, ciphered_text):
        # health check.
        self.__check_plain_key()
        if self.__use_scrypt:
            stage2_plain = self.__stage2_decrypt(ciphered_text, self.__plain_key)
        else:
            stage2_plain = ciphered_text

        # literally all the steps backwards
        stage1_ciphered = stage2_plain[:-19] + stage2_plain[-1]
        stage1_ciphered_timestamp = stage2_plain[-19:][:-1]
        stage1_shortened_timestamp = self.__shorten_timestamp(stage1_ciphered_timestamp)
        stage1_pre_key = self.__key_stage1_fragment + self.__plain_key + stage1_shortened_timestamp
        stage1_key = self.__check_and_fix_key_length(stage1_pre_key)
        stage1_plain_text = self.__stage1_decrypt(stage1_ciphered, stage1_key)
        return stage1_plain_text