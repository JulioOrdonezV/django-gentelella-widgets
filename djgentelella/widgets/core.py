from django.forms import (PasswordInput as DJPasswordInput, FileInput as DJFileInput,
                          ClearableFileInput as DJClearableFileInput, Textarea as DJTextarea,
                          DateInput as DJDateInput, DateTimeInput as DJDateTimeInput,
                          TimeInput as DJTimeInput, CheckboxInput as DJCheckboxInput, Select as DJSelect,
                          SplitHiddenDateTimeWidget as DJSplitHiddenDateTimeWidget,
                          CheckboxSelectMultiple as DJCheckboxSelectMultiple, SelectMultiple as DJSelectMultiple,
                          SelectDateWidget as DJSelectDateWidget, SplitDateTimeWidget as DJSplitDateTimeWidget)
from django.forms.widgets import Input as DJInput
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


def update_kwargs(attrs, widget, base_class='form-control '):
    if attrs is not None:
        attrs = attrs.copy()

    if attrs is None:
        attrs = {}
    if 'class' in attrs:
        attrs.update({'class':  base_class + attrs['class']})
    else:
        attrs.update({'class': base_class })
    attrs['data-widget'] = widget
    return attrs

class Input(DJInput):
    """
    Base class for all <input> widgets.
    """
    template_name = 'gentelella/widgets/input.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class TextInput(Input):
    input_type = 'text'
    template_name = 'gentelella/widgets/text.html'


class NumberInput(Input):
    input_type = 'number'
    template_name = 'gentelella/widgets/number.html'
    # min_value y max_value
    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, extraskwargs=extraskwargs)

"""
class NumberKnobInput(Input):
    input_type = 'number'
    template_name = 'gentelella/widgets/number.html'
    # min_value y max_value
    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__, base_class='')
        if 'max_value' in attrs:
            attrs['data-max'] = attrs['max_value']
        if 'min_value' in attrs:
            attrs['data-min'] = attrs['min_value']
        super().__init__(attrs, extraskwargs=extraskwargs)
"""
class EmailInput(Input):
    input_type = 'email'
    template_name = 'gentelella/widgets/email.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, extraskwargs=extraskwargs)

class URLInput(Input):
    input_type = 'url'
    template_name = 'gentelella/widgets/url.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        attrs['placeholder'] = 'https://'
        super().__init__(attrs, extraskwargs=extraskwargs)

class PasswordInput(DJPasswordInput):
    input_type = 'password'
    template_name = 'gentelella/widgets/password.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)
#Fixme: do upload view
class FileInput(DJFileInput):
    input_type = 'file'
    needs_multipart_form = True
    template_name = 'gentelella/widgets/file.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__, base_class='djgentelella-file-input form-control')
        if 'data-href' not in attrs:
            attrs.update({'data-href': reverse_lazy('upload_file_view')})
        if 'data-done' not in attrs:
            attrs['data-done'] = reverse_lazy('upload_file_done')
        super().__init__(attrs)


class ClearableFileInput(DJClearableFileInput):
    template_name = 'gentelella/widgets/file.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)


class Textarea(DJTextarea):
    template_name = 'gentelella/widgets/textarea.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='resizable_textarea form-control')
        attrs['rows']='3'
        super().__init__(attrs)

class TextareaWysiwyg(DJTextarea):
    template_name = 'gentelella/widgets/wysiwyg.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='form-control')

        super().__init__(attrs)

class DateInput(DJDateInput):
    """
    .. warning::
        Set in settings

            USE_L10N = False

            DATE_INPUT_FORMATS=[ '%Y-%m-%d','%d/%m/%Y','%d/%m/%y']

        By limitation on js datetime widget format conversion
    """
    format_key = 'DATE_INPUT_FORMATS'
    template_name = 'gentelella/widgets/date.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)




class DateTimeInput(DJDateTimeInput):
    """
    .. warning::
        Set in settings

            USE_L10N = False

            DATETIME_INPUT_FORMATS=[ '%m/%d/%Y %H:%M %p' ]

        By limitation on js datetime widget format conversion
    """

    format_key = 'DATETIME_INPUT_FORMATS'
    template_name = 'gentelella/widgets/datetime.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)



class TimeInput(DJTimeInput):
    format_key = 'TIME_INPUT_FORMATS'
    template_name = 'gentelella/widgets/time.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)
        self.format = format or "%H:%M:%S"

class CheckboxInput(DJCheckboxInput):
    input_type = 'checkbox'
    template_name = 'gentelella/widgets/checkbox.html'


    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__, base_class='flat ')
        super().__init__(attrs)
        self.format = format or None

class YesNoInput(DJCheckboxInput):
    input_type = 'checkbox'
    template_name = 'gentelella/widgets/checkyesno.html'


    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__, base_class='js-switch')

        super().__init__(attrs)
        self.format = format or None


class Select(DJSelect):
    input_type = 'select'
    template_name = 'gentelella/widgets/select.html'
    option_template_name = 'gentelella/widgets/select_option.html'
    add_id_index = False
    checked_attribute = {'selected': True}
    option_inherits_attrs = False

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__, base_class='select2_single form-control ')
        super().__init__(attrs,  choices=choices)

class SelectWithAdd(Select):
    template_name = 'gentelella/widgets/addselect.html'
    option_template_name = 'gentelella/widgets/select_option.html'


    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                                  base_class='form-control ')
        if 'add_url' not in attrs:
            raise ValueError('SelectWithAdd requires add_url in attrs')
        super().__init__(attrs,  choices=choices, extraskwargs=False)

class SelectTail(DJSelect):
    input_type = 'select'
    template_name = 'gentelella/widgets/select.html'
    option_template_name = 'gentelella/widgets/select_option.html'
    add_id_index = False
    checked_attribute = {'selected': True}
    option_inherits_attrs = False

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__, base_class='select2_single form-control ')
        super().__init__(attrs,  choices=choices)

class SelectMultiple(DJSelectMultiple):
    allow_multiple_selected = True

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='select2_multiple form-control ')
        super(SelectMultiple, self).__init__(attrs, choices=choices)

class SelectMultipleAdd(SelectMultiple):
    allow_multiple_selected = True
    template_name = 'gentelella/widgets/addselect.html'
    option_template_name = 'gentelella/widgets/select_option.html'

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='select2_multiple form-control ')
        super(SelectMultipleAdd, self).__init__(attrs, choices=choices, extraskwargs=False)

class SelectMultipleTail(DJSelectMultiple):
    allow_multiple_selected = True

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='form-control ')
        super().__init__(attrs, choices=choices)



class RadioSelect(Select):
    input_type = 'radio'
    template_name = 'gentelella/widgets/radio.html'
    option_template_name = 'gentelella/widgets/attrs.html'

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, choices=choices, extraskwargs=extraskwargs)

class NullBooleanSelect(RadioSelect):

    def __init__(self, attrs=None, choices = (
                                    ('unknown', _('Unknown')),
                                    ('true', _('Yes')),
                                    ('false', _('No')),
                                    )):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, choices=choices, extraskwargs=False)

    def format_value(self, value):
        try:
            return {
                True: 'true', False: 'false',
                'true': 'true', 'false': 'false',
                # For backwards compatibility with Django < 2.2.
                '2': 'true', '3': 'false',
            }[value]
        except KeyError:
            return 'unknown'

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        return {
            True: True,
            'True': True,
            'False': False,
            False: False,
            'true': True,
            'false': False,
            # For backwards compatibility with Django < 2.2.
            '2': True,
            '3': False,
        }.get(value)




class CheckboxSelectMultiple(DJCheckboxSelectMultiple):
    input_type = 'checkbox'
    template_name = 'gentelella/widgets/checkbox_select.html'
    option_template_name = 'gentelella/widgets/checkbox_option.html'

    def __init__(self, attrs=None, check_test=None):
        attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='flat ')
        super().__init__(attrs)

class SplitDateTimeWidget(DJSplitDateTimeWidget):
    template_name = 'gentelella/widgets/splitdatetime.html'
    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class SplitHiddenDateTimeWidget(DJSplitHiddenDateTimeWidget):
    template_name = 'gentelella/widgets/splithiddendatetime.html'
    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class SelectDateWidget(DJSelectDateWidget):
    template_name = 'gentelella/widgets/select_date.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class PhoneNumberMaskInput(TextInput):
    input_type = 'text'
    template_name = 'gentelella/widgets/phone_number_input_mask.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)

        super().__init__(attrs)

class DateMaskInput(DJDateInput):
    format_key = 'DATE_INPUT_FORMATS'
    template_name = 'gentelella/widgets/date_input_mask.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class DateTimeMaskInput(DJDateTimeInput):
    format_key = 'DATETIME_INPUT_FORMATS'
    template_name = 'gentelella/widgets/datetime_input_mask.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class EmailMaskInput(TextInput):
    template_name = 'gentelella/widgets/email_input_mask.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)

        super().__init__(attrs)

class DateRangeTimeInput(DJDateTimeInput):
    format_key = 'DATETIME_INPUT_FORMATS'
    template_name = 'gentelella/widgets/daterangetime.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)


class DateRangeInput(DJDateInput):
    format_key = 'DATE_INPUT_FORMATS'
    template_name = 'gentelella/widgets/daterange.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)
