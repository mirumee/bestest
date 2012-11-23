def clever_count(items):
    for row_number, line in enumerate(items):
        # (…)
        continue
    try:
        num_records = row_number + 1
    except UnboundLocalError:
        # in case of row_number as not been assign yet
        num_records = 0
    return num_records
