#!/usr/bin/env python3
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed
        if len(name) > 25:
            self._name = "Name must be string between 1 and 25 characters."
            
        elif name == '':
            self._name = "Name must be string between 1 and 25 characters."
        
        if breed not in APPROVED_BREEDS:
            self._breed = "Breed must be in the list of approved breeds."

    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed
    
fido = Dog("fido","Pointer")
