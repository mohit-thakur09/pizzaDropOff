# Pizza Drop Off - Python Command Line Pizza Ordering System

![pizzaDropOff](https://github.com/mohit-thakur09/pizzaDropOff/assets/82665617/1b0edb64-695f-4a35-a7d2-f9e3d0fe61c9)



The **Pizza Drop Off** is a Python command-line interface (CUI) project that allows users to select pizzas, beverages, and snacks with different types, flavors, and sizes and add them to their cart. The project utilizes various Python third-party libraries like `os`, `csv`, `random`, and `math` for bill calculation and CSV bill generation. It offers features such as user authentication, pizza selection, order cancellation, beverage selection, and CSV bill generation.

## Features

- **User Authentication**: Users can enter their details for authentication before placing an order.

- **Pizza Selection**:
  - Choose from a variety of pizzas with different types, flavors, and sizes.
  - Add multiple pizzas to the cart.

- **Order Cancellation**: Cancel the entire order and start over.

- **Beverage Selection**:
  - Select beverages to complement your pizza.
  - Choose from a range of options.

- **Bill Generation**: Automatically calculate and generate a CSV bill with all order details.

## Getting Started

Follow these steps to run the Pizza Drop Off application:

1. Clone or download this repository to your local machine.

2. Navigate to the project directory:

   ```bash
   cd pizza-drop-off
   ```

3. Run the application:

   ```bash
   python pizza_drop_off.py
   ```

4. Follow the on-screen instructions to interact with the Pizza Drop Off system.

## Usage

1. **User Authentication**:
   - Enter your details (e.g., name, phone number) for authentication.

2. **Pizza Selection**:
   - Choose from the available pizza options.
   - Specify the type (e.g., Margherita, Pepperoni), flavor, and size.
   - Add the selected pizza to your cart.

3. **Order Cancellation**:
   - If you want to cancel the entire order, use the cancel order option.

4. **Beverage Selection**:
   - Select beverages to go with your pizza order.
   - Choose from a list of available options (e.g., Coke, Pepsi).

5. **CSV Bill Generation**:
   - The system will automatically calculate your bill, including the cost of pizzas and beverages.
   - A CSV bill will be generated and saved in the `bills` folder.

## Project Structure

- `pizza_drop_off.py`: The main Python script for the Pizza Drop Off application.
- `menu.py`: Contains functions for displaying menus and taking user input.
- `bill.py`: Handles bill calculation and CSV bill generation.
- `bills/`: Contains CSV files for generated bills.
- `data/`: Stores pizza and beverage data in CSV files.

## Contributing

Contributions to this project are welcome. You can contribute by opening issues, providing feedback, or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy your pizza with Pizza Drop Off! 🍕
