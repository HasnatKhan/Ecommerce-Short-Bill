toffee = int(input("Enter the number of Toffees : "));
c_bar = int(input("Enter the number of Chocolate Bars : "));
c_gum = int(input("Enter the number of Chewing Gum : "));
hash = "-"*35
print("Bill");
print('{:<15s}{:>4s}{:>10s}'.format("Item","Quantity","Cost"));
if (toffee > 0):
    print('{:<15s}{:>4s}{:>13s}'.format("Tofees",str(toffee),str(toffee*7)));
if (c_bar > 0):
    print('{:<15s}{:>4s}{:>13s}'.format("Chocolate Bars",str(c_bar),str(c_bar*30)));
if (c_gum > 0):
    print('{:<15s}{:>4s}{:>13s}'.format("Chewing Gum",str(c_gum),str(c_gum*12)));
print(hash)
print('{:<28s}{:>4s}'.format("Total",str((toffee*7)+(c_bar*30)+(c_gum*12))));
