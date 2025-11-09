def convexity(coupon, bond_yield, price):
    """ 
    Return convexity of function.
    
    Parameters:
    coupon(list of int or float):list of coupon payments including principal
    bond_yield(int or float): yield of bond
    price(float or int): current price of bond

    Returns:
    float: convexity of bond
    """
    res=0
    
    # run through all coupon payments to calculate yield
    for t in range(1,len(coupon)+1):
        res+=coupon[t-1]*(t)*(t+1)/(1+bond_yield)**(t+2)
    
    return res/price


def modified_duration(coupon, bond_yield, price):
    """ 
    Return modified duration of bond.
    
    Parameters:
    coupon(list of int or float):list of coupon payments including principal
    bond_yield(int or float): yield of bond
    price(float or int): current price of bond

    Returns:
    float: modified duration of bond
    """
    res=0
    
    for t in range(1,len(coupon)+1):
        res+=(t)*coupon[t-1]/(1+bond_yield)**(t+1)
    
    return res/price

def price_calulator(coupon_rate,face,time,ytm):
    """ 
    Return price of bond.
    
    Parameters:
    coupon_rate(int or float):coupon rate as % of face value
    face(int or float): face value of bond
    time(float or int): the time to maturity
    ytm(int or float): yield of bond

    Returns:
    float: price of bond
    list: list of coupon payment including principal
    """
    coupon=coupon_rate*face
    price=0
    for t in range(1,time+1):
        price+=coupon/(1+ytm)**t
    price+=face/(1+ytm)**time
    coupon_payments=[coupon]*time
    coupon_payments[-1]+=face
    return price, coupon_payments

ytm=float(input("Enter ytm:"))
time=int(input("Enter time until maturity:"))
face=int(input("Enter Face Value:"))
coupon_rate=float(input("Enter coupon rate:"))
price,coupon_payments=price_calulator(coupon_rate,face,time,ytm)
mod_duration=modified_duration(coupon_payments,ytm,price)
conv=convexity(coupon_payments,ytm,price)

print(f"Price of Bond is:{price:.2f}")
print(f"Modified Duration of bond is:{mod_duration:.2f}")
print(f"Convexity of bond is:{conv:.2f}")

