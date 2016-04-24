#!/usr/bin/python
# ---------------------------------------------------------------------
# Paramaters 
base_price=100.00
buy1_per=20.0
buy2_per=40.0
put_cost=5.0
put_price=110.0
call_gain=20.0
print("Inital price: %02f"% base_price) 

# ---------------------------------------------------------------------
# Initial investment
transact_cnt=0
total_shares=0
total_cost=0
my_put=0
my_call=0

# ---------------------------------------------------------------------
def buy_share(num,price):
	global transact_cnt
	global total_shares
	global total_cost

	transact_cnt+=1
	total_shares+=num
	total_cost+=(price*num)
	print('Transcation #'+str(transact_cnt))
	print('Transact: Buy '+str(num)  +' shares @'+str(price)+'$/share')

# ---------------------------------------------------------------------
def print_balance(price):
	global total_shares
	global total_cost
	global my_put
	global my_call

	max_loss=my_put*total_shares-total_cost
	cur_gain=price*total_shares-total_cost
	print('Total Shares: '+str(total_shares)+' shares @'+str(total_cost/total_shares)+'$/share')
	print('Min Loss %: '+str(100.0*max_loss/total_cost)+'% Max Loss '+str(max_loss))
	print('Cur Gain %: '+str(100.0*cur_gain/total_cost)+'% Gain Loss '+str(cur_gain))
	
# ---------------------------------------------------------------------
# Simulation 
cur_price=base_price
buy_share(33,cur_price)
print_balance(cur_price)

# First buy
transact_cnt+=1
cur_price=base_price*(1+buy1_per/100.0)
cur_shares=33
total_shares+=cur_shares
total_cost+=(cur_price*cur_shares)
print('Transcation #'+str(transact_cnt))
print_balance(cur_price)

cur_put_base=put_price
cur_put_price=put_cost
my_put=cur_put_base
total_cost+=(cur_put_price*100)
print('Transact: Buy put @'+str(cur_put_price*100)+'$/100 shares')
print_balance(cur_price)

# Second buy
transact_cnt+=1
cur_price=base_price*(1+buy2_per/100.0)
cur_shares=34
total_shares+=cur_shares
total_cost+=(cur_price*cur_shares)
print('Transcation #'+str(transact_cnt))
print('Transact: Buy '+str(cur_shares)+' shares @'+str(cur_price)+'$/share')
print('Transact: Buy put @'+str(cur_put_price*100)+'$/100 shares')
print_balance(cur_price)

