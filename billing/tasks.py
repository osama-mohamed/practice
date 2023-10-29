from __future__ import absolute_import, unicode_literals


from celery import shared_task, Task, Celery


app = Celery('billing')


@app.task(name='add_two_numbers')
# @shared_task
def add(x, y):
  return x + y

@app.task(name='mul_two_numbers')
def mul(x, y):
  return x * y

@app.task(name='xsum_two_numbers')
def xsum(numbers):
  return sum(numbers)