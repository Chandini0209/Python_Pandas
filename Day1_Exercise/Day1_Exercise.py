# Question
# Sandeep wants to travel throughout India on his bicycle to raise awareness of "Hazards of Plastics". His entire route covers 10,000 kms. 
# How many years, months, days and hours will it take sandeep to complete this great inspiring tour of India.


# Answer

def finding_time():
    total_distance = 10_000

    # Assumptions
    avg_hours_travel_per_day = 7  # hours
    avg_time_for_one_km = 4  # minutes
    avg_km_travel_per_hour = 15  # kms
    ride_days_before_rest = 6  # days

    # Calculation
    total_hours_needed = round(total_distance / avg_km_travel_per_hour,2)
    ride_days_needed = round(total_hours_needed / avg_hours_travel_per_day,2)
    rest_days_needed = round(ride_days_needed / ride_days_before_rest,2)
    total_days_needed = ride_days_needed + rest_days_needed
    total_months_needed = round(total_days_needed / 30,2)
    total_years_needed = round(total_months_needed / 12,2)
    
    print(f"Total Years Needed: {total_years_needed} years")
    print(f"Total Months Needed: {total_months_needed} months")
    print(f"Total Days Needed: {total_days_needed} days")
    print(f"Total Hours Needed: {total_hours_needed} hours")
    
finding_time()
