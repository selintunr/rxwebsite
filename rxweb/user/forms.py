from django import forms

class RegisterForm(forms.Form):

    username= forms.CharField(max_length=50, label="Username")
    password= forms.CharField(max_length=20, label="password", widget=forms.PasswordInput)
    confirm= forms.CharField(max_length=50, label="confirm", widget=forms.PasswordInput)
    #datayı valid etmeyi unutma .clean      

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("conifrm")

         #filled but false hata fırlat
        if password and confirm and password != confirm :
            raise forms.ValidationError("passwords did not match")
            

        values= {
            "username": username,
            "password": password
        }    
        return values
            


    
    
    
    

