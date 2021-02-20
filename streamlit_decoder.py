import streamlit as st

st.title('Ciphers')

def caesar_cipher(text, e_or_d, shift = 13):
    """ Applies the Caeser cipher function on user input.
        parameters:
        text, the string that's being decrpyted/encrypted,
        shift, the value by which we're performing the Caesar/rotational shift, with a default value of 13.
        e_or_d, an int that's -1 if we're decrypting and 1 if we're encrypting
        The function shifts every character that is a letter in text by shift. A Cesarian Shift works as if we have two strips of paper and we aligned them such that A on strip 1 corresponded to F (or any other letter) on strip 2.
        Output: a dycryption of text"""
	
    decryption = ""

    for c in text:
        if c.isupper():
            c_index = ord(c) - ord("A")
            new_index = (c_index + (e_or_d*shift)) % 26
            new_uni = new_index + ord("A")
            decryption += chr(new_uni)
        elif c.islower():
            c_index = ord(c) - ord("a")
            new_index = (c_index + (e_or_d*shift)) % 26
            new_uni = new_index + ord("a")
            decryption += chr(new_uni)
        else:
            decryption += c
    return decryption


def atbash_cipher(text):
    """ Applies the decryption function on user input.
        parameters:
        text, the string that's being decrpyted using the Atbash decoding
        The function flips every character that is a letter in text such that a becomes z, b becomes y, and A becomes Z and B becomes Y, etc.
        Output: a dycryption of text"""
        
    decryption = ""
    for c in text:
        if c.isupper():
            decryption += charUpper(c)
        elif c.islower():
            decryption += charLower(c)
        else:
            decryption += c
    return decryption

def charLower(c):
    """ Helper function for atbash_decoder
        parameters:
        c, a character in text
        The function flips lowercase letters (a to z, c to x, etc).
        Output: a lowercase dycrypted character"""
    c_unicode = ord(c)
    flip = abs((c_unicode - (ord("a")-1)) - 27)
    if (flip > 0 and flip <= 26):
        return chr(flip + ord("a")-1)
    else:
        return c

def charUpper(c):
    """ Helper function for atbash_decoder
        parameters: c, a character in text
        The function flips uppercase letters (A to Z, C to X, etc).
        Output: an uppercase dycrypted character"""
        
    c_unicode = ord(c)
    flip = abs((c_unicode - (ord("A")-1)) - 27)
    if (flip > 0 and flip <= 26):
        return chr(flip + ord("A")-1)
    else:
        return c



e_or_d = st.radio("Do you want to encode or decode?", ["Encrypt", "Decrypt"])

st.write(f'You chose {e_or_d}!')

type_selected = st.selectbox("Select your cipher", ["Caesar", "Atbash"])

if type_selected == "Caesar":
    
    no_default = st.checkbox("Choose your own Shift Value (Default is 13)", value=False, key=None)
    if no_default:
        n = st.number_input('Number', min_value = 0, max_value = 25)
        text = st.text_input(f'Enter some text to {e_or_d}')
        if e_or_d == "Decrypt":
            decryption = caesar_cipher(text, -1, n)
            st.write(f'{decryption}')
        elif e_or_d == "Encrypt":
            encryption = caesar_cipher(text, 1, n)
            st.write(f'{encryption}')
    else:
        text = st.text_input(f'Enter some text to {e_or_d}')
        cryption = caesar_cipher(text, -1)
        st.write(f'{cryption}')
        
elif type_selected == "Atbash":
    text = st.text_input(f'Enter some text to {e_or_d}')
    cryption = atbash_cipher(text)
    st.write(f'{cryption}')


