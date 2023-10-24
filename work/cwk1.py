"""
Introduction to Programming Coursework 1

@author: Miles Blackwood
"""


def valid_puzzle(puzzle: list) -> bool:
    if isinstance(puzzle, list) and isinstance(puzzle[0], str): # Checks if the inputed puzzle is a list - returns True if so
        initialLength = len(puzzle[0]) # After checking if the first item is actually a string it stores its length to compare other strings against

        for item in puzzle: # iterates through each item in the puzzle list
            if isinstance(item, str) and len(item) == initialLength:
                pass #Cleared the check, moves onto next item in list

            else:
                return False #Didn't clear the check so puzzle is not valid
            
        return True # If all items in the list clear the check returns true.

    else:
        return False # inputed puzzle is not a list


def similarity_grouping(data: list) -> list:
    groupedArray = [] # initialising an array to store the groups of data in
    for element in data: # iterates through each element within the first array
        grouped = False # Setting up a boolean so I can tell whether an item has been placed into a group yet.
        for group in groupedArray:
            if element in group:
                group.append(element)
                grouped = True
                break
        if grouped == False: # if no existing group for that element a new group is created in the groupedArray
            groupedArray.append([element])
    return groupedArray




def highest_count_items(data: str) -> list:
    items = data.split(",")
    itemCount = []
    for item in items:
        item = item.strip() # removes any whitespace
        added = False
        for i in itemCount: #iterates through each appearance in itemCount
            if item == i[0]: # checks if item is already in itemCount
                i[1] += 1 # adds one to the times it has apeared
                added = True
                break
        if added == False:
            itemCount.append([item, 1])
    
    highestCount = 0
    indexofHighests = []
    for items in enumerate(itemCount):
        if items[1][1] > highestCount: # resets what the highest appearance is
            indexofHighests.clear()
            highestCount = items[1][1]
            indexofHighests.append(items[0])
        
        elif items[1][1] == highestCount: # occurs if multiple items appear the most the samle amount of times
            indexofHighests.append(items[0])
        
        else:
            pass

    maxAppearences = []
    for indexes in indexofHighests:
        maxAppearences.append(itemCount[indexes]) # adds the respective items coresponding to their indexes to the final list

    return maxAppearences





def valid_char_in_string(popList: list, charSet: list) -> bool:
    if isinstance(charSet, list):
        for char in charSet:
            if len(char) != 1:
                return False # invalid character set - list doesn't contain individual characters
        for string in popList:
            for char in string:
                inSet = False
                for item in charSet:
                    if char == item:
                        inSet = True
                if inSet == False:
                    return False # Not all characters are in the character set
        return True # All characters in each string are in the character set
    else:
        return False # invalid character set - not a list


def total_price(unit: int) -> float:
    
    sixPacks = unit // 6 # integer division on unit
    singleUnits = unit % 6 # finds remainder of integer division
    total = (sixPacks * 5) + (singleUnits * 1.25) # finds total price of purchase
    if total >= 20: # applies discount if greater than or equal to £20
        total = total * 0.9 # 10% discount applied
    return total


if __name__ == "__main__":
    # sample test for task 1.1
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
