#Cash register function
#Take in total cost as input
#returns the exact change in standard denomination



#function accepts a total cost (float)
#returns a denomination (dict)
def cash_register(total_cost: float,payment: float) -> dict:
    #edge case, if payment is less than total cost, 
    #void the transaction
    if total_cost > payment:
        return "Invalid transaction! Payment is less than cost of item!" 
    #dictionary to track denomination
    #bills,1,2,5,10,20,50,100 bills (int)
    #coins: 1,5,10,25 (int)
    denomination_array = [100,50,20,10,5,2,1,0.25,0.10,0.05,0.01]
    denomination_dict = {}
    #total change that customer is getting back
    customer_change = payment - total_cost

    #loop through array and init dictionary with
    #denomination and counter
    for denom in denomination_array:
        denomination_dict[denom] = 0

    #return the amount with the lowest number of denomination
    current_change = customer_change
    for denom in denomination_array:
        #keep track of current change value
        if current_change >= denom:
            denom_count = int(current_change / denom)
            remainder = current_change % denom
            #increment the count in the dict
            denomination_dict[denom] =+ denom_count
            current_change = current_change - (denom_count * denom)
        #need to round the current change to nearest 2-digit floating point
        current_change = round(current_change,2)

    return denomination_dict

#test case
#[1.01,2],
test_cases = [[1.01,2],[101,200],[1,0]]

for testc in test_cases:
    print("Test case: " + str(testc))
    print(cash_register(testc[0],testc[1]))

            
        

        


        