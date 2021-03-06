# Generated by Django 2.2.24 on 2021-07-22 16:32

from django.db import migrations


def merge_url_endpoints(apps, schema_editor):
    SoapService = apps.get_model("stuf", "SoapService")
    for soap_service in SoapService.objects.all():
        if soap_service.url:
            if soap_service.endpoint_vrije_berichten:
                # If the optional partial endpoint_vrije_berichten is set, the service url is most likely a partial URL.
                soap_service.endpoint_beantwoord_vraag = (
                    f"{soap_service.url}/BeantwoordVraag"
                )
            else:
                # If the optional partial endpoint_vrije_berichten is not set, the service url is most likely used for all endpoints.
                soap_service.endpoint_beantwoord_vraag = soap_service.url

        # Set fully qualified URLs to allow full flexibility on these endpoints.
        if soap_service.endpoint_vrije_berichten:
            soap_service.endpoint_vrije_berichten = (
                f"{soap_service.url}{soap_service.endpoint_vrije_berichten}"
            )

        if soap_service.endpoint_ontvang_asynchroon:
            soap_service.endpoint_ontvang_asynchroon = (
                f"{soap_service.url}{soap_service.endpoint_ontvang_asynchroon}"
            )

        soap_service.save()


class Migration(migrations.Migration):

    dependencies = [
        ("stuf", "0005_auto_20210722_1827"),
    ]

    operations = [
        migrations.RunPython(merge_url_endpoints, migrations.RunPython.noop),
    ]
