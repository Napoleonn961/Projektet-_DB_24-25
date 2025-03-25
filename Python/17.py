
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib


def sum_list(numbers):
    return sum(numbers)


def average_list(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


def sort_numbers(numbers):
    return sorted(numbers)


def validate_input(prompt, type_func=int):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Hyrje e pavlefshme, ju lutem provoni përsëri.")


def main_menu():
    print("\nMath Helper - Mjet për Llogaritjet Matematikore dhe Manipulimin e të Dhënave")
    print("Zgjidhni një opsion:")
    print("1. Llogarit Faktorialin")
    print("2. Gjenero Serinë Fibonacci")
    print("3. Llogarit Shumën e Listës")
    print("4. Llogarit Mesataren e Listës")
    print("5. Rendit Listën në Rritje")
    print("6. Dil nga Programi")
    
    choice = validate_input("Ju lutem zgjidhni opsionin: ", int)
    
    if choice == 1:
        n = validate_input("Shkruani një numër për faktorialin: ")
        print(f"Faktoriali i {n} është {factorial(n)}")
    elif choice == 2:
        n = validate_input("Shkruani numrin e terma të serisë Fibonacci: ")
        print(f"Seria Fibonacci deri në {n}-term është: {fibonacci(n)}")
    elif choice == 3:
        numbers = list(map(int, input("Shkruani numrat për listën (ndajini me hapësirë): ").split()))
        print(f"Shuma e listës është: {sum_list(numbers)}")
    elif choice == 4:
        numbers = list(map(int, input("Shkruani numrat për listën (ndajini me hapësirë): ").split()))
        print(f"Mesatarja e listës është: {average_list(numbers)}")
    elif choice == 5:
        numbers = list(map(int, input("Shkruani numrat për listën (ndajini me hapësirë): ").split()))
        print(f"Lista e renditur: {sort_numbers(numbers)}")
    elif choice == 6:
        print("Faleminderit që përdorët Math Helper! Mirupafshim!")
        return
    else:
        print("Opsion i pavlefshëm, ju lutem provoni përsëri.")
    
 
    main_menu()


if __name__ == "__main__":
    main_menu()
