# functions.rpy

# Définir les fonctions pour obtenir la lettre suivante et précédente
init python:
    def next_letter(letter):
        return chr(((ord(letter) - ord('A') + 1) % 26) + ord('A'))

    def prev_letter(letter):
        return chr(((ord(letter) - ord('A') - 1) % 26) + ord('A'))
