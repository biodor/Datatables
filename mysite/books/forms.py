from django import forms

from .models import Book


class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )
		def get_form(self):
			form = super().get_form()
			form.fields['publication_date'].widget = DateTimePickerInput()
			return form

	author = forms.CharField(
		label='Author',
		widget=forms.TextInput(attrs={'placeholder': 'Biodor Bonifacio'})
	)

	publication_date = forms.DateTimeField(
		input_formats=['%d/%m/%Y'],
		widget=forms.DateTimeInput(attrs={
			'class': 'form-control datetimepicker-input',
			'data-target': '#id_publication_date'
		})
	)

