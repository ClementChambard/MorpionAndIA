from random import randrange

def iajouer(Trest,plat):
    """
        Look on every possibility of the board and evaluate the better one

        This function use the minmax algorithm to test each case of the board
        and modify one of the case with the maximum possibility of win.

        :param Trest: number of turn left
        :param plat: current board
        :type Trest: int
        :type plat: 2D int list
        :return: nothing, just modify the board with the best value

        :Example:

        >>> board = [[1,0,2][0,0,2][1,2,1]]

        >>> iajouer(3,board)

        >>> board
        [[1,0,2][0,1,2][1,2,1]]

        .. seealso:: minimum(), maximum()
    """
    max_prob = -1000
    i = 0

    while i < 3:
        j = 0
        while j < 3:
            if plat[i][j] == 0:
                plat[i][j] = 1
                prob = minimum(Trest - 1,plat)
                plat[i][j] = 0
            else:
                prob = -2000

            if prob > max_prob or (prob == max_prob and randrange(0,9)%2 == 0):
                max_prob = prob
                max_i = i
                max_j = j

            j += 1
        i += 1

    plat[max_i][max_j] = 1




def minimum(Trest,plat):
    """
        Look on every possibility of the board when it's Player turn

        This function test all case and return the minimum probability
        of IA's win when it's the player turn.

        :param Trest: number of turn left
        :param plat: current board
        :type Trest: int
        :type plat: 2D int list
        :return: minimum possibility of win
        :rtype: int

        .. seealso:: maximum(),winner(),evaluation()
    """
    if Trest <= 0 or winner(plat):
        return evaluation(plat,Trest + 1)

    min_prob = 1000
    i = 0

    while i < 3:
        j = 0
        while j < 3:
            if plat[i][j] == 0:
                plat[i][j] = 2
                prob = maximum(Trest - 1,plat)
                plat[i][j] = 0
            else:
                prob = 2000

            if prob < min_prob or (prob == min_prob and randrange(0,9)%2 == 0):
                min_prob = prob

            j += 1
        i += 1

    return min_prob




def maximum(Trest,plat):
    """
        Look on every possibility of the board when it's IA turn

        This function test all case and return the maximum probability
        of IA's win when it's the IA turn.

        :param Trest: number of turn left
        :param plat: current board
        :type Trest: int
        :type plat: 2D int list
        :return: maximum possibility of win
        :rtype: int

        .. seealso:: minimum(),winner(),evaluation()
    """
    if Trest == 0 or winner(plat):
        return evaluation(plat,Trest + 1) + Trest

    max_prob = -1000
    i = 0

    while i < 3:
        j = 0
        while j < 3:
            if plat[i][j] == 0:
                plat[i][j] = 1
                prob = minimum(Trest - 1,plat)
                plat[i][j] = 0
            else:
                prob = -2000

            if prob > max_prob or (prob == max_prob and randrange(0,9)%2 == 0):
                max_prob = prob

            j += 1
        i += 1

    return max_prob




def evaluation(plat,Trest):
    """
        return a probability at the end of the simulation

        This function return a great number if the IA win and a great
        negative number if the player win. else it return 0
        the number is even bigger if there are more turn left

        :param Trest: number of turn left
        :param plat: current board
        :type Trest: int
        :type plat: 2D int list
        :return: the final probability of win
        :rtype: int

        .. seealso:: winner()
    """
    if winner(plat) == 1:
        return 1000
    elif winner(plat) == 2:
        return -1000
    else:
        return 0
    return series(plat)

def series(plat):
    """
        test every line to determine which player have the most chance to win

        This function test all line and calculate the number of series of 2 case
        of each player. It return the difference of the two series number

        :param plat: current board
        :type plat: 2D int list
        :return: difference between the number of lines
        :rtype: int
    """
    compteur1,compteur2,i,j,series_j1,series_j2 = 0,0,0,0,0,0

    #diagonale descendante
    while i < 3:
        if plat[i][i] == 1:
            compteur1 += 1
            compteur2 = 0
            if compteur1 == 2:
                series_j1 += 1

        elif plat[i][i] == 2:
            compteur2 += 1
            compteur1 = 0
            if compteur2 == 2:
                series_j2 += 1

        i += 1

    compteur1,compteur2,i = 0,0,0

    #Diagonale montante
    while i < 3:
        if plat[i][2-i] == 1:
            compteur1 += 1
            compteur2 = 0
            if compteur1 == 2:
                series_j1 += 1

        elif plat[i][2-i] == 2:
            compteur2 += 1
            compteur1 = 0
            if compteur2 == 2:
                series_j2 += 1
        i += 1

    i = 0

    #Lignes
    while i < 3:
        compteur1,compteur2,j = 0,0,0

        #Horizontalement
        while j < 3:
            if plat[i][j] == 1:
                compteur1 += 1
                compteur2 = 0
                if compteur1 == 2:
                    series_j1 += 1

            elif plat[i][j] == 2:
                compteur2 += 1
                compteur1 = 0
                if compteur2 == 2:
                    series_j2 += 1
            j += 1

        compteur1,compteur2,j = 0,0,0

        #Verticalement
        while j < 3:
            if plat[j][i] == 1:
                compteur1 += 1
                compteur2 = 0
                if compteur1 == 2:
                    series_j1 += 1

            elif plat[j][i] == 2:
                compteur2 += 1
                compteur1 = 0
                if compteur2 == 2:
                    series_j2 += 1
            j += 1

    return series_j1 - series_j2



def winner(plat):
    """
        test every line to determine the winner

        This function test all line and return 1 if the IA have at least
        one line and return 2 if the player have at least one line.
        else it return 0 or 3

        :param plat: current board
        :type plat: 2D int list
        :return: the winner
        :rtype: int
    """
    if plat[0][0] == plat[0][1] == plat[0][2] == 1\
    or plat[1][0] == plat[1][1] == plat[1][2] == 1\
    or plat[2][0] == plat[2][1] == plat[2][2] == 1\
    or plat[0][0] == plat[1][0] == plat[2][0] == 1\
    or plat[0][1] == plat[1][1] == plat[2][1] == 1\
    or plat[0][2] == plat[1][2] == plat[2][2] == 1\
    or plat[0][0] == plat[1][1] == plat[2][2] == 1\
    or plat[2][0] == plat[1][1] == plat[0][2] == 1:

        return 1

    elif plat[0][0] == plat[0][1] == plat[0][2] == 2\
    or plat[1][0] == plat[1][1] == plat[1][2] == 2\
    or plat[2][0] == plat[2][1] == plat[2][2] == 2\
    or plat[0][0] == plat[1][0] == plat[2][0] == 2\
    or plat[0][1] == plat[1][1] == plat[2][1] == 2\
    or plat[0][2] == plat[1][2] == plat[2][2] == 2\
    or plat[0][0] == plat[1][1] == plat[2][2] == 2\
    or plat[2][0] == plat[1][1] == plat[0][2] == 2:

        return 2

    else:
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                if plat[i][j] == 0:
                    return 0
                j += 1
            i += 1
        return 3

def affplat(plat):
    """
        display the current board

        :param plat: current board
        :type plat: 2D int list
    """
    print(plat[0][0],"|",plat[0][1],"|",plat[0][2])
    print(plat[1][0],"|",plat[1][1],"|",plat[1][2])
    print(plat[2][0],"|",plat[2][1],"|",plat[2][2])




def choixjoueur(plat):
    """
        ask the player whitch case to play

        It also test if the case is allready played and if it's the
        case, it return the same function

        :param plat: current board
        :type plat: 2D int list
        :return:the same function
    """
    c = input("sur quelle case voulez vous jouer ? ")

    if c == "1":
        if plat[2][0] == 0:
            plat[2][0] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)

    elif c == "2":
        if plat[2][1] == 0:
            plat[2][1] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)

    elif c == "3":
        if plat[2][2] == 0:
            plat[2][2] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)

    elif c == "4":
        if plat[1][0] == 0:
            plat[1][0] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)

    elif c == "5":
        if plat[1][1] == 0:
            plat[1][1] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)

    elif c == "6":
        if plat[1][2] == 0:
            plat[1][2] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)

    elif c == "7":
        if plat[0][0] == 0:
            plat[0][0] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)

    elif c == "8":
        if plat[0][1] == 0:
            plat[0][1] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)

    else:
        if plat[0][2] == 0:
            plat[0][2] = 2
        else:
            print("case deja jouee")
            return choixjoueur(plat)
