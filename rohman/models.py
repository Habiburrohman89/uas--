from django.db import models


class editor(models.Model):
    NAMA = models.CharField(max_length=30)
    NPM = models.CharField(max_length=20)
    ALAMAT = models.TextField()
    TETALA = models.DateField()
    EMAIL = models.EmailField(default='@gmail.com')
    KODEPOS = models.CharField(max_length=5)


    def __str__(self):
        return "{}. {}".format(self.id,self.NAMA)

