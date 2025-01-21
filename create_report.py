from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
import math

import pandas

def get_day_start(date):
  return datetime(
    year=date.year,
    month=date.month,
    day=date.day,
    hour=0,
    minute=0,
    second=0,
  )

def get_day_end(date):
  return datetime(
    year=date.year,
    month=date.month,
    day=date.day,
    hour=23,
    minute=59,
    second=59,
    microsecond=999,
  )

def get_args():
  arg_parser = ArgumentParser(
    prog="Report maker",
    description="Creates reports for specified day based on jira excel output",
  )

  arg_parser.add_argument("-d", "--date")
  arg_parser.add_argument("-f", "--filename")
  return arg_parser.parse_args()

def format_hours(hours):
  whole_hours = math.floor(hours)
  whole_minutes = round((hours - whole_hours) * 60)

  if not whole_hours:
    return f"{whole_minutes}m"

  if not whole_minutes:
    return f"{whole_hours}m"
  
  return f"{whole_hours}h {whole_minutes}m"

if __name__ == "__main__":
  args = get_args()

  filename = args.filename
  date = datetime.strptime(args.date) if args.date else datetime.today()

  data = pandas.read_excel(filename, parse_dates=["Дата работы"]).rename(
    columns={
      "Статус задачи": "status",
      "Часов": "hours",
      "Ключ задачи": "key",
      "Дата работы": "date",
      "Имя активности": "activity",
      "Описание работы": "description",
    }
  )
  report_data = data[data["date"] > get_day_start(date)][data["date"] < get_day_end(date)]

  outdir = Path("output")

  with open(outdir/date.strftime("%Y-%m-%d.txt"), "x", encoding="utf8") as report_file:
    report_file.writelines(
      f"{item.date.strftime("%H:%M")} {format_hours(item.hours)} {item.key} {item.description}\n" for item in report_data.itertuples()
    )