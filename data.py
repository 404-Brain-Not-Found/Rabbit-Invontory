import os
import numpy as np
import fileinput
import datetime
import functools


class Data(object):
    def _add_bun(self, name, breed, mass, age, dateIn, gender, fixed, litter, problemList, housing, adopted, bio, dateOut = " ", Id = 0):
        # Create any missing information in system
        year = dateIn[len(dateIn) - 4:len(dateIn)]
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

    def _pull_bun_data(self, name):
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
