from django.db import models


class ScientificDirector(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.surname} {self.name}"


class Section(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"({self.short_name}) {self.name}"


class Competitor(models.Model):
    user_record = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    sc_director = models.ForeignKey(ScientificDirector,
                                    on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    section_number = models.IntegerField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.user_record.first_name} {self.user_record.last_name}"
