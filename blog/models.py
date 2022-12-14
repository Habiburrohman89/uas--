from django.db import models

class blog(models.Model):
    judul = models.CharField(max_length=100)
    body = models.TextField()
    komen = models.CharField(max_length=200)
    email = models.EmailField(default='@gmail.com')
    alamat = models.CharField(max_length=200, blank=True)
 
    def __str__(self):
        return "{}. {}".format(self.id,self.judul)


class aldi(models.Model):
    nama = models.ForeignKey(blog, on_delete=models.CASCADE)
    komen = models.TextField()

    def __str__(self):
        return "{}. {}".format(self.id,self.nama)

class habib(models.Model):
    tidur = models.ForeignKey(blog, on_delete=models.CASCADE)
    tahu = models.TextField()

    def __str__(self):
        return "{}. {}".format(self.id,self.tidur)

   
