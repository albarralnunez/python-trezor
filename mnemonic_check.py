#!/usr/bin/python
'''
    Use this script to cross-check that TREZOR generated valid
    mnemonic sentence for given internal (TREZOR-generated)
    and external (computer-generated) entropy.

    Keep in mind that you're entering secret information to this script.
    Hijacking of these information may lead to stealing your bitcoins
    from your wallet! We strongly recommend to run this script only on
    offline computer (ideally live linux distribution without internet connection).
'''

import binascii
import hashlib
import mnemonic

def generate_entropy(strength, internal_entropy, external_entropy):
    '''
    strength - length of produced seed. One of 128, 192, 256
    random - binary stream of random data from external HRNG
    '''
    if strength not in (128, 192, 256):
        raise Exception("Invalid strength")

    if not internal_entropy:
        raise Exception("Internal entropy is not provided")

    if len(internal_entropy) < 32:
        raise Exception("Internal entropy too short")

    if not external_entropy:
        raise Exception("External entropy is not provided")

    if len(external_entropy) < 32:
        raise Exception("External entropy too short")

    entropy = hashlib.sha256(internal_entropy + external_entropy).digest()
    entropy_stripped = entropy[:strength / 8]

    if len(entropy_stripped) * 8 != strength:
        raise Exception("Entropy length mismatch")

    return entropy_stripped

def main():
    comp = binascii.unhexlify(raw_input("Please enter computer-generated entropy (in hex): ").strip())
    trzr = binascii.unhexlify(raw_input("Please enter TREZOR-generated entropy (in hex): ").strip())
    word_count = int(raw_input("How many words your mnemonic has? "))

    strength = word_count * 32 / 3

    entropy = generate_entropy(strength, trzr, comp)

    words = mnemonic.Mnemonic('english').to_mnemonic(entropy)
    if not mnemonic.Mnemonic('english').check(words):
        print "Mnemonic is invalid"
        return

    if len(words.split(' ')) != word_count:
        print "Mnemonic length mismatch!"
        return

    print "Generated mnemonic is:", words

if __name__ == '__main__':
    main()