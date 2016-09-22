bill_total = float(raw_input('What was the total bill? '))
service_rating = raw_input('Rate the service (Good, Fair, or Bad): ')
split_bill = float(raw_input('Split the bill how many ways? (1 for none): '))

if service_rating == 'Good':
    tip_total = bill_total * 0.20
elif service_rating == 'Fair':
    tip_total = bill_total * 0.15
elif service_rating == 'Bad':
    tip_total = bill_total * 0.10
else:
    print 'Please Type Good, Fair, or Bad as a rating.'


bill_with_tip = tip_total + bill_total

if split_bill > 1:
    bill_per_person = bill_with_tip/split_bill
    print 'Tip to give: ' + str('%.2f' % tip_total)
    print 'Bill with tip: ' + str('%.2f' % bill_with_tip)
    print 'Amount per person: ' + str('%.2f' % (bill_with_tip/split_bill))

else:
    print 'Tip to give: ' + str('%.2f' % tip_total)
    print 'Bill with tip: ' + str('%.2f' % bill_with_tip)
