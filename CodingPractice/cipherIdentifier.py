# A basic Cipher Identifier project.

# import replit
import re

encryptedRawText = input("Enter Encrypted Text (Remove all paragraph lines): ")
adfgvx = ["a","d","f","g","v","x"]
adfgv = ["a","d","f","g","v"]
# replit.clear()
print("Analysis Complete")

encryptedText = ""
encryptedText = (re.sub('[^A-Za-z0-9]+', '', encryptedRawText)).lower()
encryptedText = encryptedText.replace('\n', '').replace('\r', '')
print("Number of unique characters: " + str(len(set(encryptedText))))

if len(set(encryptedText)) == 2:
  cipher = "Baconian"
elif len(set(encryptedText)) in (5,6):
  cipher = "Polybius Square, Playfair, Foursquare, Bifid"
  if len(encryptedText) % 2 != 0:
    cipher = "Polybius Square, Bifid"
  if set(set(encryptedText)) == set(adfgv):
    cipher = "ADFGV"
  if set(set(encryptedText)) == set(adfgvx):
    cipher = "ADFGVX"
elif len(set(encryptedText)) > 26:
  cipher = "Code/Nomenclature or Homophonic Substitution Cipher"
elif len(set(encryptedText)) in (23,24,25,26):
  monogram = input("Is monogram analysis equivalent to English? (y/n): ")
  if monogram == "y":
    cipher = "Transposition Cipher (Columnar, etc. )"
  else:
    IC = input("Enter IC frequency analysis result: ")
    if float(IC) < 0.07 and float(IC) > 0.05:
      cipher = "Substitution Cipher (Caesar, Affine, etc. )"
    else:
      cipher = "Polyalphabetic, Polygraphic, Vigenere, Porta, Beaufort, Hill, or Gronsfeld (a.k.a You're fucked.)"

print("Possible Ciphers: " + cipher)