from adpkg.triangle import areaoftriangle

if __name__ == '__main__':
    print("--- Triangle Area Calculator ---")
    
    while True:
        try:
            side_a = input("Enter the length of side a: ")
            side_b = input("Enter the length of side b: ")
            side_c = input("Enter the length of side c: ")
            
            area = areaoftriangle(side_a, side_b, side_c)
            
            if area is not None:
                print(f"The calculated area of the triangle is: {area}")
            
        except Exception as e:
            print(f"An error occurred during input: {e}")
            
        check_again = input("\nDo you want to calculate another area? (yes/no): ").lower()
        if check_again != 'yes':
            break

    print("Exiting calculator. Goodbye!")