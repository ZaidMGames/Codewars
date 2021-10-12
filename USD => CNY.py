def usdcny(usd):
    exchange = usd * 6.75
    format_float = "{:.2f}".format(exchange)
    return str(format_float) +  " Chinese Yuan"