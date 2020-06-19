#!/usr/bin/env python
# mortgage.py
#
# Exercise 1.7

month = 0
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 48
extra_payment_end_month = 60
extra_payment = 1000

while principal > 0:
    while month < extra_payment_start_month and month > extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
        print(month, total_paid, principal)
        month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, total_paid, principal)
    month = month + 1

print('Months =', month)
print('Total paid', round(total_paid, 2))
