from django.db import models
class Humans(models.Model):
    name = models.CharField('Имя', max_length=100)
    competition = models.CharField('competition', max_length=100 )
    date = models.DateField('date')
    place = models.CharField('place', max_length=100)
    category = models.CharField('category', max_length=100)
    km = models.IntegerField('KM')
    rank = models.IntegerField('rank')
    result_time = models.TimeField('result_time')
    winner_time = models.TimeField('winner_time')
    delta_with_winner = models.TimeField('delta_with_winner')
    winner_time_min = models.FloatField('winner_time_min')
    delta_min = models.FloatField('delta_min')
    persent = models.FloatField('persent')
    speed_per_km = models.FloatField('speed_per_km')
    def __str__(self):
        return f'{self.name} {self.competition}'

class Auto(models.Model):
    name = models.CharField('Имя', max_length=100)
    text1 = models.CharField('text', max_length=100000)
    def __str__(self):
        return f'{self.name}'