from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Employee
cursor = connection.cursor()


def raw_sql_type1(request):
    # to retrieve data

    # query = 'select * from app1_employee'
    # cursor.execute(query)
    # for record in cursor:
    #     print(record)

    # to insert records

    # query = 'insert into app1_employee(name, salary) values ("pratik", 1020), ("vijay", 2300)'
    # cursor.execute(query)

    # to update record

    # query = 'update app1_employee set salary=5000 where id=5'
    # cursor.execute(query)

    # to delete record
    # query = 'delete from app1_employee where id=5'
    # cursor.execute(query)
    return HttpResponse('method 1')


def raw_sql_type2(request):
    # to retrieve data

    # query = 'select * from app1_employee'
    # employees = Employee.objects.raw(query)
    # for employee in employees:
    #     print(employee)

    return HttpResponse('method 2')


