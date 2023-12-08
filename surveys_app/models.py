from django.db import models
from django.conf import settings

class RoommatePreferences(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clean_bathroom_periodically = models.IntegerField()
    clean_dust_immediately = models.IntegerField()
    vacuum_once_a_day = models.IntegerField()
    clean_hair_dust_immediately = models.IntegerField()
    tidiness_waste_energy = models.IntegerField()
    tidiness_not_needed = models.IntegerField()
    Cleaning_Non_Priority_Daily_Life = models.IntegerField()
    roommate_pet_ok = models.IntegerField()
    no_friends_without_permission = models.IntegerField()
    roommate_drink_less = models.IntegerField()
    Daily_Life_Stress_Susceptibility = models.IntegerField()
    late_night_calls_ok = models.IntegerField()
    long_bathroom_use_ok = models.IntegerField()
    clothes_borrowing_ok = models.IntegerField()
    enter_without_knocking_ok = models.IntegerField()
    meals_with_roommate_important = models.IntegerField()
    roommate_drink_alcohol_well = models.IntegerField()
    emotional_closeness_good = models.IntegerField()
    movie_watching_times = models.IntegerField()
    age_difference_ok = models.IntegerField()
    same_hobbies_not_needed = models.IntegerField()
    maintain_some_distance = models.IntegerField()
    Different_Hobbies_Relationship_Impact = models.IntegerField()
    not_clean_others_mess = models.IntegerField()
    Self_Responsibility_in_Household_Chores_Effectiveness = models.IntegerField()
    Individual_Family_Member_Household_Chores_Responsibility = models.IntegerField()
    share_household_chores = models.IntegerField()
    Housework_Family_Roles_Over_Individual_Tasks = models.IntegerField()

    class Meta:
        db_table = 'roommate_preferences'



class User(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)

    def __str__(self):
        return self.name




