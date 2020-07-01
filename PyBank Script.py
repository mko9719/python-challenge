import csv
import statistics

count_months = 0
total = 0
ls = []
this_value = 0
previous_value = 0
biggest_increase = 0
biggest_increase_month = ""
biggest_decrease = 0
biggest_decrease_month = ""

#opens csv
with open('PyBank/Resources/budget_data.csv', mode = 'r')as csv_file:
    y = csv.reader(csv_file, delimiter = ',')
    next(y, None)
    for lines in y:
        this_value = int(lines[1])
        if(previous_value == 0):
            previous_value = this_value
        if((this_value-previous_value) > 0):
            if((this_value-previous_value) > biggest_increase):
                biggest_increase = this_value
                biggest_increase_month = (lines[0])
        if((this_value-previous_value) < 0):
            if((this_value-previous_value) < biggest_decrease):
                biggest_decrease = this_value
                biggest_decrease_month = (lines[0])
        total = total + int(lines[1])
        count_months = count_months + 1 
        ls.append(int(lines[1]))
        previous_value = this_value



a = statistics.stdev(ls)
print("Total Months "  + str(count_months))
print("Total $" + str(total))
print("Average Change " + str(a))
print("Greatest Increase " + str(biggest_increase) + " " + str(biggest_increase_month))
print("Greatest Decrease " + str(biggest_decrease) + " " + str(biggest_decrease_month))
