#!/usr/bin/env python3
import sys
import json
import os

try:
    from odf.opendocument import OpenDocumentSpreadsheet
    from odf.table import Table, TableRow, TableCell
    from odf.text import P
    from odf.style import Style, TextProperties, TableColumnProperties, TableCellProperties, TableRowProperties, ParagraphProperties
    from odf.number import TimeStyle, Hours, Minutes, Text as NumberText
except ImportError:
    print("Error: 'odfpy' library is not installed. Please install it using: pip install odfpy")
    sys.exit(1)

def create_ods(config, output_path):
    doc = OpenDocumentSpreadsheet()

    # Create common data styles
    # HH:MM Time Style
    hhmm_style = TimeStyle(name="HHMM")
    hhmm_style.addElement(Hours(style="long"))
    hhmm_style.addElement(NumberText(text=":"))
    hhmm_style.addElement(Minutes(style="long"))
    doc.styles.addElement(hhmm_style)

    # Create styles
    styles = {}
    if 'styles' in config:
        for name, props in config['styles'].items():
            s = Style(name=name, family="table-cell")
            if 'background_color' in props:
                s.addElement(TableCellProperties(backgroundcolor=props['background_color']))
            if 'font_weight' in props:
                s.addElement(TextProperties(fontweight=props['font_weight']))
            if 'font_size' in props:
                s.addElement(TextProperties(fontsize=props['font_size']))
            if 'color' in props:
                s.addElement(TextProperties(color=props['color']))
            if 'border' in props:
                 s.addElement(TableCellProperties(border=props['border']))
            if 'text_align' in props:
                s.addElement(ParagraphProperties(textalign=props['text_align']))
            
            # Apply data style if requested
            if props.get('data_style') == 'HH:MM':
                s.setAttribute("datastylename", "HHMM")

            doc.automaticstyles.addElement(s)
            styles[name] = s

    for sheet_config in config.get('sheets', []):
        table = Table(name=sheet_config.get('name', 'Sheet'))
        
        # Handle column widths if defined
        if 'column_widths' in sheet_config:
            for i, width in enumerate(sheet_config['column_widths']):
                 col_style = Style(name=f"col_{sheet_config['name']}_{i}", family="table-column")
                 col_style.addElement(TableColumnProperties(columnwidth=width))
                 doc.automaticstyles.addElement(col_style)
                 # Note: applying col styles in odfpy requires a bit more care, 
                 # for now we focus on content and basic formatting.

        for row_data in sheet_config.get('rows', []):
            tr = TableRow()
            if 'style' in row_data:
                 # Row styles (like height)
                 pass

            for cell_data in row_data.get('cells', []):
                tc = TableCell()
                if isinstance(cell_data, dict):
                    val = cell_data.get('value', '')
                    style_name = cell_data.get('style')
                    formula = cell_data.get('formula')
                    value_type = cell_data.get('type', 'string')

                    if style_name and style_name in styles:
                        tc.setAttribute("stylename", style_name)
                    
                    if formula:
                        tc.setAttribute("formula", formula)
                    
                    if value_type == 'float' or value_type == 'currency':
                        tc.setAttribute("valuetype", "float")
                        tc.setAttribute("value", str(val))
                    elif value_type == 'date':
                        tc.setAttribute("valuetype", "date")
                        tc.setAttribute("datevalue", str(val))
                    elif value_type == 'time':
                        tc.setAttribute("valuetype", "time")
                        if val:
                            tc.setAttribute("timevalue", str(val))
                    else:
                        tc.setAttribute("valuetype", "string")

                    tc.addElement(P(text=str(val)))
                else:
                    tc.setAttribute("valuetype", "string")
                    tc.addElement(P(text=str(cell_data)))
                
                tr.addElement(tc)
            table.addElement(tr)
        doc.spreadsheet.addElement(table)

    doc.save(output_path)
    print(f"Spreadsheet saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: create_ods.py <config_json_path> <output_ods_path>")
        sys.exit(1)
    
    config_path = sys.argv[1]
    output_path = sys.argv[2]
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    create_ods(config, output_path)
