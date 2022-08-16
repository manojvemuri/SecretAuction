from replit import clear
from art import logo
print(logo)
print("Welcome to the Secret Auction\n")
should_continue = 1
auction={}

def highest_bidder(auc_list):
  highest_bid=0
  winner=0
  for bidder  in auc_list:
    amount=int(auc_list[bidder])
    if highest_bid<amount:
      highest_bid=amount
      winner=bidder
  print(f"Winner is {winner} and the highest bid amount is {highest_bid}")

while should_continue==1:
  bidder=input("\n What's Your Name : ")
  bid=input("\n Whats yor Bid? : $")
  auction[bidder]=bid
  reloop=input("\n Are there any other bidders? Type'yes' or 'no' : ").lower()
  if reloop=="yes":
    should_continue= 1
  elif reloop=="no":
    should_continue= 0
  clear()

print(auction)
highest_bidder(auction)

    
    