# Paramaters 
base_price=100.00
buy1_per=20.0
put_cost=5.0
call_gain=20.0
print("Inital price: %02f"% base_price) 

# Initial investment
total_shares=0
total_cost=0

# Simulation 
cur_price=base_price
cur_shares=33
total_shares+=cur_shares
total_cost+=(cur_price*cur_shares)
print('Transact: Buy '+str(cur_shares)+' shares @'+str(cur_price)+'$/share')
print('Total Shares: '+str(total_shares)+' Total cost: '+str(total_cost)+'$')
