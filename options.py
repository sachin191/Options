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
def print_trasact():
	global transact_cnt

	transact_cnt+=1
	print('Transcation #'+str(transact_cnt)+' ------------')

# ---------------------------------------------------------------------
def buy_share(num,price):
	global total_shares
	global total_cost

	total_shares+=num
	total_cost+=(price*num)
	print_trasact()
	print('Transact: Buy '+str(num)  +' shares @$'+str(price)+'/share')

# ---------------------------------------------------------------------
def buy_put(num,price,cost):
	global total_cost
	global my_put

	my_put=price
	total_cost+=(num*cost*100)
	print_trasact()
	print('Transact: Buy put @'+str(cost*100)+'$/100 shares')

# ---------------------------------------------------------------------
def print_balance(price):
	global total_shares
	global total_cost
	global my_put
	global my_call

	max_loss=my_put*total_shares-total_cost
	cur_gain=price*total_shares-total_cost
	print('Total Shares: '+str(total_shares)+' shares @$'+str(total_cost/total_shares)+'/share')
	print('Min Loss %: '+str(100.0*max_loss/total_cost)+'% Max Loss $'+str(max_loss))
	print('Cur Gain %: '+str(100.0*cur_gain/total_cost)+'% Gain Loss $'+str(cur_gain))
	
# ---------------------------------------------------------------------
# Simulation 
cur_price=base_price
buy_share(33,cur_price)
print_balance(cur_price)

# First buy
cur_price=base_price*(1+buy1_per/100.0)
buy_share(33,cur_price)
print_balance(cur_price)

buy_put(1,put_price,put_cost)
print_balance(cur_price)

# Second buy
cur_price=base_price*(1+buy2_per/100.0)
buy_share(34,cur_price)
print_balance(cur_price)

