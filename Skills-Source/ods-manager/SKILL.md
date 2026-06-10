---
name: ods-manager
description: Create and manage complex OpenOffice Spreadsheet (.ods) files from scratch. Use when Gemini CLI needs to build professional inventory systems, financial reports, or structured data trackers with formatting and formulas.
---

# ODS Manager

This skill allows you to programmatically create complex OpenDocument Spreadsheets (.ods) for professional use, such as inventory management.

## Core Workflows

### 1. Generating a New Spreadsheet
To create a spreadsheet from scratch:
1.  **Define the Structure**: Determine the sheets (e.g., Inventory, Dashboard), columns, and rows needed.
2.  **Plan the Usability**: Refer to [inventory_best_practices.md](references/inventory_best_practices.md) for layout and functionality tips.
3.  **Prepare the Config**: Create a JSON configuration following the [schema.md](references/schema.md).
4.  **Execute the Script**: Run `python3 scripts/create_ods.py <config.json> <output.ods>`.

### 2. Implementation Guide
- **Complex Documents**: Use multiple sheets and structured cross-references.
- **Formulas**: Use OpenFormula syntax (e.g., `of:=[.B2]*[.C2]`).
- **Formatting**: Define styles in the `styles` section of the JSON for headers, alerts, and highlighting.

## Dependencies
This skill requires the `odfpy` Python library. If it is not installed, provide instructions to the user to install it:
`pip install odfpy`

## Referencing Bundled Material
- **[schema.md](references/schema.md)**: Details on the JSON configuration format.
- **[inventory_best_practices.md](references/inventory_best_practices.md)**: Specialized guide for high-usability inventory spreadsheets.
- **[create_ods.py](scripts/create_ods.py)**: The execution engine for generating the files.
