import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_INN_HORSE_COPPER_PER_NIGHT
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    copper = amount/10
    return float(copper)

def silver2gold(amount:int) -> float:
    silver = amount/5
    return float(silver)

def copper2gold(amount:int) -> float:
    copper = amount/50
    return float(copper)

def platinum2gold(amount:int) -> float:
    platinum = amount*25
    return float(platinum)

def getPersonCashInGold(personCash:dict) -> float:
    platinum = personCash['platinum'] * 25.0
    gold = personCash['gold'] 
    copper = personCash['copper']/10.0/5.0
    silver = personCash['silver']/5.0
    personCash = platinum + gold + copper +silver
    return personCash

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    cost_in_copper = (COST_FOOD_HORSE_COPPER_PER_DAY * horses + COST_FOOD_HUMAN_COPPER_PER_DAY * people) * JOURNEY_IN_DAYS
    cost_in_gold = cost_in_copper/50
    return cost_in_gold

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lijstje = []
    for x in list:
        if key in x and x[key] == value:
            lijstje.append(x)
    return lijstje

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people,'adventuring',True)
    

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends,'sharewith',True)

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends,'friends',True)


##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people /2)
def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    totalCost = horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS + tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)

    return totalCost

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    item_list = []
    for item in items:
        item_list.append(f"{item['amount']}{item['unit']} {item['name']}")

    return ', '.join(item_list)
        
def getItemsValueInGold(items:list) -> float:
    totaal = 0
    for item in items:
        if item['price']['type'] == 'copper':
            totaal += copper2gold( item['amount'] * item['price']['amount'])
        elif item['price']['type'] == 'silver':
            totaal += silver2gold( item['amount'] * item['price']['amount'])
        elif item['price']['type'] == 'platinum':
            totaal += platinum2gold( item['amount'] * item['price']['amount'])
        else:
            gold = item['amount'] * item['price']['amount']
            totaal += gold
    return totaal 
##################### M04.D02.O8 #####################
def getCashInGoldFromPeople(people: list) -> float:
    lijst =[]
    for x in people:
        lijst.append(copper2gold(x['cash']['copper']))
        lijst.append(silver2gold(x['cash']['silver']))
        lijst.append(platinum2gold(x['cash']['platinum']))
        lijst.append(x['cash']['gold'])
    return sum(lijst)
##################### M04.D02.O9 #####################
def getInterestingInvestors(investors:list) -> list:
    return[x for x in investors if x['profitReturn'] >= 10]

def getAdventuringInvestors(investors:list) -> list:
    return [c for c in investors if c['adventuring'] == True and c in investors if c['profitReturn'] < 10]

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total_cost = 0
    Adventuring_Investors = getAdventuringInvestors(investors)
    for x in range(len(Adventuring_Investors)):
        total_cost += getItemsValueInGold(gear)
    
    total_cost += getJourneyFoodCostsInGold(len(Adventuring_Investors),len(Adventuring_Investors))
    total_cost += getTotalRentalCost(len(Adventuring_Investors),len(Adventuring_Investors))
    return total_cost


##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    mens = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    paard = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    totaal = int(leftoverGold / (mens + paard))
    return totaal

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) 
    mensen = gold * people
    paard = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    paarden = paard * horses
    totaal = round((mensen + paarden) * nightsInInn,2)
    return totaal
##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    lijst = []
    for x in investors:
        if x['profitReturn'] < 10:
            lijst.append(round(x['profitReturn'] / 100 * profitGold,2))
    return lijst

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    aantal = 0
    for x in investorsCuts:
        aantal += x
    totaal = round((profitGold - aantal) / fellowship,2)
    return totaal

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()