import os
import random
channels_1 = [
    {"MrBeast": 420000000},
    {"T-Series": 300000000},
    {"Cocomelon": 195000000},
    {"SET India": 185000000},
    {"Kids Diana Show": 135000000},
    {"Vlad and Niki": 140000000},
    {"Like Nastya": 125000000},
    {"Zee Music Company": 120000000},
    {"PewDiePie": 110000000},
    {"WWE": 108000000},
    {"Goldmines": 105000000},
    {"Sony SAB": 102000000},
    {"BLACKPINK": 98000000},
    {"ChuChu TV": 96000000},
    {"Alan Chikin Chow": 95000000},
    {"5-Minute Crafts": 81000000},
    {"BANGTANTV": 83000000},
    {"HYBE LABELS": 78000000},
    {"Justin Bieber": 75000000},
    {"Zee TV": 74000000},
    {"Canal KondZilla": 67000000},
    {"Aaj Tak": 69000000},
    {"Colors TV": 72000000},
    {"Movieclips": 62000000},
    {"Marshmello": 58000000}
    ]

channels_2 = [
    {"Ed Sheeran": 57000000},
    {"Taylor Swift": 62000000},
    {"EminemMusic": 65000000},
    {"Billie Eilish": 55000000},
    {"Dude Perfect": 62000000},
    {"CarryMinati": 45000000},
    {"Technical Guruji": 24000000},
    {"Round2Hell": 36000000},
    {"Ashish Chanchlani": 31000000},
    {"BB Ki Vines": 27000000},
    {"Sandeep Maheshwari": 29000000},
    {"Dhruv Rathee": 31000000},
    {"Total Gaming": 45000000},
    {"Techno Gamerz": 46000000},
    {"Triggered Insaan": 25000000},
    {"Amit Bhadana": 24000000},
    {"FactTechz": 18000000},
    {"A4": 75000000},
    {"Mark Rober": 73000000},
    {"Kurzgesagt": 25000000},
    {"Veritasium": 19000000},
    {"TED": 27000000},
    {"National Geographic": 24000000},
    {"NASA": 13000000},
    {"CrashCourse": 17000000}
]

def higherLower():
    score=0
    while True:
        key_1=random.choice(channels_1)
        key_1_index=channels_1.index(key_1)
        compare_1=list(key_1.keys())[0]

        key_2=random.choice(channels_2)
        key_2_index=channels_2.index(key_2)
        compare_2=list(key_2.keys())[0]

        print(f'Compare 1 : {compare_1}')
        print('VS')
        print(f'Compare 2 : {compare_2}')
        ask=input("who has more followers ? Typ '1' or '2' : ")
        if ask=='1':
            if channels_1[key_1_index][compare_1]>channels_2[key_2_index][compare_2]:
                score+=1
                print(f"You are right. Your score is {score}.")
            else:
                os.system('cls')
                print(f"You wrong ! .. Your final score is {score}")
                return
        elif ask=='2':
            if channels_1[key_1_index][compare_1]<channels_2[key_2_index][compare_2]:
                score+=1
                print(f"You are right. Your score is {score}.")
            else:
                os.system('cls')
                print(f"You wrong ! .. Your final score is {score}")
                return
        else:
            print("invalid input")
            return 
higherLower()
