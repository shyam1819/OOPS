# Encapsulation

Encapsulation is the bundling of data (variables) and the methods that operate on that data into a single unit (class). Crucially, it involves Data Hiding using access modifiers like private.


# Why encapsulation is needed

Real-World Use Case: Bank Account Management
Think about a BankAccount class. You wouldn't want any other part of the program to be able to do account.balance = 1000000.

The Bundle: The balance variable is marked private.

The Control: You provide a deposit() method. Inside this method, you can add validation: Is the amount positive? Is the user authenticated?

The Benefit: It ensures Data Integrity. By forcing all changes through specific methods, you guarantee the internal state of your object remains valid and protected from accidental (or malicious) corruption.
