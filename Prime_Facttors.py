#ΥΠΟΕΡΓΑΣΙΑ 3 ΓΙΝΟΜΕΝΟ ΠΡΩΤΩΝ ΠΑΡΑΓΟΝΤΩΝ

print("Γινόμενο Πρώτων Παραγόντων")
                                                      
apothikevmenoi_arithmoi = [ ]
diairetis = 2            

while True:
    number = int(input("Δώστε το n (2-10000): "))
    if 2 <= number <= 10000:
        arxikos_arithmos = number                           # βάζουμε τον αριθμό (input) σε μεταβλητή για να τον καλέσουμε στην τελική εκτύπωση
        break
           
while number >=2 :
    if number % diairetis == 0:                               # Αν διαιρείται ακριβώς με τον τρέχοντα διαιρέτη
        apothikevmenoi_arithmoi.append(diairetis)  # Προσθέτουμε τον διαιρέτη στη λίστα (αποθηκευμένοι αριθμοί)
        number = number // diairetis                        # Διαιρούμε τον αριθμό με τον διαιρέτη
    else:
        diairetis = diairetis + 1  

print(f"{arxikos_arithmos} = {'  x  '.join(map(str, apothikevmenoi_arithmoi))}")
    

     
    
    
               
