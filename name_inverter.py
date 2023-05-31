#!/usr/bin/python3.11
import yaml
import argparse

def inverter(name):
    with open('letters.yaml') as stream:
        letters = yaml.safe_load(stream)['letters']

    with open('letters.yaml') as stream:
        special_characters = yaml.safe_load(stream)['special_characters']

    output_name = ''
    index = 0

    halfway = int(len(letters)) -1

    for letter in name:
        try:
            letters.index(letter.lower())
            index = letters.index(letter.lower())
            if index > halfway:
                index -= halfway
            else:
                index -= halfway
            if letter.islower():
                output_name += letters[index].lower()
            else:
                output_name += letters[index].upper()
        except ValueError:
            try:
                special_characters.index(letter.lower())
                output_name += letter
            except ValueError:
                return f'''Letter {letter} not found in letter list. Please see all accepted letters below
                           {letters}
                           {special_characters}'''
    return output_name





parser = argparse.ArgumentParser(
    prog='Name inverter'
)

if __name__ == '__main__':
    parser.add_argument('Name', type=str)
    args = parser.parse_args()
    print(inverter(args.Name))