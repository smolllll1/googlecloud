from django import forms
from .models import Reservation
from datetime import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'visit_date', 'visit_time', 'quests', 'message')

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                         'id': "resName",
                                                                         'type': "text",
                                                                         'name': "res_name",
                                                                         'required': "",
                                                                                          }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                           'id': "resEmail",
                                                           'type': "email",
                                                            'name': "res_email",
                                                           'required': "",
                                                           }))
    phone = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                         'id': "resNumber",
                                                                         'type': "number",
                                                                         'name': "res_number",
                                                                         'required': "",
                                                                         }))
    visit_date = forms.DateField(input_formats=['%Y-%m-%d',  # '2006-10-25'
                                                    '%d-%m-%Y',
                                                    '%d %m %Y',
                                                    '%d.%m.%Y',
                                                    '%m/%d/%Y',  # '10/25/2006'
                                                    '%m/%d/%y',  # '10/25/06'
                                                    '%b %d %Y',  # 'Oct 25 2006'
                                                    '%b %d, %Y',  # 'Oct 25, 2006'
                                                    '%d %b %Y',  # '25 Oct 2006'
                                                    '%d %b, %Y',  # '25 Oct, 2006'
                                                    '%B %d %Y',  # 'October 25 2006'
                                                    '%B %d, %Y',  # 'October 25, 2006'
                                                    '%d %B %Y',  # '25 October 2006'
                                                    '%d %B, %Y',  # '25 October, 2006'
                                                    ], widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                                     'id': "resDate",
                                                                                     'type': "text",
                                                                                     'name': "res_date",
                                                                                     'required': "",
                                                                                      }))
    visit_time = forms.TimeField(input_formats=['%H:%M',
                                                '%H %M',
                                                '%H.%M',
                                                '%H,%M',
                                                '%H;%M'
                                                ], widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                                'id': "resDate",
                                                                                'type': "text",
                                                                                'name': "res_date",
                                                                                'required': "",
                                                                                }))
    quests = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                             'id': "resPeople",
                                                                             'type': "number",
                                                                             "name": "res_people",
                                                                             'required': "",
                                                                             }))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                                            'id': "request",
                                                                            'rows': "7",
                                                                            'name': "res_request",
                                                                            'required': "",
                                                                            }))
