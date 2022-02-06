from django.contrib import admin
from django import forms
from django.shortcuts import render, redirect
from .models import Registry, Zmk
from django.urls import path
import pandas as pd


def parsing_excel(df) -> dict:
    """
    df - pandas dataframe from excel file
    return dict data
    Функция очищает пустый столбики данных и столбики в которых не заполнены поля даты
    """
    result_dict = {}
    row_names = df.iloc[1]
    zmk_has_names = pd.isnull(row_names)
    zmk_names = [name for name, has_name in zip(row_names.tolist(), zmk_has_names) if not has_name]
    df_start_position = [i + 1 for i, value in enumerate((pd.isnull(df.iloc[3])).tolist()) if value]
    df_start_position.append(df.shape[1] + 1)
    rows_count = df.shape[0]
    rows = [i for i in range(4, rows_count)]
    for num, index in enumerate(df_start_position[:-1]):
        result_dict[zmk_names[num]] = {}
        end = df_start_position[num + 1] - 1
        columns = [i for i in range(index, end)]
        column_names = (df.iloc[3]).tolist()[index: end]
        columns_count = len(columns)
        objects_count = columns_count - 5
        objects_nums = [i for i in range(2, objects_count + 2)]
        df0 = df.iloc[rows, columns]
        df_i = df0.dropna(thresh=3)  # нужно хотя бы 3 значения в строке
        for object_num in objects_nums:
            result_dict[zmk_names[num]][column_names[object_num]] = []
            df_i_obj = (df_i.iloc[:, [0, 1, object_num, columns_count - 1]]).dropna(thresh=4)
            for i, row in df_i_obj.iterrows():
                result_dict[zmk_names[num]][column_names[object_num]].append(row.tolist())
    return result_dict


def multy_save(data: dict):
    """"
    dict - dict with data from excel file
    """
    for zmk_name, value_dict in data.items():
        zmk_i, has_create = Zmk.objects.get_or_create(name=zmk_name)
        for object_name, value_list in value_dict.items():
            for values in value_list:
                obj, created = Registry.objects.update_or_create(
                    name=object_name,
                    num=values[0],
                    zmk=zmk_i,
                    defaults={
                        'departure_date': values[1],
                        'receiving_date': values[3],
                        'weight': values[2],
                    },
                )

@admin.register(Zmk)
class ZmkAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CsvImportForm(forms.Form):
    xlsx_file = forms.FileField()


@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    list_display = ('num', "name", 'weight', 'departure_date', 'receiving_date')
    date_hierarchy = 'departure_date'
    change_list_template = "entities/changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-xlsx/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            allowable_extensions = ('xlsx', 'xls')
            file = request.FILES["xlsx_file"]
            try:
                ext = file.name.split('.')[-1]
            except IndexError:
                ext = ''
            if ext in allowable_extensions:
                df = pd.read_excel(file.file)
                dict_data = parsing_excel(df)
                multy_save(dict_data)
                message = "Your xlsx file has been imported"
            else:
                message = "Invalid file extension"
            self.message_user(request, message)
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/xlsx_form.html", payload
        )
