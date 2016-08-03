from django.core.urlresolvers import reverse

from django import forms 
from django.core.validators import RegexValidator

#crispy imports:
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Submit, HTML, Div
from crispy_forms.bootstrap import FormActions


#import models
from models import State, City 



class EditState(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditState, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edit_state', kwargs={'pk': self.instance.pks})
        self.helper.layout = layout(
                    Div(
                        Div('name', css_class='col-md-10'),
                        Div('abbreviation', css_class='col-md-2'),
                        css_class='row'

                    ),
                    Div(
                        Div(FormActions(Submit('submit', 'submit')), css_class="col-md-12")
                    css_class='row'

                        )
                        
            )



class StateCreate(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'






class EditCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(EditCity, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edit_city', kwargs={'pk': self.instance.pk })

        #self.helper.add_input(Submit('submit', 'search'))
        self.helper.layout = Layout(
                    Div('state', 'name', 'county', css_class='col-sm-6'),
                    Div('latitude', 'longitude', 'zipcode', css_class='col-sm-6'),
                    Div(FormActions(Submit('submit', 'Save')), css_class='col-sm-12')


            )



class CityCreate(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'



    def __init__(self, *args, **kwargs):
        super(StateCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'create_city'

        #self.helper.add_input(Submit('submit', 'search'))
        self.helper.layout = Layout(
                    Div('state', 'name', 'county', css_class='col-sm-6'),
                    Div('latitude', 'longitude', 'zipcode', css_class='col-sm-6'),
                    Div(FormActions(Submit('submit', 'Save')), css_class='col-sm-12')


            )        




class CitySearchForm(forms.Form):
    letters_only = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed')
    city = forms.CharField(required=True, initial="Orem", validators=[letters_only])
    state = forms.CharField(required=True, initial="Utah", validators=[letters_only])

    def __init__(self, *args, **kwargs):
        super(CitySearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_action = 'city_search'

        #self.helper.add_input(Submit('submit', 'search'))
        self.helper.layout = Layout(
                    Div('city', css_class='col-sm-6 col-md-6', style='max-width:224px;'),
                    Div('state', css_class='col-sm-6 col-md-6'),
                    Div(
                        FormActions(
                            Submit('submit', 'search') #to be modified
                            ),
                        css_class='col-sm-2 col-sm-2',
                        style='margin-top:25px;'
                        )
                )



    # STATES = ['Texas', 'Utah'], ['California', 'Colorado']

    # STATES1 = (('1', 'Texas'),
    #          ('2', 'Utah'),
    #          ('3', 'California'))

    # STATES2 = State.objects.all().values_list('id', 'name')


    # print STATES1
    # print STATES2

    # state_select = form.CharField(choices=STATES2)




