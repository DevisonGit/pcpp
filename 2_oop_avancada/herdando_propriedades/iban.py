def validate_iban(iban: str):
    iban = iban.replace(' ', '')
    if not iban.isalnum():
        print("You have entered invalid characters")
    elif len(iban) < 15:
        print("IBAN entered is too short")
    elif len(iban) > 31:
        print("IBAN entered is too long")
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
            print("IBAN entered is valid")
        else:
            print("IBAN entered is invalid")



# valid IBAN
validate_iban('GB72 HBZU 7006 7212 1253 00')
validate_iban("FR76 30003 03620 00020216907 50")
validate_iban("DE02100100100152517108")

# invalid IBAN
validate_iban("DE02100100100162517108")
