# Internet Shop Simulator

A Python-based command-line shopping cart simulator. Add, modify, delete, or clear products from categories like food, drinks, and self-care. Features dynamic pricing and a simple menu-driven interface.

## Features

- **Product Categories**: Food (fruits, bread, dairy), Drinks (soft drinks, juices), Self-Care (shampoo, deodorants, toothpaste).  
- **Cart Management**: Add, modify, delete, or clear products.  
- **Dynamic Pricing**: Prices adjust based on quantity (e.g., weight for fruits, units for bread).  
- **User-Friendly Interface**: Simple text menu for easy navigation.  

## Requirements

- **Python 3.x** or higher.  
- No external libraries required.  

## How to Run

1. Clone or download this repository.  
2. Open your terminal or command prompt.  
3. Navigate to the directory where the script is located.  
4. Run the script:  

```bash
python main.py
```

## Usage

- **Add**: Add products to the cart.
- **Modify**: Change product or quantity.
- **Delete**: Remove specific products.
- **Clear**: Empty the cart.
- **Products**: View cart and total price.

## Simulation: Internet Shop Flow
```
Welcome to the Internet Shop!
Press "1" to shop or "0" to exit.
::: 1

Choose: "Add", "Modify", "Delete", "Clear", or "Products".
::: Add

Select category: Food, Drinks, Self-Care.
::: Food

Choose product: Apple, Banana, Lemon.
::: Apple

Enter weight (kg): 2

2.0kg of "Apple" added. Total: $3.00
```

## Code Structure 

- **Product Prices**: Stored in dictionaries for easy access and updates.
- **Cart Management**: The cart is represented as a dictionary, with products as keys and their details (quantity, price) as values.

## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/Internet-Shop)**

