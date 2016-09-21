bill_total = float(raw_input('What was the total bill? '))
service_rating = raw_input('Rate the service (Good, Fair, or Bad): ')
split_bill = float(raw_input('Split the bill? (1 for no): '))

if service_rating == 'Good':
    tip_total = bill_total * 0.20
elif service_rating == 'Fair':
    tip_total = bill_total * 0.15
elif service_rating == 'Bad':
    tip_total = bill_total * 0.10

bill_with_tip = tip_total + bill_total

print 'Tip to give: ' + str('%.2f' % tip_total)
print 'Bill with tip: ' + str('%.2f' % bill_with_tip)
print 'Amount per person: ' + str('%.2f' % (bill_with_tip/split_bill))
