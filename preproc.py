def mileagePreproc(milage):

    if milage == "---": return float('NaN')
    if type(milage) is float: return milage
    
    num_str, unit = milage.split(" ")
    
    num_str = num_str.replace(",", "")

    # Convert to integer

    num = int(num_str)

    if "km" in unit:
        pass
    elif "mi" in milage:
        num *= 1.60934

    return num

def pricePreproc(price):

    if "No" in price:
        return float('NaN')

    # £1,100
    price = price.replace(",", "")
    # £1100
    if "£" in price:
        price = price.replace("£", "")
        # "1100"
        price = int(price) * 1.15 
    elif "€" in price:
        price = price.replace("€", "")
        price = int(price)

    return price

def yearPreproc(year):
    if type(year) is float:
        return float('NaN')
    if year == "---":
        return float('NaN')
    return int(year)

def engSizePreproc(engSize):
    if type(engSize) is float:
        return engSize
    if engSize == "---":
        return float('NaN')
    return float(engSize.replace("litre", ""))

def powerPreproc(power):
    if type(power) is float:
        return power
    if power == "---":
        return float('NaN')
    return float(power.replace("hp", ""))
