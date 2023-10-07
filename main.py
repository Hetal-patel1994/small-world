if __name__ == '__main__':
    # enter filename
    filename = input("Please enter the name of the file: ")
    try:
        with open(filename) as fp:
            # read first line from the file - read the value of n
            line = fp.readline()
            # file empty
            if not line:
                print("File is empty. Please create more than 1 cast to find the shortest connection.")
                exit()
            n = int(line.strip("\n"))
            if n < 2:
                print("Number of casts must be greater than 1")
                exit()
            casts = []
            line = fp.readline()
            while line:
                # splitting the actors into a list delimited by comma
                actorsInput = line.strip("\n").split(",")
                # prepare a cast of actors
                actors = []
                # stripping leading and trailing white spaces from the input
                for actor in actorsInput:
                    actors.append(actor.strip())
                # adding it to a list
                casts.append(actors)
                line = fp.readline()
        if len(casts) != n:
            print("Mismatch between n and number of casts as input. Please fix the file.")
            exit()
        # compare 1st cast with the 2nd cast and print the common actor if any
        commonActor = ""
        found = False
        for act1 in casts[0]:
            for act2 in casts[1]:
                if act1 == act2:
                    commonActor = act1
                    found = True
                    break
        # if common actor is found
        if found:
            print("Shortest connection = 1, Actor = " + commonActor + ".")
        else:
            # look for other casts and find a common between each of the above two casts
            for itr in range(2, len(casts)):
                # checking if first cast has common actor with cast j and second cast has common actor with cast j
                if set(casts[0]).intersection(casts[itr]) and set(casts[1]).intersection(casts[itr]):
                    found = True
                    print("Shortest Connection = 2, Cast =", casts[itr])
                    break
            # if there is no common actor
            if not found:
                print("Shortest Connection > 2 or no connection.")
    except FileNotFoundError:
        # if file name is not correct
        print("Please enter the correct fileName.")
    except Exception as e:
        # generic exception handled
        print("Some error occurred" + e)
