print("Lesson 4")

class Human:
    def __init__(self, Name):
        self.Name= Name

class Auto:
    def __init__(self,brand):
        self.Brand= brand
        self.Humans= []
    def AddHuman(self, Human):
        self.Humans.append(Human)
    def PrintHumans(self):
        if self.Humans != []:
            print("Names humans:")
            for Human in self.Humans:
                print("\t",Human.Name)
        else:
            print("This auto is empty")

human1= Human("Victo Pavlik")
human2= Human("Yarosh Bohdan")

autoBohdan=Auto("Bohdan")

print("Brand of auto:", autoBohdan.Brand)

autoBohdan.AddHuman(human1)
autoBohdan.AddHuman(human2)

autoBohdan.AddHuman(Human("Samchuk Maxim"))

autoBohdan.PrintHumans()


