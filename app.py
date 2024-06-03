from enum import Enum
from helpers.clear_terminal import clear_screen
from helpers.data_manage import load_diamonds_from_csv
from helpers.func import highest_diamond_price, average_diamond_price, count_ideal_diamonds, diamond_colors, median_carat_of_premium, average_carat_by_cut, average_price_by_color

class Actions(Enum):
    HIGHEST_DIAMOND_PRICE = 1
    AVRAGE_DIAMOND_PRICE = 2
    COUNT_IDEAL = 3
    DIAMOND_COLORS = 4
    MEDIAN_CARAT_OF_PREMIUM = 5
    AVERAGE_CARAT_BY_CUT = 6
    AVERAGE_PRICE_BY_COLOR  = 7
    EXIT = 8

def menu():
    for action in Actions:
        print(f'{action.value} - {action.name}')
    return Actions(int(input('Select one: ')))

if __name__ == '__main__':
    clear_screen()
    diamonds_data = load_diamonds_from_csv('data/data.csv')
    while True:
        try:
            action = menu()
            if action == Actions.HIGHEST_DIAMOND_PRICE:
                clear_screen()
                highest_diamond_price(diamonds_data)
            elif action == Actions.AVRAGE_DIAMOND_PRICE:
                clear_screen()
                average_diamond_price(diamonds_data)
            elif action == Actions.COUNT_IDEAL:
                clear_screen()
                count_ideal_diamonds(diamonds_data)
            elif action == Actions.DIAMOND_COLORS:
                clear_screen()
                diamond_colors(diamonds_data)
            elif action == Actions.MEDIAN_CARAT_OF_PREMIUM:
                clear_screen()
                median_carat_of_premium(diamonds_data)
            elif action == Actions.AVERAGE_CARAT_BY_CUT:
                clear_screen()
                average_carat_by_cut(diamonds_data)
            elif action == Actions.AVERAGE_PRICE_BY_COLOR :
                clear_screen()
                average_price_by_color(diamonds_data)
            elif action == Actions.EXIT:exit()

        except ValueError:
            clear_screen()
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
    