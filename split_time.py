from datetime import date

def split_period(start_date, end_date, chunk_days=365):
    """
    Découpe la période en intervalles d'un an maximum.
    La dernière période s'arrête exactement à end_date.
    """
    periods = []

    current_start = date.fromisoformat(start_date)
    final_end = date.fromisoformat(end_date)

    while current_start < final_end:
        try:
            # tentative : même jour + 1 an
            next_year = current_start.replace(year=current_start.year + 1)
        except ValueError:
            # cas 29 février
            next_year = current_start.replace(month=2, day=28, year=current_start.year + 1)

        current_end = min(next_year, final_end)
        periods.append((current_start.isoformat(), current_end.isoformat()))

        current_start = current_end

    return periods
