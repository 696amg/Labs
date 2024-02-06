Hata = {"1 brat", "2 brat", "3 brat"}
if "2 brat" in Hata:
    print("YES")


Hata2 = {"1 brat", "2 brat"}
Hata2.add("Me")
print(Hata2)


fruits = {"banana", "pineapple"}
any_fruits = {"orange", "nectarine"}
fruits.update(any_fruits)
print(fruits)

 
berrys = {"blackberry", "cherry"}
berrys.remove("cherry")
print(berrys)


vege = {"carrot", "onion", "tomato"}
vege.discard("carrot")
print(vege)  