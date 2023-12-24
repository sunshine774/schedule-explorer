from datetime import datetime, timedelta

def generate_dates(start_date, end_date):
    current_date = start_date
    dates = []
    while current_date <= end_date:
        dates.append(current_date.strftime("%d/%m"))
        current_date += timedelta(days=1)
    return dates

def print_term_dates(term_start, term_end):
    term_start_date = datetime.strptime(term_start, "%d/%m")
    term_end_date = datetime.strptime(term_end, "%d/%m")

    current_week_start = term_start_date
    week_number = 1

    while current_week_start <= term_end_date:
        current_week_end = current_week_start + timedelta(days=6)
        print(f"Week {week_number}: {current_week_start.strftime('%d/%m')} - {current_week_end.strftime('%d/%m')}")
        
        current_week_start += timedelta(days=7)
        week_number += 1

# Define term dates
term_1_start = "27/01"
term_1_end = "06/04"
term_2_start = "24/04"
term_2_end = "30/06"
term_3_start = "17/07"
term_3_end = "22/09"
term_4_start = "09/10"
term_4_end = "19/12"

# Print dates for each term
print("Term 1:")
print_term_dates(term_1_start, term_1_end)

print("\nTerm 2:")
print_term_dates(term_2_start, term_2_end)

print("\nTerm 3:")
print_term_dates(term_3_start, term_3_end)

print("\nTerm 4:")
print_term_dates(term_4_start, term_4_end)
