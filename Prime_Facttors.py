# Prime Factorization
print("Prime Factorization")
                                                      
stored_numbers = [ ]
diairetis = 2            

while True:
    number = int(input("Δώστε το n (2-10000): "))
    if 2 <= number <= 10000:
        arxikos_arithmos = number                            # We store the number (input) in a variable so that we can call it in the final output.
           
while number >=2 :
    if number % diairetis == 0:                              # If it is divisible exactly by the current divisor.
       stored_numbers.append(diairetis)            # We add the divisor to the list (stored numbers)
        number = number // diairetis                         # We divide the number by the divisor
    else:
        diairetis = diairetis + 1  

print(f"{arxikos_arithmos} = {'  x  '.join(map(str, stored_numbers))}")
    

     
    
    
               
