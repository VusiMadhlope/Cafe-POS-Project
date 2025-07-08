## ☕Cafe-POS-Project 
Python Cafe POS Project

A fully functional Python made Point of Sale system for the Local Home Run Cafe.
It handles item selection, customization, payments and includes details receipts

## 📌 Flow Overview
1. User is welcomed.
2. Menu is displayed (pulled from a JSON File).
3. User selects their preferred items of choice.
4. An order is then placed.
5. Payment section is then shown and customer has the following payment. options; Cash, Card, Tap Payment and Scan to pay.
6. Upon payment the following two outcomes will be prompted.
-   Inavlid payment option message if payment options from above is not chosen.
-   Prompted to try again if invalid amount is entered.
-   Payment is sucessful if payment amount is enough.
-   Payment will decline due to insufficient funds.
7. Once payment is successful a  receipt will be printed included items selected, subtotal, vat and total.
8. Goodbye message and ending of program.

## ✨ Features
1. Menu Selection:
-   Menu is loaded from a JSON file (structured as a dictionary).

2. Order customization:
-   Users are able to customize their orders for example add additional items, extras.

3. Payment system:
-   Variety of payment options to cater for real life scenarios
-   General flow of payment outcome. If payment is less than total, payment will decline and customer is prompted to retry.
-   Else, payment will be accepted and successful if amount is greater than the subtotal

4. Receipt printing:
-   Receipt includes:
    -   All selected items with pricing
    -   Subtotal
    -   VAT Calculation
    -   Gratitude
    -   Total

## 🛠️ Tech Stack
-   Fully operated python project
-   JSON file

    