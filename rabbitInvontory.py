import os
import numpy as np
import Tkinter as tk
import functools
import datetime

try:
    directory = np.load('C:/Users/thomq/Documents/Rabbit-essential/Directory.npy')
except IOError:
    print "run setup"


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def _add_bun(name, breed, mass, age, dateIn, gender, fixed, litter, problemList, housing, adopted, bio, dateOut = " ", Id = 0):
    # Create any missing information in system
    year = dateIn[len(dateIn) - 4:len(dateIn)]
    print name
    global directory

    if Id == 0:
        try:
            numInYear = np.load('C:/Users/thomq/Desktop/Rabbit-invontory/Essential/' + ('Number_in_' + str(year)) + '.npy')
        except IOError:
            numInYear = [0, 0]
            np.save('C:/Users/thomq/Desktop/Rabbit-invontory/Essential/' + ('Number_in_' + str(year)), numInYear)
        year = str(year)
        print adopted
        if not os.path.isdir('C:/Users/thomq/Desktop/Rabbit-invontory/Rabbit/' + year):
            os.makedirs('C:/Users/thomq/Desktop/Rabbit-invontory/Rabbit/' + year)

        # Create bun's folder and sub-folders
        if gender == 'Male':
            numInYear[1] += 1
            number = str(numInYear[1])
            gLetter = 'M'
        else:
            numInYear[0] += 1
            number = str(numInYear[0])
            gLetter = 'F'

        folderName = '/' + name + '-' + str(year) + '-' + gLetter + str(number)
    else:
        folderName = '/' + name + '-' + str(Id)

    if not os.path.isdir('C:/Users/thomq/Desktop/Rabbit-invontory/Rabbits/' + str(year) + folderName + '/Information'):
        os.makedirs('C:/Users/thomq/Desktop/Rabbit-invontory/Rabbits/' + str(year) + folderName)
        os.makedirs('C:/Users/thomq/Desktop/Rabbit-invontory/Rabbits/' + str(year) + folderName + '/Information')
        os.makedirs('C:/Users/thomq/Desktop/Rabbit-invontory/Rabbits/' + str(year) + folderName + '/Pictures')
        os.makedirs('C:/Users/thomq/Desktop/Rabbit-invontory/Rabbits/' + str(year) + folderName + '/Pictures\BioPic')

    # Create bun's info page
    div = os.path.join('C:/Users/thomq/Desktop/Rabbit-invontory', str(year))
    div = os.path.join(div, folderName)
    div = os.path.join(div, 'Information')
    dirName = os.path.join(div, 'Info_page.txt')
    file = open('C:/Users/thomq/Desktop/Rabbit-invontory/Rabbits/' + str(year) + folderName + '/Information/Info_page.txt', 'w')

    file.write('Name: ' + str(name) + '\n')
    if Id == 0:
        file.write('ID Number:' + year + '-' + gLetter + number + '\n\n')
    else:
        file.write(str('ID Number:' + str(str(year) + ':' + str(Id) + "\n\n")))
    file.write('Breed: ' + str(breed) + '\n\n')
    file.write('Weight: ' + str(mass) + '\n\n')
    file.write('Age: ' + str(age) + '\n\n')
    file.write("Date of  Arrival: " + str(dateIn) + "\n")
    file.write("Date of Departure: " + dateOut + "\n\n")
    file.write("Gender: " + gender + "\n")
    file.write("Fixed: " + fixed + "\n\n")
    file.write('Letter box trained: ' + litter + '\n\n')
    file.write("Problem(s): " + problemList + "\n\n")
    file.write("Adoptable: " + adopted + "\n\n")
    file.write("Housing: " + housing + '\n\n')
    file.write("Bio: " + str(bio))
    file.close()


def _pull_bun_data(name):
    year = name[len(name) - 4:len(name)]
    completeName = os.path.join(directory + year + name + "\Information", 'Info_Page.txt')
    file = open(completeName, 'r')
    count = 0
    lines = []
    for line in file:
        lines[count] = line
        count += 1
    name = lines[0]
    name = name[6:len(name)]
    Id = lines[1]
    Id = Id[len("Name: "):len(Id)]
    breed = lines[4]
    breed = breed[len("Breed: "):len(breed)]
    wieght = lines[6]
    wieght = wieght[len("Wieght: "):len(wieght)]
    age = lines[7]
    age = age[len("Age: "):len(age)]
    dayOfAvrival = lines[8]
    dayOfAvrival = dayOfAvrival[len("Day of arrival: "):len(dayOfAvrival)]
    dayOfDeparture = lines[9]
    dayOfDeparture = dayOfDeparture[len("Day of departure: "): len(dayOfDeparture)]
    gender = lines[11]
    gender = gender[len("Gender: "): len(gender)]
    fixed = lines[12]
    fixed = fixed[len("Fixed: "): len(fixed)]
    litter = lines[14]
    litter = litter[len("Letter box trained: "):len(litter)]
    problem = lines[16]
    problem = problem[len("Problem(s): "):len(problem)]
    adpotable = lines[18]
    adpotable = adpotable[len("Adoptable: "):len(adpotable)]
    housing = lines[20]
    housing = housing[len("Housing: "):len(housing)]
    bio = lines[22]
    bio = bio[len('Bio: '):len(bio)]

    os.remove(completeName)
    return name, Id, breed, wieght, age, dayOfAvrival, dayOfDeparture, gender, fixed, litter, problem, adpotable, housing, bio

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def _show(self):
        self.lift()


class _add_page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Name
        tk.Label(self, text="Name").pack(side='top', fill='both', expand=True)
        name = tk.Entry(self)
        name.pack(side='top')

        # breed
        tk.Label(self, text='Breed of the rabbit').pack(side='top', fill='both',
                                                        expand=True)
        breed = tk.StringVar()
        breedOptions = tk.OptionMenu(self, breed, 'American', 'American Chinchilla',
                                     'American Fuzzy Lop', 'American Sable',
                                     'Argente Brun', 'Belgian Hare', 'Beveren',
                                     'Blanc de Hotot', 'Britannia Petite',
                                     'Californian', "Champagne D'Argent",
                                     'Checkered Giant', 'Cinnamon', "Creme D'Argent",
                                     'Dutch', 'Dwarf Hotot', 'English Angora',
                                     'English Lop', 'English Spot', 'Flemish Giant',
                                     'Florida White', 'French Angora', 'French Lop',
                                     'Giant Angora', 'Giant Chinchilla', 'Harlenquin',
                                     'Havana', 'Himalayan', 'Holland Lop',
                                     'Jersey Wooly', 'Lilac', 'Lionhead', 'Mini Loop',
                                     'Mini Rex', 'Mini Satin', 'Netherland Dwarf',
                                     'New Zealand', 'Palomino', 'Polish', 'Rex',
                                     'Rhinelander', 'Satin', 'Satin Angora', 'Silver',
                                     'Silver Fox', 'Silver Marten',
                                     'Standard Chinchilla', 'Tan', 'Thrianta')
        breedOptions.pack(side='top')

        # weight
        tk.Label(self, text="Weight of Rabbit(lbs)").pack(side='top')
        mass = tk.Entry(self, width=7)
        mass.pack(side='top')

        # age
        tk.Label(self, text='Age of Bun:').pack(side='top', fill='both', expand=True)
        age = tk.Entry(self, width=2)
        age.pack(side="top")

        # Date of Arrival
        tk.Label(self, text="Date of Arrival", width=2).pack(side='top',
                                                             fill='both',
                                                             expand=True)
        dayOFArrivalEntery = tk.Entry(self, width=10)
        day = str(datetime.date.today())
        day = day[5:7] + '/' + day[8:10] + "/" + day[0:4]
        dayOFArrivalEntery.insert(0, day)
        dayOFArrivalEntery.pack(side='top')

        # Gender
        gender = tk.StringVar()
        gender.set("Female")
        tk.Label(self, text='Gender:').pack(side='top')
        tk.OptionMenu(self, gender, 'Male', 'Female').pack(side='top')

        # Fixed
        fixed = tk.StringVar()
        fixed.set('No')
        tk.Checkbutton(self, text='Fixed', variable=fixed, onvalue='Yes',
                       offvalue="No").pack(side='top', fill='both', expand=True)

        # Litter box trained
        litterTrained = tk.StringVar()
        litterTrained.set('No')
        tk.Checkbutton(self, text='Litter box trained', variable=litterTrained,
                       onvalue='Yes', offvalue='No').pack(side='top',
                                                          fill='both', expand=True)

        # Other probelms
        tk.Label(self, text='Other problem(s)').pack(side='top', fill='both',
                                                     expand=True)
        problemEntry = tk.Entry(self)
        problemEntry.insert(0, 'List problem(s)')
        problemEntry.pack(side='top', fill='both', expand=True)

        # Housing location
        tk.Label(self, text="Where is the bun staying").pack(side='top', fill='both', expand=True)
        housingEntry = tk.Entry(self)
        housingEntry.pack(side='top', fill='both', expand=True)

        # Ready to be adopted
        adoptable = tk.StringVar()
        tk.Checkbutton(self, text='Adoptable', variable=adoptable, onvalue='Yes', offvalue='No').pack(side='top',
                                                                                                      fill='both',
                                                                                                      expand=True)

        #Bio
        tk.Label(self, text="Bio for Bun:").pack(side='top', fill='both', expand=True)
        Bio = tk.Text(self, height=10)
        Bio.pack(side='top', fill='both', expand=True)

        # Buttons
        b1 = tk.Button(self, text='Add Bun', command=functools.partial(_add_bun, name.get(), breed.get(), mass.get(),
                                                                       age.get(), dayOFArrivalEntery.get(),
                                                                       gender.get(), fixed.get(), litterTrained.get(),
                                                                       problemEntry.get(), housingEntry.get(),
                                                                       adoptable.get(), Bio.get(1.0, tk.END)))
        b2 = tk.Button(self, text='Cancel', command=root.update())

        b1.pack(side='top', fill='both', expand=True)
        b2.pack(side='top', fill='both', expand=True)




class _find_bun(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        tk.Label(self, text="Name of bun").grid(row=0)
        name = tk.Entry(self)
        name.grid(row=0, column=1)
        tk.Button(self, text='Find', command=functools.partial(_pull_bun_data, name.get())).grid(row=1, column=0,
                                                                                                 sticky=tk.W, pady=4)
        tk.Button(self, text='Cancel', command=_main_page).grid(row=2, column=1, sticky=tk.W, pady=4)


class _display_data(Page):
    def __init__(self, bun):
        name, Id, breed, mass, age, dateIn, dateOut, gender, fixed, litter, problemList, housing, adopted, bio = _pull_bun_data(bun)
        # Display info/ edit

        # Name
        tk.Label(self, text='Name:').pack(side="top")
        bunName = tk.Entry(self)
        bunName.insert(0, name)
        bunName.pack(side="top")

        # Id
        tk.Label(self, text='ID: ' + str(Id)).pack(side='top')

        # Breed
        bunBreed = tk.Entry(self)
        bunBreed.insert(0, breed)
        bunBreed.pack(side='top')

        # Weight
        tk.Label(self, text="Weight").pack(side='top')
        bunWeight = tk.Entry(self)
        bunWeight.insert(0, mass)
        bunWeight.pack(side='top')

        #age
        # Weight
        tk.Label(self, text="Age").pack(side='top')
        bunAge = tk.Entry(self)
        bunAge.insert(0, age)
        bunAge.pack(side='top')

        # Date in
        tk.Label(self, text="Date of Arrival:").pack(side='top')
        dateArrival = tk.Entry(self)
        dateArrival.insert(0, dateIn)
        dateArrival.pack(side="top")

        # Date Out
        tk.Label(self, text='Date of Departure').pack(side='top')
        dateDeparture = tk.Entry(self)
        dateDeparture.insert(0, dateOut)
        dateDeparture.pack(side='top')

        # Gender
        tk.Label(self, text='Gender:').pack(side='top')
        gender1 = tk.Entry(self)
        gender1.insert(0, gender)
        gender1.pack(side='top')

        # Fixed
        isFixed = tk.StringVar()
        isFixed.set(fixed)
        tk.Checkbutton(self, text='Fixed', variable=isFixed, onvalue='Yes', offvalue='No').pack(side='top')

        # litter
        litterTrained = tk.StringVar()
        litterTrained.set(litter)
        tk.Checkbutton(self, text='Litter box trained', variable=litterTrained, onvalue='Yes', offvalue='No')

        # problem(s)
        tk.Label(self, text='Probelm(s):').pack(side='top')
        problems = tk.Entry(self)
        problems.insert(0, problemList)
        problems.pack(side="top")

        # housing
        tk.Label(self, text='Housing:').pack(side='top')
        location = tk.Entry(self)
        location.insert(0, housing)
        location.pack(side='top')

        # adoptable
        canBeAdopted = tk.StringVar()
        canBeAdopted.set(adopted)
        tk.Checkbutton(self, text='Adoptable', variable=canBeAdopted, onvalue='Yes', offvalue='No')

        # bio
        tk.Label(self, text='Bio')
        bioBox = tk.Text(self, height=20)
        bioBox.insert(0, bio)
        bioBox.pack(side='top')

        # button
        tk.Button(self, text='Update', command=functools.partial(_add_bun, bunName.get(), bunBreed, bunWeight, bunAge,
                                                                 dateArrival.get(), gender.get(), isFixed, litterTrained,
                                                                 problems.get(), location.get(), canBeAdopted,
                                                                 dateDeparture.get(), Id)).pack('top')
        tk.Button(self, text='Cancel', command=_main_page).pack('top')


class _main_page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = _add_page(self)
        #p2 = _find_bun(self)
        #p3 = _display_data(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill='x', expand=False)
        container.pack(side='top', fill='both', expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        #p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Add Bun", command=p1.lift)
        #b2 = tk.Button(buttonframe, text="Edit Bun", command=p3.lift)

        b1.pack(side='left')
        #b2.pack(side='left')


if __name__ == "__main__":
    root = tk.Tk()
    main = _main_page(root)
    main.pack(side='top', fill='both', expand=True)
    root.wm_geometry("400x800")
    main.mainloop()
