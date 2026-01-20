class Bidder:
    def __init__(self, name, private_value):
        self.name = name
        self.private_value = private_value

    def __repr__(self):
        return f"{self.name} (Value: {self.private_value})"


def english_auction(bidders, start_price=10, step=10):
    print("\n=== ENGLISH AUCTION START ===")
    current_price = start_price
    active_bidders = bidders.copy()  # bidders still in auction
    winner = None

    while len(active_bidders) > 1:
        # Remove bidders who cannot pay next price
        active_bidders = [b for b in active_bidders if b.private_value >= current_price + step]
        if not active_bidders:
            break
        winner = active_bidders[-1]
        current_price += step

    if not winner:
        winner = max(bidders, key=lambda b: b.private_value)
        current_price = start_price if winner.private_value < start_price else winner.private_value

    print(f"Winner: {winner.name}")
    print(f"Final Price: {current_price}")
    print(f"Winner's Value: {winner.private_value}")
    print("=== AUCTION END ===")


def first_price_sealed_bid(bidders):
    print("\n=== FIRST-PRICE SEALED BID AUCTION START ===")
    bids = {b.name: b.private_value for b in bidders}
    winner_name = max(bids, key=bids.get)
    final_price = bids[winner_name]
    winner = next(b for b in bidders if b.name == winner_name)
    print(f"Winner: {winner.name}")
    print(f"Final Price (bid submitted): {final_price}")
    print(f"Winner's Value: {winner.private_value}")
    print("=== AUCTION END ===")


def second_price_auction(bidders):
    print("\n=== SECOND-PRICE (VICKREY) AUCTION START ===")
    bids = {b.name: b.private_value for b in bidders}
    sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
    winner_name, winner_bid = sorted_bids[0]
    second_price = sorted_bids[1][1] if len(sorted_bids) > 1 else winner_bid
    winner = next(b for b in bidders if b.name == winner_name)
    print(f"Winner: {winner.name}")
    print(f"Final Price (second-highest bid): {second_price}")
    print(f"Winner's Value: {winner.private_value}")
    print("=== AUCTION END ===")


if __name__ == "__main__":
    bidders = [
        Bidder("Alice", 120),
        Bidder("Bob", 150),
        Bidder("Charlie", 90),
        Bidder("Diana", 180)
    ]

    print("=== AUCTION SIMULATOR ===")
    print("Choose auction type:")
    print("1. English Auction")
    print("2. First-Price Sealed Bid Auction")
    print("3. Second-Price (Vickrey) Auction")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        english_auction(bidders)
    elif choice == "2":
        first_price_sealed_bid(bidders)
    elif choice == "3":
        second_price_auction(bidders)
    else:
        print("Invalid choice.")
