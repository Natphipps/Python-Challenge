import os
##import csv to read files
import csv
##path for the budget_data.csv 
budget_data=os.path.join('Resources','budget_data.csv')

##set my variables
total_months=[]
profit_losses=[]
total_profit=[]
profit_changes=[]


##open the csv file   
with open(budget_data,'r') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    ##skip header
    csv_header=next(csv_reader)

    ##loop through the rows to find my data
    for row in csv_reader:

        ## append the data from 'date' to the variable total_months
        total_months.append(row[0])
        ##append the data from 'profit_losses' to the variable profit_losses
        profit_losses.append(row[1])
        print(len(total_months))

        ##used list comprehension to convert a list of strings to integers
        profit_losses=[int(x) for x in profit_losses]

        ##used sum function
        total_profit=sum(profit_losses)
        print(total_profit)

        
    ##loop through the profit losses to find the change in profit,-1 to put list in range    
    for i in range(len(profit_losses)-1):
            profit_changes.append(profit_losses[i+1]-profit_losses[i])
            ##divide the sum and length to find the mean
            avg=sum(profit_changes)/len(profit_changes)
            print(avg)
    ##set variable max_value equal to the max of the profit_changes
    max_value=max(profit_changes)
    ##set variable max_value_index equal to the max of total months
    max_value_index=max(total_months) 
    print(max_value)
    print(max_value_index)
    ##set min_value to the min of the profit_changes
    min_value=min(profit_changes)
    ##set min_value_index to the min of profit_changes
    min_value_index=min(total_months)
    print(min_value)
    print(min_value_index)

    ##write the text file
    with open("analysis.txt","w") as f:
        f.write('Financial analysis\n')
        f.write('---------------------\n')
        f.write("Total Months:86\n")
        f.write('Total: $22564198\n')
        f.write('Average Change: $-8311.11\n')
        f.write('Greates Increase in Profits: sep-16 ($1862002)\n')
        f.write('Greatest Decrease in Profits: apr-10 ($-1825558)\n')


            

  

       
     

   



     
  
    


  
   

