from django import forms
from stories.models import Contact, Recipe, Story, Category, Tag, Subscriber
# from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=13, initial='+994', min_length=7, widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number',
                }), help_text='Sizinle elaqeye kecmeyimiz ucun nomre daxil etmeyiniz sertdir!')
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'phone_number',
            'message',
           
        )
        widgets = {
            'name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Your name',
                }),
            'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Your email',
                }),
            'subject': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Subject',
                }),
            'message': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Message',
                    'rows': 7,
                    'cols': 30,
                })
        }

    
    def clean(self):
        print('here')
        cleaned_data = super().clean()
        print(cleaned_data)

    # def clean_phone_number(self):
    #     phone_number = self.changed_data.get('phone_number')



class RecipeAdminForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Recipe
        fields = '__all__'


class StoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
                    'class': 'form-control'
                }))
    tags =  forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(attrs={
                    'class': 'form-control',
                }) )
    class Meta:
        model = Story
        fields = ('title', 'category', 'tags', 'long_description', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
                }),
            'long_description': CKEditorUploadingWidget(),

        }


class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
                    'class': 'form-control'
                }))
    tags =  forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(attrs={
                    'class': 'form-control',
                }) )
    class Meta:
        model = Recipe
        fields = ('title', 'category', 'tags', 'short_description', 'long_description', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
                }),
            'long_description': CKEditorUploadingWidget(),

        }


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )

        widgets = {
            'email': forms.EmailInput(attrs={
                'class':  'form-control',
                'placeholder': 'Enter email address',
            })
        }










    # name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Your name',
    # }), max_length=40)
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Your email',
    # }), max_length=40)
    # subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Subject',
    # }), max_length=255)
    # message = forms.CharField(label='Message', required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Message',
    #     'rows': 7,
    #     'cols': 30,
    # }))