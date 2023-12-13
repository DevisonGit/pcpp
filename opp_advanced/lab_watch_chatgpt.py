class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @classmethod
    def create_engraved_watch(cls, engraving_text):
        cls.validate_engraving_text(engraving_text)
        return cls()

    @staticmethod
    def validate_engraving_text(text):
        if len(text) > 40 or not text.isalnum():
            raise ValueError("Invalid engraving text. Text should be alphanumeric and no longer than 40 characters.")

# Create a watch with no engraving
watch1 = LuxuryWatch()
print("Number of watches created:", LuxuryWatch.get_number_of_watches_created())

# Create a watch with correct text for engraving
engraved_watch_text = "BeautifulWatch123"
watch2 = LuxuryWatch.create_engraved_watch(engraved_watch_text)
print("Number of watches created:", LuxuryWatch.get_number_of_watches_created())

# Try to create a watch with incorrect text
try:
    invalid_engraved_watch_text = "foo@baz.com"
    watch3 = LuxuryWatch.create_engraved_watch(invalid_engraved_watch_text)
except ValueError as e:
    print("Error:", e)

print("Number of watches created:", LuxuryWatch.get_number_of_watches_created())
