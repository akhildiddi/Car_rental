from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator  # Import MaxValueValidator
from multiselectfield import MultiSelectField


class Car(models.Model):
    state_choice = (
        ("AP", "Andra Pradesh"),
        ("DL", "Delhi"),
        # ... (other state choices)
        ("TS", "Telangana"),
        ("MH", "Maharashtra"),
        ("KA", "Karnataka"),
        ("TN", "Tamilanadu"),
        ("KL", "Kerala"),
        ("RJ", "Rajasthan"),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ("Cruise Control", "Cruise Control"),
        ("Audio Interface", "Audio Interface"),
        # ... (other feature choices)
        ("Bluetooth Handset", "Bluetooth Handset"),
        ("dual airbags", "dual airbags"),
        ("Touchscreen infotainment", "Touchscreen infotainment"),
        ("ABS", "ABS"),
        ("Panoramic sunroof", "Panoramic sunroof"),
        ("rear parking sensors", "rear parking sensors"),
        ("Harman infotainment", "Harman infotainment"),
        ("Leather seats", "Leather seats"),
        ("LED headlights", "LED headlights"),
        ("Dual-zone climate control", "Dual-zone climate control"),
        ("ADAS", "ADAS"),
        ("connected car tech", "connected car tech"),
        ("Apple CarPlay", "Apple CarPlay"),
        ("Android Auto", "Android Auto"),
        ("Lane Keeping Assist", "Lane Keeping Assist"),
        ("Adaptive Cruise Control", "Adaptive Cruise Control"),
        ("Bluetooth Connectivity", "Bluetooth Connectivity"),
        ("Steering-Mounted Controls", "Steering-Mounted Controls"),
        ("Wireless phone charging", "Wireless phone charging"),
        ("Dual-zone climate control", "Dual-zone climate control"),
        ("SmartPlay infotainment", "SmartPlay infotainment"),
        ("SYNC 3 infotainment", "SYNC 3 infotainment"),
        ("Rearview camera", "Rearview camera"),
        ("Sporty alloy wheels", "Sporty alloy wheels"),
        ("Automatic climate control", "Automatic climate control"),
        ("Sport suspension", "Sport suspension"),
        ("Convertible soft top", "Convertible soft top"),
        ("4x4 drivetrain", "4x4 drivetrain"),
        ("7-inch touchscreen", "7-inch touchscreen"),
        ("ABS with EBD", "ABS with EBD"),
        ("7-seater", "7-seater"),
    )

    door_choices = (
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(("year"), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    car_photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    car_photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    car_photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    car_photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    features = MultiSelectField(
        choices=features_choices,
        validators=[MaxValueValidator(10)],  # Set the max_choices validator
    )
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title

    class Meta:
        # Example: ordering by the created_date field
        ordering = ["-created_date"]
