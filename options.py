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
def buy_share(price,num):
	global total_shares
	global total_cost

	total_shares+=num
	total_cost+=(price*num)
	print_trasact()
	print('Transact: Buy '+str(num)  +' shares @$'+str(price)+'/share')

# ---------------------------------------------------------------------
def buy_put(price,cost):
	global total_cost
	global my_put

	my_put=price
	total_cost+=(cost*100)
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
# Buy stock 1
cur_price=100
buy_share(cur_price,33)
print_balance(cur_price)

# Buy stock 2
cur_price=80
buy_share(cur_price,33)
print_balance(cur_price)

# Buy put
cur_price=110
buy_put(110,5)
print_balance(cur_price)

# Buy stock 3
cur_price=120
buy_share(cur_price,34)
print_balance(cur_price)
