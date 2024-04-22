# Written by Anthony Luu

# the purpose of this code is to count the total number of LUEs for MSUD 
# accounts by month and route code. The route codes in this set are those in PP1.
# The data set is named "Altered MSUD Geocoded Data (02-13-2024)"

# data sum will be spanned from 01/2021-12/2023
# install month 01/2021 = 613
# install month 12/2023 = 648 

import csv


# create list of each row
results = []
with open("Altered MSUD Geocoded Data (02-13-2024).csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: # each row is a list
        results.append(row)
        
data = []
for i in range(1,len(results)):
    #routes , LUEs, install month
    data.append([results[i][0][0:3],float(results[i][1]),int(results[i][2])])

#PP1 routes
routes = ['001','002','003','004','005','006','008','010','011','012','013','015','016','017','018','019','021','023','024','025','026','027','028','030','031','032','034','035','036','037','038','039','040','041','042','043','045','051','053','055','057','116']

sum_data = []
for i3 in range(613,649):
    for i4 in range(0,len(routes)):
        sum_data.append([i3,routes[i4]])
        
for i5 in range(0,len(sum_data)):
    tot=0
    for i in range(0,len(data)):
        if data[i][0]==sum_data[i5][1] and data[i][2]<=sum_data[i5][0]:
            tot = tot + data[i][1]
    sum_data[i5].append(tot)
    
fields = results[0]

# totals to CSV
# with open('totalLUE_by_month_and_route_results_PP1.csv', 'w') as f:
     
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
     
#     write.writerow(fields)
#     write.writerows(sum_data)

# find all route codes and sort them    
allroutes = set()
for i in range(len(data)):
    allroutes.add(data[i][0])
allroutes_sorted = list(allroutes)
allroutes_sorted.sort()    

sum_data_CCN = []
for i6 in range(613,649):
    for i7 in range(0,len(allroutes_sorted)):
        sum_data_CCN.append([i6,allroutes_sorted[i7]])
        
for i8 in range(0,len(sum_data_CCN)):
    tot_all=0
    for i9 in range(0,len(data)):
        if data[i9][0]==sum_data_CCN[i8][1] and data[i9][2]<=sum_data_CCN[i8][0]:
            tot_all = tot_all + data[i9][1]
    sum_data_CCN[i8].append(tot_all)
    

# totals to CSV
with open('totalLUE_by_month_and_route_results_CCN.csv', 'w') as f:
     
    # using csv.writer method from CSV package
    write_all = csv.writer(f)
     
    write_all.writerow(fields)
    write_all.writerows(sum_data_CCN)    

    

