
import json
import calendar
from datetime import date, timedelta
import os
import subprocess

def get_week_number(d):
    return d.isocalendar()[1]

def generate_config(year):
    german_months = [
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ]
    german_days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    
    config = {
        "styles": {
            "header": {
                "background_color": "#4a86e8",
                "font_weight": "bold",
                "color": "#ffffff",
                "border": "0.1pt solid #000000"
            },
            "week_even": {
                "background_color": "#ffffff",
                "border": "0.1pt solid #eeeeee"
            },
            "week_odd": {
                "background_color": "#f0f7ff",
                "border": "0.1pt solid #eeeeee"
            },
            "week_even_time": {
                "background_color": "#ffffff",
                "border": "0.1pt solid #eeeeee",
                "data_style": "HH:MM"
            },
            "week_odd_time": {
                "background_color": "#f0f7ff",
                "border": "0.1pt solid #eeeeee",
                "data_style": "HH:MM"
            },
            "week_even_right": {
                "background_color": "#ffffff",
                "border": "0.1pt solid #eeeeee",
                "text_align": "end"
            },
            "week_odd_right": {
                "background_color": "#f0f7ff",
                "border": "0.1pt solid #eeeeee",
                "text_align": "end"
            },
            "total": {
                "background_color": "#e0e0e0",
                "font_weight": "bold",
                "border": "0.1pt solid #000000",
                "text_align": "end"
            }
        },
        "sheets": []
    }
    
    for month in range(1, 13):
        sheet = {
            "name": german_months[month-1],
            "rows": [
                {
                    "cells": [
                        {"value": "KW", "style": "header"},
                        {"value": "Datum", "style": "header"},
                        {"value": "Beginn", "style": "header"},
                        {"value": "Ende", "style": "header"},
                        {"value": "Pause (min)", "style": "header"},
                        {"value": "Urlaubstag", "style": "header"},
                        {"value": "Gesamtstunden", "style": "header"}
                    ]
                }
            ]
        }
        
        last_day = calendar.monthrange(year, month)[1]
        current_week = -1
        
        for day in range(1, last_day + 1):
            d = date(year, month, day)
            week_num = get_week_number(d)
            
            is_odd = week_num % 2 != 0
            style = "week_odd" if is_odd else "week_even"
            time_style = "week_odd_time" if is_odd else "week_even_time"
            right_style = "week_odd_right" if is_odd else "week_even_right"
            
            kw_value = f"KW{week_num}" if week_num != current_week else ""
            current_week = week_num
            
            row_idx = len(sheet["rows"]) + 1
            row = {
                "cells": [
                    {"value": kw_value, "style": style},
                    {"value": f"{german_days[d.weekday()]}, {day:02d}.{month:02d}.", "style": style},
                    {"value": "", "style": time_style, "type": "time"},
                    {"value": "", "style": time_style, "type": "time"},
                    {"value": 0, "style": right_style},
                    {"value": 0, "style": right_style},
                    {
                        "value": 0,
                        "formula": f"of:=( ([.D{row_idx}]-[.C{row_idx}])*24 ) - ([.E{row_idx}]/60)",
                        "type": "float",
                        "style": right_style
                    }
                ]
            }
            sheet["rows"].append(row)
        
        # Add Summe row
        last_row_idx = len(sheet["rows"])
        sheet["rows"].append({
            "cells": [
                {"value": "", "style": "total"},
                {"value": "", "style": "total"},
                {"value": "", "style": "total"},
                {"value": "", "style": "total"},
                {"value": "Summe:", "style": "total"},
                {
                    "value": 0,
                    "formula": f"of:=SUM([.F2]:[.F{last_row_idx}])",
                    "type": "float",
                    "style": "total"
                },
                {
                    "value": 0,
                    "formula": f"of:=SUM([.G2]:[.G{last_row_idx}])",
                    "type": "float",
                    "style": "total"
                }
            ]
        })
        
        config["sheets"].append(sheet)
        
    return config

if __name__ == "__main__":
    year = 2026
    config = generate_config(year)
    
    config_path = "/home/levins/Gemini-Workspace/Projects/Work-Hours-2026/.gemini/full_year_config_v3.json"
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"Generated config at {config_path}")
    
    output_path = "/home/levins/Gemini-Workspace/Projects/Work-Hours-2026/Work_Hours_2026_Clean.ods"
    script_path = "/home/levins/.gemini/skills/ods-manager/scripts/create_ods.py"
    
    subprocess.run(["python3", script_path, config_path, output_path])
