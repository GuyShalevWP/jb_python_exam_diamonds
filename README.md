# Diamond Data Analysis

Data Analysis with basic Python exam

## Functions

`helpers/data_manage.py`

- **load_diamonds_from_csv**: Loads diamond data from a CSV file. Initializes with an empty list if the file doesn't exist or is invalid.

`helpers/func.py`

- **highest_diamond_price**: Prints the highest diamond price.
- **average_diamond_price**: Prints the average diamond price.
- **count_ideal_diamonds**: Prints the number of Ideal cut diamonds.
- **diamond_colors**: Prints the number of different diamond colors and lists them.
- **median_carat_of_premium**: Prints the median carat size of Premium cut diamonds.
- **average_carat_by_cut**: Prints the average carat size for each cut type.
- **average_price_by_color**: Prints the average price for each color.

`helpers/clear_terminal.py`

- **clear_screen**: Clears the console screen.

`app.py`

- **menu**: Displays action menu and prompts user to select one.
- **Main Script Execution**: Loads diamond data, displays menu, performs actions (highest price, average price, count Ideal diamonds, list colors, median carat of Premium diamonds, average carat by cut, average price by color), and handles user inputs.
