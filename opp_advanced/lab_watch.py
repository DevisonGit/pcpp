class LuxuryWatch:
    __internal_counter = 0

    def __init__(self) -> None:
        LuxuryWatch.__internal_counter += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return "# of objects created {}".format(cls.__internal_counter)
    
    @classmethod
    def including_engraving(cls, engraving):
        _luxurywatch = cls()
        _luxurywatch.engraving = engraving
        return _luxurywatch
    

    @staticmethod
    def validate(engraving):
        if len(engraving) > 40 or not engraving.isalnum():
            raise TypeError("The {} was a invalid characters".format(engraving))


print(LuxuryWatch.get_number_of_watches_created())
watch_no_engraving = LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created())
watch_engraving = LuxuryWatch.including_engraving('Engraving')
print(LuxuryWatch.get_number_of_watches_created())
watch_engraving_incorrect = LuxuryWatch.validate('foo@baz.com')
print(LuxuryWatch.get_number_of_watches_created())