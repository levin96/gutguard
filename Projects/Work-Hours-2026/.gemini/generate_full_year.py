import json
import calendar
from datetime import date, timedelta

def get_week_number(d):
    return d.isocalendar()[1]

year = 2026
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_de = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

config = {
    "styles": {
        "header": {"background_color": "#4a86e8", "font_weight": "bold", "color": "#ffffff", "border": "0.1pt solid #000000"},
        "week_even": {"background_color": "#ffffff", "border": "0.1pt solid #eeeeee"},
        "week_odd": {"background_color": "#f0f7ff", "border": "0.1pt solid #eeeeee"},
        "total": {"background_color": "#e0e0e0", "font_weight": "bold"}
    },
    "sheets": []
}

for m_idx, m_name in enumerate(months, 1):
    sheet = {"name": m_name, "rows": []}
    # Header
    sheet["rows"].append({
        "cells": [
            {"value": "CW", "style": "header"},
            {"value": "Date", "style": "header"},
            {"value": "Start", "style": "header"},
            {"value": "End", "style": "header"},
            {"value": "Break (min)", "style": "header"},
            {"value": "Total Hours", "style": "header"}
        ]
    })
    
    # Days
    num_days = calendar.monthrange(year, m_idx)[1]
    for d_idx in range(1, num_days + 1):
        curr_date = date(year, m_idx, d_idx)
        cw = get_week_number(curr_date)
        style = "week_even" if cw % 2 == 0 else "week_odd"
        
        day_str = f"{days_de[curr_date.weekday()]}, {d_idx:02d}.{m_idx:02d}."
        
        row_num = d_idx + 1
        formula = f"of:=( ([.D{row_num}]-[.C{row_num}])*24 ) - ([.E{row_num}]/60)"
        
        sheet["rows"].append({
            "cells": [
                {"value": f"W{cw}", "style": style},
                {"value": day_str, "style": style},
                {"value": "", "style": style},
                {"value": "", "style": style},
                {"value": 0, "style": style},
                {"value": 0, "formula": formula, "type": "float", "style": style}
            ]
        })
    
    # Monthly Total
    total_row = num_days + 2
    sheet["rows"].append({
        "cells": [
            "", "", "", "", 
            {"value": "Total:", "style": "total"},
            {"value": 0, "formula": f"of:=SUM([.F2]:[.F{num_days+1}])", "type": "float", "style": "total"}
        ]
    })
    
    config["sheets"].append(sheet)

with open('/home/levins/full_year_config.json', 'w') as f:
    json.dump(config, f)
