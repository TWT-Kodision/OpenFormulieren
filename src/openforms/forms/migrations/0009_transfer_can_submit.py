# Generated by Django 2.2.25 on 2021-12-13 11:43

from django.db import migrations

from openforms.forms.constants import SubmissionAllowedChoices


def forwards_func(apps, schema_editor):
    Form = apps.get_model("forms", "Form")
    forms = Form.objects.all()

    for form in forms:
        if form.can_submit:
            form.submission_allowed = SubmissionAllowedChoices.yes
        else:
            form.submission_allowed = SubmissionAllowedChoices.no_with_overview
    Form.objects.bulk_update(forms, ["submission_allowed"])


def backwards_func(apps, schema_editor):
    Form = apps.get_model("forms", "Form")
    forms = Form.objects.all()

    for form in forms:
        if form.submission_allowed != SubmissionAllowedChoices.yes:
            form.can_submit = False
        else:
            form.can_submit = True
    Form.objects.bulk_update(forms, ["can_submit"])


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0008_form_submission_allowed"),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]
