class LuxuryWatch:
    __watches_created = 0

    def __init__(self):
        LuxuryWatch.__watches_created += 1

    @classmethod
    def including_text(cls, text):
        _luxury_watch = cls()
        _luxury_watch.text = text
        return _luxury_watch

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created

    @staticmethod
    def validate_text(text):
        if len(text) <= 40 and text.isalnum():
            return True
        else:
            raise TypeError("Text does not comply with restrictions")


dict_watches = {"watch1": "", "watch2": "bellaciao", "watch3": "foo@baz.com"}

for k, v in dict_watches.items():
    try:
        if v == "":
            LuxuryWatch()
        elif LuxuryWatch.validate_text(v):
            LuxuryWatch.including_text(v)
    except TypeError as err:
        print(err)
    print("Counter watches", LuxuryWatch.get_number_of_watches_created())
