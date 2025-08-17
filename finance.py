# This module contains an interest calculator
# Formula used for compound interest: A = P * (1 + r / n) ** (n * t)

def interest(prime_amount, time_duration_str, number_of_times_interest_will_compound_per_year, rate_of_interest) :
    """
    Calculates the compound interest.

    Args:
        prime_amount (float or int): The initial principal amount (P).
        time_duration_str (str): The duration for which the interest is calculated,
                                 **must be in specific short-hand formats**:
                                 - "XyYm" (e.g., "5y6m", "1y8m" for 1 year 8 months)
                                 - "Xm" (e.g., "15m", "6m" for 15 months, 6 months)
                                 - "Xy" (e.g., "5y", "1y" for 5 years, 1 year)
                                 Where X and Y are whole numbers.
        number_of_times_interest_will_compound_per_year (float or int):
            The number of times interest is compounded per year (n).
            (e.g., 2 for half-yearly, 4 for quarterly, 12 for monthly, 365 for daily).
        rate_of_interest (float or int): The annual nominal interest rate (as a percentage, e.g., 5 for 5%).

    Returns:
        float: The compound interest amount earned, rounded to 3 decimal places.
        None: If the input is not valid or any error occurs.
    """

    # Convert and validate numeric inputs (P, N, R)
    try:
        p = float(prime_amount)
        n = float(number_of_times_interest_will_compound_per_year)
        r = float(rate_of_interest)
    except ValueError:
        print('Error: Please enter valid numbers (integer or float) for Prime Amount, Compounding Frequency, and Rate of Interest.')
        return None
    except Exception as error:
        print(f'An unexpected error happened during initial input conversion: {error}')
        return None

    # Parse and validate 'time_duration_str' without 're' module
    total_time_in_years = 0.0
    # Normalize input string for consistent parsing
    time_str_normalized = str(time_duration_str).lower().strip()

    years = 0
    months = 0
    is_valid_format = False

    if 'y' in time_str_normalized and 'm' in time_str_normalized:
        # Potentially XyYm format
        y_index = time_str_normalized.find('y')
        m_index = time_str_normalized.find('m')

        if y_index != -1 and m_index != -1 and y_index < m_index:
            years_part = time_str_normalized[:y_index]
            months_part = time_str_normalized[y_index + 1 : m_index]

            if years_part.isdigit() and months_part.isdigit():
                years = int(years_part)
                months = int(months_part)
                total_time_in_years = years + (months / 12.0)
                is_valid_format = True
    
    if not is_valid_format: # If XyYm wasn't matched or was invalid, try other formats
        if time_str_normalized.endswith('m') and 'y' not in time_str_normalized:
            # Format: Xm
            months_part = time_str_normalized[:-1] # Remove 'm'
            if months_part.isdigit():
                months = int(months_part)
                total_time_in_years = months / 12.0
                is_valid_format = True
        elif time_str_normalized.endswith('y') and 'm' not in time_str_normalized:
            # Format: Xy
            years_part = time_str_normalized[:-1] # Remove 'y'
            if years_part.isdigit():
                years = int(years_part)
                total_time_in_years = float(years)
                is_valid_format = True
    
    if not is_valid_format:
        print(f"Error: Invalid time duration format: '{time_duration_str}'.")
        print("Please use formats like '5y6m', '15m', or '5y'.")
        return None
    
    # Final validation for parsed time
    if total_time_in_years <= 0:
        print('Error: Time duration must be a positive value.')
        return None

    # Validate other numeric data (after time parsing, before main logic)
    if p <= 0:
        print('Error: Prime amount should be greater than Zero.')
        return None
    if n <= 0:
        print('Error: The number of times the interest will compound per year should be greater than Zero.')
        return None
    if r <= 0:
        print('Error: Rate of Interest should be greater than Zero.')
        return None

    # Main calculation logic
    try :
        r_decimal = r / 100.0  # Change percentage to decimal (using 100.0 for float division)

        # Calculate the total amount after compounding with full precision
        total_amount_precise = p * (1 + r_decimal / n) ** (n * total_time_in_years)

        # Calculate the compound interest with full precision
        compound_interest_precise = total_amount_precise - p

        # Round the final interest amount to 3 decimal places before returning
        result = round(compound_interest_precise, 3)

        return result

    except Exception as error :
        print(f'An unexpected error happened during calculation: {error}')
        return None
