#!/usr/bin/env python
# mortgage.py
#
# Exercise 1.7

month = 0
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_months = 12

while principal > 0:
    while month < extra_payment_months:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
        month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month = month + 1

print('Months =', month)
print('Total paid', round(total_paid, 2))
