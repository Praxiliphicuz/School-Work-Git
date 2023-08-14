#So first off we have a new key word called class and class sort of acts like a function
#Then we provide a name of the class & then an indented block to continue the code
#so in the class here we just have x = 0, thats an attribute of all party animals will have a variable named x in them and theres a lttle functon. So this is now a method
class PartyAnimal:
    x = (0)

#this code is a part of the block of the code above, every class has some data associated with that class and some code associated with that class
    def party(self) :
        self.x = self.x + 1
        print("So far " ,self.x)

#The method above has a bit of code in it, but when this is done, it doesnt actually run any code, but what happens is we have a template called PartyAnimal.
# And The syntax here below    an = PartyAnimal()    is basically saying make me a PartyAnimal, its the same as saying x = list(), which says mint me a new list, there is a template for a new list here and then give that empty list back in the variable of x
# once thats empty or fresh PartyAnimal is done, then give it back to me in the variable an, and so this then is an OBJECT
an = PartyAnimal()

# So here we make a call by taking name of the object .  dot it the operator and then the method within it, its calls it 3 times
print("Type", type(an))
print("Dir", dir(an))   


#we can use more parameters in this class we made/ called, the second party animal has no parameters while the first has one parameters, which is (self)
#And what you basically can think of this as, is its kind've like saying, go into party animal, call the party function within that and then pass, an , as the first parameter variabel, which comes in as (self), most people name the variable salf.
# And what self says   self.x = self.x + 1     well thats kind've like saying      an..x = an.x + 1       because were calling it in the context of an
