from django.db import models

class Customer (models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=500)
    confirm_password=models.CharField(max_length=500)


    def register(self):
        self.save()

    def is_exits (self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    # for loginpage
    @staticmethod
    def get_costomer_by_name (username):
        try:
            return Customer.objects.get(username=username)
        except:
            pass
    