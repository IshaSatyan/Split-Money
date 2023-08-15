Debt Settlement Algorithm
This script implements a debt settlement algorithm to find the path for balancing debts among a group of individuals.

Problem Statement
In a group of individuals, each person owes or is owed some amount of money by other individuals. The goal is to find a way to settle these debts in a way that minimizes the total number of transactions.

How it Works
The find_path function takes a dictionary parms as input, where keys are individuals' names and values are the amounts they owe or are owed. The script then calculates the maximum and minimum values in the parms dictionary. If the maximum and minimum values are not equal, it identifies two individuals—one with the maximum debt and one with the minimum debt—to perform a transaction between. The amount to be exchanged is the sum of their debts.

The script then updates the parms dictionary to reflect the new debt values after the transaction. This process continues until the debts are balanced or minimized.

Usage
Make sure you have Python installed on your system.

Run the script by executing the following command in your terminal:

Copy code
python debt_settlement.py
The script will print the transactions needed to settle the debts among the individuals.

Example
Consider the following example dictionary:

python
Copy code
parms = {
    "Lakshya": 120.0,
    "Mehul": -40.0,
    "Khush": -90.0,
    "Manish": 10.0,
}
Running the script with this input will result in a sequence of transactions to balance the debts among the individuals.

Note
This script demonstrates a simplified debt settlement algorithm. In real-world scenarios, more complex algorithms and considerations may be necessary for optimal debt settlement.