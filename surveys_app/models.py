from django.db import models
from django.conf import settings

class RoommatePreferences(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    CLEANING_CHOICES = [
        (2, 'Strongly Agree'),
        (1, 'Agree'),
        (0, 'Neutral'),
        (-1, 'Disagree'),
        (-2, 'Strongly Disagree')
    ]

    clean_bathroom_periodically = models.IntegerField(choices=CLEANING_CHOICES,default=0)
    clean_dust_immediately = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    vacuum_once_a_day = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    clean_hair_dust_immediately = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    tidiness_waste_energy = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    tidiness_not_needed = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    Cleaning_Non_Priority_Daily_Life = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    roommate_pet_ok = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    no_friends_without_permission = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    roommate_drink_less = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    Daily_Life_Stress_Susceptibility = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    late_night_calls_ok = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    long_bathroom_use_ok = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    clothes_borrowing_ok = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    enter_without_knocking_ok = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    meals_with_roommate_important = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    roommate_drink_alcohol_well = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    emotional_closeness_good = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    movie_watching_times = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    age_difference_ok = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    same_hobbies_not_needed = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    maintain_some_distance = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    Different_Hobbies_Relationship_Impact = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    not_clean_others_mess = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    Self_Responsibility_in_Household_Chores_Effectiveness = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    Individual_Family_Member_Household_Chores_Responsibility = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    share_household_chores = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    Housework_Family_Roles_Over_Individual_Tasks = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    drinks_alcohol = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    smokes_cigarettes = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    smokes_indoors = models.IntegerField(choices=CLEANING_CHOICES, default=0)

    class Meta:
        db_table = 'roommate_preferences'




class User(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)

    def __str__(self):
        return self.name




