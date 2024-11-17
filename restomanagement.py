menu={
    "Pizza":70,
    "Burger":50,
    "Pasta":40,
    "Macaroni":60,
    "Tea":5,
    "Coffee":15,
    "Fluids":60

}

print("Welcome To BTech restro+cafe\n The menu is\n Pizza 70\n Burger 50\n Pasta 40\n Macaroni 60\n Tea 5\n Coffee 15\n Fluids 60\n ")
total_amount=0
while True:
    order=input("Enter your order please ")
    quantity=int(input("enter quantity please "))
    if order in menu:
        total_amount=total_amount+(menu[order]*quantity)
    ch=input("Anything else you want to add Y for Yes and N for no ")
    if ch in "Nn":
        break
print("Your bill is",total_amount)

