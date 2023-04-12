from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):

    # specify the name of model to use
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')

        super(CategoryForm, self).__init__(*args, **kwargs)
        # add class
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    # validation
    def clean(self):
        cleaned_data = super(CategoryForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError({"confirm_password": "Password & Confirm Password does not match"}
                                        )

        return cleaned_data

    class Meta:
        model = Category
        fields = ("name", "image", "description")
        # widgets = {
        #     'username': TextInput(attrs={'placeholder': 'Enter the Username'}),
        #     'email': EmailInput(attrs={'placeholder': 'Enter the Email-Id'}),
        #     'first_name': TextInput(attrs={'placeholder': 'Enter the First Name'}),
        #     'last_name': TextInput(attrs={'placeholder': 'Enter the Last Name'}),
        #     'password': PasswordInput(attrs={'placeholder': 'Enter the Password', 'maxlength': "18", 'minlength': "3"}),
        #     'confirm_password': PasswordInput(
        #         attrs={'placeholder': 'Enter the Confirm Password', 'maxlength': "18", 'minlength': "3"})
        # }
