import datetime

class Auction:
    def __init__(self, item_name, starting_price):
        self.item_name = item_name
        self.starting_price = starting_price
        self.current_bid = starting_price
        self.bids = []
        self.is_active = True
        self.start_time = datetime.datetime.now()

    def place_bid(self, bidder_name, bid_amount):
        if not self.is_active:
            return "Auction is closed."
        if bid_amount <= self.current_bid:
            return "Bid must be higher than the current bid."
        self.current_bid = bid_amount
        self.bids.append((bidder_name, bid_amount))
        return "Bid placed successfully."

    def close_auction(self):
        self.is_active = False
        return f"Auction closed. Winning bid: {self.current_bid} by {self.bids[-1][0]}"

    def get_status(self):
        status = {
            "item_name": self.item_name,
            "starting_price": self.starting_price,
            "current_bid": self.current_bid,
            "is_active": self.is_active,
            "bids": self.bids
        }
        return status

class OnlineAuctionSystem:
    def __init__(self):
        self.auctions = []

    def create_auction(self):
        item_name = input("Enter the item name: ")
        starting_price = float(input("Enter the starting price: "))
        auction = Auction(item_name, starting_price)
        self.auctions.append(auction)
        print(f"Auction created for {item_name} with a starting price of {starting_price}.")

    def view_auctions(self):
        if not self.auctions:
            print("No active auctions.")
            return
        for i, auction in enumerate(self.auctions):
            if auction.is_active:
                status = auction.get_status()
                print(f"Auction {i + 1}:")
                print(f"  Item: {status['item_name']}")
                print(f"  Current Bid: {status['current_bid']}")
                print(f"  Bids: {status['bids']}")
                print()

    def place_bid(self):
        self.view_auctions()
        auction_index = int(input("Enter the auction number to place a bid: ")) - 1
        if auction_index < 0 or auction_index >= len(self.auctions):
            print("Invalid auction number.")
            return
        auction = self.auctions[auction_index]
        bidder_name = input("Enter your name: ")
        bid_amount = float(input("Enter your bid amount: "))
        result = auction.place_bid(bidder_name, bid_amount)
        print(result)

    def close_auction(self):
        self.view_auctions()
        auction_index = int(input("Enter the auction number to close: ")) - 1
        if auction_index < 0 or auction_index >= len(self.auctions):
            print("Invalid auction number.")
            return
        auction = self.auctions[auction_index]
        result = auction.close_auction()
        print(result)

def main():
    system = OnlineAuctionSystem()
    while True:
        print("Online Auction System")
        print("1. Create Auction")
        print("2. View Auctions")
        print("3. Place Bid")
        print("4. Close Auction")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            system.create_auction()
        elif choice == '2':
            system.view_auctions()
        elif choice == '3':
            system.place_bid()
        elif choice == '4':
            system.close_auction()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
