from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

value_loan = 1_000_000
years = 5
month_years = years*12
value_installment = value_loan//month_years
date_take_loan = '20/12/2020'
due_installment_date = 20

date_take_loan_2 = datetime.strptime(date_take_loan, '%d/%m/%Y')
date_loan_br = date_take_loan_2.strftime('%d/%m/%Y')
final_date_loan = (date_take_loan_2 + relativedelta(years=5)).strftime\
('%d/%m/%Y')
print('---'*16)
print(f'O valor pego em empréstimo foi de R$1.000.000,00. Na data\
 {date_loan_br}.')

count = 1
count_month = date_take_loan_2 + relativedelta(months=1)
date_installment = count_month.strftime('%d/%m/%Y')
while count <= month_years:
    print('~-'*32)
    print(f'Nº parcela: {count}  Data do vencimento: \
{count_month.strftime('%d/%m/%Y')}\
  Valor parcela: {f'{value_installment:,.2f}'}')
    count += 1
    count_month += relativedelta(months=1)

print(' ')
print(' ')
print(' ')
print(' ')