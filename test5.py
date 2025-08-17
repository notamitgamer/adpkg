from adpkg.finance import interest

if __name__ == '__main__':
    print("--- Compound Interest Calculator ---")
    
    while True:
        try:
            print("\nPlease provide the following details:")
            prime_amount = input("Principal Amount (P): ")
            rate_of_interest = input("Annual Interest Rate (%): ")
            compounding_frequency = input("Times per year interest is compounded (n): ")
            time_duration_str = input("Time Duration (e.g., '5y6m', '18m', '3y'): ")
            
            calculated_interest = interest(prime_amount, time_duration_str, compounding_frequency, rate_of_interest)
            
            if calculated_interest is not None:
                print(f"\nCompound Interest earned is: {calculated_interest}")
            else:
                print("\nCalculation failed due to invalid input.")

        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            
        check_again = input("\nDo you want to calculate another interest amount? (yes/no): ").lower()
        if check_again != 'yes':
            break

    print("Exiting calculator. Goodbye!")