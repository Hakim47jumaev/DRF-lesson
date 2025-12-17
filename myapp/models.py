from django.db import models



class Author(models.Model):
    fullname=models.CharField( max_length=50)
    birth_year=models.IntegerField()


    def __str__(self):
        return self.fullname

class Book(models.Model):
    title=models.CharField( max_length=50)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    price=models.IntegerField()

    def __str__(self):
        return self.title
    

class Car(models.Model):
    model=models.CharField( max_length=50)
    brend=models.CharField( max_length=50)
    owner=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.model
    


class Product(models.Model):
    title=models.CharField( max_length=50)


    def __str__(self):
        return self.title
    




class Course(models.Model):
    name=models.CharField( max_length=50)
    description=models.CharField( max_length=50)
    stack=models.CharField( max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    is_deleted=models.BooleanField(default=False)
    start_at=models.DateTimeField(auto_now=False, auto_now_add=False)


    def save(self, *args, **kwargs):
        self.stack=self.stack.upper()

        return super().save(*args, **kwargs)
    
    def delete(self,*args, **kwargs):
        self.is_deleted=True
        self.save(*args, **kwargs)
    



    def __str__(self):
        return self.name

