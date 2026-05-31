# Handle division by zero error
if city_count == 0:
    print("No cities with available weather data.")
else:
    average_temp = total_temp / city_count
    print(f"\nAverage temperature in European capital cities: {average_temp:.2f}°C")