import art
print(art.logo)
auction_info = {}

while True:
    name = input('What is your name?  ')
    bid_price = input('What is your bid? $ ')
    auction_info[name] = int(bid_price)
    is_there_any_other_bid = input(
        "Are there any other bidders? Type 'yes' or 'no'.").lower()
    if is_there_any_other_bid == 'no':
        break
max_bid = 0
temp_name = ''
for key in auction_info:

    if int(auction_info[key]) > max_bid:
        temp_name = key
        max_bid = auction_info[key]
print(f"The winner is {temp_name} with a bid of ${max_bid}")
