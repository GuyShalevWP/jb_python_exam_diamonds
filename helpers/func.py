from statistics import median, mean

def highest_diamond_price(diamonds):
    highest_price = max(diamonds, key=lambda x: x['price'])['price']
    print(f'Highest diamond price: {highest_price}')

def average_diamond_price(diamonds):
    avg_price = mean(diamond['price'] for diamond in diamonds)
    print(f'Average diamond price: {avg_price}')

def count_ideal_diamonds(diamonds):
    ideal_count = sum(1 for diamond in diamonds if diamond['cut'] == 'Ideal')
    print(f'Number of Ideal diamonds: {ideal_count}')

def diamond_colors(diamonds):
    colors = set(diamond['color'] for diamond in diamonds)
    color_list = list(colors)
    print(f'There are {len(colors)} different colors: {", ".join(color_list)}')

def median_carat_of_premium(diamonds):
    premium_diamonds = [diamond['carat'] for diamond in diamonds if diamond['cut'] == 'Premium']
    med_carat = median(premium_diamonds)
    print(f'Median carat of Premium diamonds: {med_carat}')

def average_carat_by_cut(diamonds):
    cuts = set(diamond['cut'] for diamond in diamonds)
    avg_carats = {cut: mean(diamond['carat'] for diamond in diamonds if diamond['cut'] == cut) for cut in cuts}
    for cut, avg_carat in avg_carats.items():
        print(f'Average carat for {cut} cut: {avg_carat}')

def average_price_by_color(diamonds):
    colors = set(diamond['color'] for diamond in diamonds)
    avg_prices = {color: mean(diamond['price'] for diamond in diamonds if diamond['color'] == color) for color in colors}
    for color, avg_price in avg_prices.items():
        print(f'Average price for {color} color: {avg_price}')