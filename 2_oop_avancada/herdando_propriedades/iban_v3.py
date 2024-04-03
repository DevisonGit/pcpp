import random


class IBANValidationError(Exception):
    pass


class IBANDict(dict):
    def __setitem__(self, key, value):
        if validate_iban(key):
            super().__setitem__(key, value)

    def update(self, *args, **kwargs):
        for key, value in dict(*args, **kwargs).items():
            self.__setitem__(key, value)


def validate_iban(iban: str):
    iban = iban.replace(' ', '')
    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters")
    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short")
    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long")
    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        new_iban = int(iban2)
        if new_iban % 97 == 1:
            return True
        else:
            raise IBANValidationError("IBAN entered is invalid")


my_dict = IBANDict()
iban_list = ["GB72 HBZU 7006 7212 1253 00", "FR76 30003 03620 00020216907 50", "DE02100100100152517108",
             "DE02100100100152617108"]

for iban_element in iban_list:
    try:
        my_dict[iban_element] = random.randint(0, 1000)
    except IBANValidationError as e:
        print(e)

print("The dictionary contains")
for k, v in my_dict.items():
    print(f'\t{k} -> {v}')
