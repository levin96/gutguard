# Inventory Spreadsheet Best Practices

To create a high-usability inventory system in OpenOffice Calc:

## 1. Sheet Structure
- **Dashboard/Summary**: High-level metrics (Total Value, Low Stock Alerts).
- **Master Inventory**: The main database of items.
- **Transactions/Logs**: A record of items coming in and out (don't just update the Master sheet, log the change).
- **Settings/Lookups**: Define categories, locations, and vendors here to use in dropdowns.

## 2. Usability Features
- **Frozen Rows**: Always freeze the header row (Row 1) so it stays visible while scrolling.
- **Alternating Row Colors**: Use a light gray background for every second row to improve readability.
- **Data Validation**: Use dropdown lists for columns like "Category" or "Status" to prevent typos.
- **Conditional Formatting**: Highlight rows in red when "Current Stock" is less than "Minimum Level".

## 3. Formulas for Inventory
- **Total Value**: `=PRICE * QUANTITY`
- **Automatic Reorder Status**: `=IF(STOCK <= MIN_LEVEL, "REORDER", "OK")`
- **Dynamic Stock Calculation**: If using a Log sheet, calculate current stock in the Master sheet using `SUMIF` from the Log sheet.

## 4. ODS-Specific Tips
- Use standard fonts like `Liberation Sans` or `Arial` for cross-platform compatibility.
- Set column widths appropriately (Item descriptions need more space than ID numbers).
