def get_bets():
    # To-Do get input to get 4 odds
    return(2,1.82,1.94,1.87)

def check_for_opp(odds):
    if(min((1/odds[0]+(1/odds[1])),(1/odds[0]+(1/odds[3])),(1/odds[2]+(1/odds[1])),(1/odds[2]+(1/odds[3])))<1):
        return(True)
    else:
        return(False)

def arb_combination(odds):
    sum = 0
    odd = [0,0]
    if (odds[0]+odds[1]) > sum:
        sum = (odds[0]+odds[1])
        odd = [odds[0],odds[1]]
    if (odds[0]+odds[3]) > sum:
        sum = (odds[0]+odds[3])
        odd = [odds[0],odds[3]]
    if (odds[2]+odds[1]) > sum:
        sum = (odds[2]+odds[1])
        odd = [odds[2],odds[1]]
    if (odds[2]+odds[3]) > sum:
        sum = (odds[2]+odds[3])
        odd = [odds[2],odds[3]]
    return(odd)
    
def calculate_bet(wager,odd,bet):
    total = (1/odd[0]+1/odd[1])
    bet1 = round(((wager*1/odd[0])/total),2)
    bet2 = round(((wager*1/odd[1])/total),2)
    return([bet1,bet2])

def calculate_profit(bet,odd, wager):
    return1 = round((bet[0]*odd[0]-wager),2)
    return2 = round((bet[1]*odd[1]-wager),2)
    return(round((return1+return2)/2,2))
    
    
def main():
    wager = 50   
    odds = get_bets()
    if check_for_opp(odds) == False:
        print("No op exists, exiting")
    else:    
        odd = arb_combination(odds)
        bet = calculate_bet(wager,odd,wager)
        profit = (calculate_profit(bet,odd,wager))
        print("An Arbitrage opportunity exists")
        print(f"Odds to use are {odd[0]} & {odd[1]}")
        print(f"Place ${bet[0]} on {odd[0]} & ${bet[1]} on {odd[1]}")
        print(f"Profit against a total bet of {wager} is ${profit} ({(profit/wager)*100}% return)")
          
main()