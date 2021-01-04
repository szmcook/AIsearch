############
############ ALTHOUGH I GIVE YOU THE 'BARE BONES' OF THIS PROGRAM WITH THE NAME
############ 'skeleton.py', YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR
############ THE PURPOSES OF THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT
############ THIS PROGRAM IS STILL CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES!
############

import os
import sys
import time
import random

############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for _ in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for _ in range(j):
                row.append(0)
            for _ in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for _ in range(j + 1):
                row.append(0)
            for _ in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############

input_file = "AISearchfile012.txt"

############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

the_particular_city_file_folder = "city-files"
    
if os.path.isfile("../" + the_particular_city_file_folder + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string("../" + the_particular_city_file_folder + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the folder '" + the_particular_city_file_folder + "'.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############

############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME, E.G., 'abcd12'.
############

code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs("../alg_codes_and_tariffs.txt")

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR USER-NAME, E.G., "abcd12"
############

my_user_name = "gsgw38"

############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############

my_first_name = "Sam"
my_last_name = "Cook"

############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############

algorithm_code = "PS"

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the agorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER.
############

added_note = ""

############
############ NOW YOUR CODE SHOULD BEGIN.
############

    
# SETTING PARAMETERS
swarmSize = 20
theta = 0.6
alpha = 0.75
beta = 2.5

# IMPORTS
import random
# random.seed(1)
from copy import copy
from datetime import datetime, timedelta

# HELPER FUNCTIONS

def tourLength(tour):
    '''finds the length of a tour'''
    tour_length = 0
    for i in range(0, num_cities - 1):
        tour_length = tour_length + dist_matrix[tour[i]][tour[i + 1]]
    tour_length = tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
    return tour_length


def newTour(num_cities):
    '''creates a random canonical tour of length num_cities'''
    tour = []
    for i in range(1, num_cities):
        tour.append(i)
    random.shuffle(tour)
    tour.insert(0,0)
    if tour[1] > tour[-1]:
        tour[1], tour[-1] = tour[-1], tour[1]
    return tour


def randomVelocity():
    '''produces a random sequence of at most num_cities swaps'''
    numberOfSwaps = random.randint(0, num_cities)
    swaps = []
    for _ in range(numberOfSwaps):
        index = random.randint(1, num_cities-2)
        swaps.append((index, index+1 ))
    return swaps


def applyVelocity(tour, velocity):
    '''applies a series of swaps to a tour'''
    newTour = copy(tour)
    for pair in velocity:
        newTour[pair[0]], newTour[pair[1]] = newTour[pair[1]], newTour[pair[0]]
    # FIXME should this then put the tour back into canonical form? doesn't seem necessary but might be required if it don't work
    return newTour


def scalarMultiplyVelocity(scalar, velocity):
    '''multiply the velocity by a scalar'''
    new_velocity = []
    for _ in range(int(scalar)):
        new_velocity = new_velocity + velocity
    
    fractionalPart = scalar - int(scalar)
    if fractionalPart != 0:
        index = int(fractionalPart * len(velocity))
        new_velocity = new_velocity + velocity[:index]
    
    return new_velocity


def epsilonRemove(epsilon, velocity):
    '''removes a random swap from the velocity'''
    # we use epsilon to point the vector in the proximity of the (best - current) and we need a discrete equivalent.
    # the easiest is to randomly generate an epsilon between 0 and 1 and multiply it with alpha - in this case the probability should be distributed so it's normally near 1
    # this is a good choice for experimentation.
    if epsilon < 0.3 and len(velocity) > 1:
        index = random.randint(0, len(velocity)-1)
        return velocity[:index] + velocity[index+1:]
    else:
        return velocity
    

def subtractTours(tourA, tourB):
    '''uses bubble sort to obtain the velocity to go from tour1 to tour2'''
    swaps = []
    A = copy(tourA)
    for i in range(num_cities-1):
        for j in range(0, num_cities - i - 1):
            if tourB.index(A[j]) > tourB.index(A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                swaps.append((j,j+1))
    return swaps


# global toursToPlot
# toursToPlot = []
# global velocitiesToPlot
# velocitiesToPlot = []

def PSO(swarmSize, theta = 1, alpha = 1, beta = 1):
    swarm = []      # current state of each tour, swarm[i] is the ith tour
    pHat = []       # tuples of the best length and the respective state for each tour
    velocities = [] # array of the current velocities, represented as arrays of tuples (swaps)
    for _ in range(swarmSize):
        new_tour = newTour(num_cities)
        swarm.append(copy(new_tour))
        pHat.append( (tourLength(new_tour), copy(new_tour)) )
        velocities.append(randomVelocity())
    
    bestTour = min(pHat, key = lambda x: x[0])

    t = 0    
    start = datetime.now()
    while True:
        for a in range(swarmSize):
            # UPDATE NEIGHBOURHOOD TODO assess whether this is a spot where we can improve the quality of the tours
            neighbourHoodBest = bestTour

            # UPDATE TOUR
            oldSwarmAPosition = copy(swarm[a])
            swarm[a] = applyVelocity(oldSwarmAPosition, velocities[a])
            velocities[a] = subtractTours(swarm[a], oldSwarmAPosition)
            
            # UPDATE pHat IF NECESSARY
            currentLength = tourLength(swarm[a])
            if currentLength < pHat[a][0]:
                pHat[a] = copy((currentLength, swarm[a]))

            # UPDATE BEST TOUR
            if pHat[a][0] < bestTour[0]:
                bestTour = copy(pHat[a])
                
            # TERMINATION CONDITION
            if (datetime.now() - start > timedelta(seconds=50)):
                # import matplotlib.pyplot as plt
                # plt.plot(toursToPlot)
                # plt.savefig(f'basicTours_{num_cities}_{datetime.now().hour}:{datetime.now().minute}')
                # plt.plot(velocitiesToPlot)
                # plt.savefig(f'basicVels{num_cities}_{datetime.now().hour}:{datetime.now().minute}')
                return bestTour[1]
                
            # UPDATE VELOCITY this is the slow bit
            thetaVelocity = scalarMultiplyVelocity(theta, velocities[a])
            
            epsilon1 = random.random()
            differenceToBest = subtractTours(pHat[a][1], swarm[a])
            differenceToBestWithEpsilon = epsilonRemove(epsilon1, differenceToBest)
            alphaVelocity = scalarMultiplyVelocity(alpha, differenceToBestWithEpsilon)

            epsilon2 = random.random()
            differenceToNeighbourhoodBest = subtractTours(neighbourHoodBest[1], swarm[a])
            differenceToNeighbourhoodBestWithEpsilon = epsilonRemove(epsilon2, differenceToNeighbourhoodBest)
            betaVelocity = scalarMultiplyVelocity(beta, differenceToNeighbourhoodBestWithEpsilon)
            
            velocities[a] = thetaVelocity + alphaVelocity + betaVelocity
            
        t = t+1

        # plotting
        # toursToPlot.append((bestTour[0], sum([tourLength(tour) for tour in swarm])//swarmSize))
        # velocitiesToPlot.append(sum([len(v) for v in velocities])/swarmSize)
        # print(len([v for v in velocities if len(v) < 5]))


tour = PSO(swarmSize=swarmSize, theta = theta, alpha = alpha, beta = beta)
tour_length = tourLength(tour)
added_note = f"This is the result from the particle swarm optimisation algorithm with swarm size {swarmSize}, theta={theta} ,alpha={alpha}, beta={beta}"





############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1}, AND YOU SHOULD ALSO
############ HOLD THE LENGTH OF THIS TOUR IN THE RESERVED INTEGER VARIABLE 'tour_length'.
############

############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE,
############ WHOSE NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATA AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")

local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = " + my_user_name + " (" + my_first_name + " " + my_last_name + "),\n")
f.write("ALGORITHM CODE = " + algorithm_code + ", NAME OF CITY-FILE = " + input_file + ",\n")
f.write("SIZE = " + str(num_cities) + ", TOUR LENGTH = " + str(tour_length) + ",\n")
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write("," + str(tour[i]))
f.write(",\nNOTE = " + added_note)
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")
    
    











    


