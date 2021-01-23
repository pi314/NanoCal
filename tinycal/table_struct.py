from datetime import timedelta, date
from collections import namedtuple


class Weekday:
    def __init__(self, weekday):
        self.weekday = weekday

    def __int__(self):
        return self.weekday

    def __str__(self):
        return str(self.weekday)

    def __repr__(self):
        return 'Weekday({})'.format(self.weekday)


class Date(date):
    def __new__(cls, *args, **kwargs):
        # Source: https://stackoverflow.com/a/45981230/3812388
        # because __new__ creates the instance you need to pass the arguments
        # to the superclass here and **not** in the __init__
        if len(args) == 1 and isinstance(args[0], date):
            d = args[0]
            return super().__new__(cls, year=d.year, month=d.month, day=d.day)

        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, is_fill=False, **kwargs):
        self.is_fill = is_fill


class TinyCalTable:
    def __init__(self):
        self.rows = []


class TinyCalCellRow:
    def __init__(self):
        self.cells = []


class TinyCalCell:
    def __init__(self, title):
        self.title = title
        self.weeks = []


class TinyCalWeek:
    def __init__(self, wk):
        self.wk = wk
        self.days = []
        self.hint = ''

    def append(self, node):
        self.days.append(node)


def cal_week_num(cal, date):
    return ((date - cal.monthdatescalendar(date.year, 1)[0][0]).days // 7) + 1


def construct_table(conf, tr, cal, drange, today):
    ''' Construct output table structure:
    table: [
        row: [
            cell: [
                title: str
                cal_week: [
                    wk: int
                    day:date x 7
                ], ...
            ], ...
        ], ...
    ]
    '''

    cal_table = TinyCalTable()

    if conf.mode == 'month':
        for idx, umn in enumerate(range(drange[0].umn, drange[1].umn + 1)):
            if idx % conf.col == 0:
                cal_row = TinyCalCellRow()
                cal_table.rows.append(cal_row)

            year = umn // 12
            month = (umn % 12) + 1

            cal_cell = TinyCalCell(tr.month_year_format.format(year=year, month=tr.month(month)))

            # Put Weekday header
            cal_week = TinyCalWeek(wk=tr.weekday[-1])
            for wkd in cal.iterweekdays():
                cal_week.append(Weekday(wkd))

            cal_cell.weeks.append(cal_week)

            # Put dates
            for week in cal.monthdatescalendar(year, month):
                if (week[0].year, week[0].month) != (year, month) and date(year, 1, 1) in week:
                    wk = 1
                else:
                    wk = cal_week_num(cal, week[0])

                cal_week = TinyCalWeek(wk=wk)
                for day in week:
                    day = Date(day)
                    day.is_fill = (day.month != month)
                    cal_week.append(day)

                cal_cell.weeks.append(cal_week)

            cal_row.cells.append(cal_cell)

        # Fill the remaining cell
        if len(cal_table.rows) > 1:
            for i in range(len(cal_row.cells), conf.col):
                cal_row.cells.append(None)

    else:
        cal_row = TinyCalCellRow()
        cal_table.rows.append(cal_row)

        if drange[0].umn == drange[1].umn:
            cal_cell = TinyCalCell(tr.month_year_format.format(year=drange[0].year, month=tr.month(drange[0].month)))
        else:
            cal_cell = TinyCalCell('{sy:04}/{sm:02} ~ {ey:04}/{em:02}'.format(
                sy=drange[0].to_date().year,
                sm=drange[0].to_date().month,
                ey=drange[1].to_date().year,
                em=drange[1].to_date().month,
                ))
        cal_row.cells.append(cal_cell)

        # Put Weekday header
        cal_week = TinyCalWeek(wk=tr.weekday[-1])
        for wkd in cal.iterweekdays():
            cal_week.append(Weekday(wkd))

        cal_cell.weeks.append(cal_week)

        dcursor = drange[0].copy().move_to_week_begin().to_date()

        while dcursor <= drange[1].to_date():
            week = [Date(dcursor + timedelta(days=i)) for i in range(7)]

            if dcursor.year != today.year and today in week:
                wk = 1
            else:
                wk = cal_week_num(cal, dcursor)

            cal_week = TinyCalWeek(wk=wk)

            if (week[-1].day <= 7) or len(cal_cell.weeks) == 1:
                cal_week.hint = tr.month(week[-1].month, abbr=True)

            for day in week:
                day.is_fill = (day.year * 12 + day.month - 1) not in range(drange[0].umn, drange[1].umn + 1)
                cal_week.append(day)

            cal_cell.weeks.append(cal_week)

            dcursor += timedelta(days=7)

    return cal_table
