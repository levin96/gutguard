# ODS Creation Schema

To create a spreadsheet using `scripts/create_ods.py`, you must provide a JSON configuration file.

## Structure

```json
{
  "styles": {
    "header": {
      "background_color": "#cccccc",
      "font_weight": "bold",
      "border": "0.5pt solid #000000"
    }
  },
  "sheets": [
    {
      "name": "Inventory",
      "rows": [
        {
          "cells": [
            {"value": "Item ID", "style": "header"},
            {"value": "Item Name", "style": "header"},
            {"value": "Price", "style": "header"}
          ]
        },
        {
          "cells": [
            "ID001",
            "Widget A",
            {"value": 19.99, "type": "currency"}
          ]
        }
      ]
    }
  ]
}
```

## Cell Types
- `string` (default)
- `float` or `currency` (numeric value)
- `date` (ISO format string)

## Formulas
Use the `"formula"` key in a cell object. Formulas should follow the OpenFormula standard (often starting with `of:=`).
Example: `{"value": 0, "formula": "of:=[.B2]*[.C2]", "type": "float"}`

## Styles
Supported properties:
- `background_color`: Hex code (e.g., `#FF0000`)
- `font_weight`: `bold` or `normal`
- `font_size`: e.g., `12pt`
- `color`: Hex code for text color
- `border`: e.g., `0.5pt solid #000000`
