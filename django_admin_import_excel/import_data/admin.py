from django.contrib import admin
from django import forms
from django.shortcuts import render, redirect
import csv
import sys
from django.http import HttpResponse, HttpResponseRedirect
from .models import Registry
from django.urls import path, reverse


class CsvImportForm(forms.Form):
    xlsx_file = forms.FileField()


@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    change_list_template = "entities/changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-xlsx/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            file = request.FILES["xlsx_file"]
            reader = csv.reader(file)
            print(file)
            print(file.name)
            print(reader)
            # with open(file.name) as f:
            #     lines = f.readlines()
            # for line in lines:
            #     print(line)
            # Create Hero objects from passed in data
            # ...
            self.message_user(request, "Your xlsx file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/xlsx_form.html", payload
        )
