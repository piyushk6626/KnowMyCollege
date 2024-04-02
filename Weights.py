
import pandas as pd
import time

start_time = time.time()
#Function to get sorted List
def Value(df, placement_pref, coding_pref, campus_size_value, higher_studies_pref,Cultural_Pref,brand_value,Entra ,a,b,c,d,e,f,g):
    totals = []
    for index, row in df.iterrows():
        total = 0
        placement = row['Placement ']
        coding_culture = row['Coding_Culture']
        campus = row['Campus']
        Higher_Eduction = row['Higher Education']
        
        Higher_Eduction_pref=0
        if higher_studies_pref == 'y':
            Higher_Eduction_pref += 100
        else:
            Higher_Eduction_pref += 0

        # states = 0
        # states_arr = [100, 75, 60, 50, 40]
        # for i in range(5):
        #     if states[i] == row['STATE']:
        #         states += states_arr[i]
                
        Cultural_Activity = row['Cultural_Activity'] 
        
        # Branch= row['Parent Branch']
        # Branch_pref=0
        # arr2=[100,88,76,64,52,40,28,16]
        
        # for i in range(len(Branches)):
        #     if Branch== Branches[i]:
        #         Branch_pref+=arr2[i]
                
        brand= row['Brand_Value']
        Entrepreneurship= row['Entrepreneurship_Culture']
        

        total += int(placement_pref) * placement*a
        total += int(coding_pref) * coding_culture*b
        total += int(campus_size_value) * campus*c
        total += int(Higher_Eduction_pref) * Higher_Eduction*d
        #total += int(states)
        total += int(Cultural_Activity)*int(Cultural_Pref)*e
        #total += Branch_pref*5
        total += brand*int(brand_value)*f
        total += Entrepreneurship*int(Entra)*g
        totals.append(total)    
    df['Total'] = totals
    
    sorted_df = df.sort_values(by='Total', ascending=False)
    LIST=[]
    for index,row in sorted_df.iterrows():
        V1 = row['College Name']
        V2 = row['Branch']
        V3 = f"{V1} {V2}"  
        LIST.append(V3)
    return LIST



#function to calculate persentage correctness
def correctness(Given,Known):
    correct=0
    for i in range(len(Given)):
        if Given[i]==Known[i]:
            correct+=1
    correct=correct*(100/len(Given))
    return correct    
            
#List
Known=[
    "IIT BOMBAY COMPUTER SCIENCE & ENGINEERING",
    "IIT DELHI COMPUTER SCIENCE AND ENGINEERING",
    "IIT KANPUR COMPUTER SCIENCE & ENGINEERING",
    "IIT MADRAS COMPUTER SCIENCE & ENGINEERING",
    "IIT Kharagpur COMPUTER SCIENCE & ENGINEERING",    
    "IIT ROORKEE COMPUTER SCIENCE AND ENGINEERING",
    "IIT HYDERABAD COMPUTER SCIENCE & ENGINEERING",
    "IIT GUWAHATI COMPUTER SCIENCE & ENGINEERING",
    "IIT BHU COMPUTER SCIENCE AND ENGINEERING",        
    "IIT INDORE COMPUTER SCIENCE AND ENGINEERING",
    "IIT DHANBAD COMPUTER SCIENCE AND ENGINEERING",
    "IIT PATNA COMPUTER SCIENCE & ENGINEERING",
    "IIT ROPAR COMPUTER SCIENCE AND ENGINEERING",    
    "IIT GANDHINAGAR COMPUTER SCIENCE AND ENGINEERING",
    "IIT JODHPUR COMPUTER SCIENCE & ENGINEERING",
    "IIT MANDI COMPUTER SCIENCE AND ENGINEERING",
    "IIT TIRUPATI COMPUTER SCIENCE AND ENGINEERING",
    "IIT BHUBANESHWAR COMPUTER SCIENCE AND ENGINEERING",
    "IIT JAMMU COMPUTER SCIENCE AND ENGINEERING",
    "IIT GOA COMPUTER SCIENCE & ENGINEERING",
    "IIT PALAKKAD COMPUTER SCIENCE AND ENGINEERING",
    "IIT DHARWAD COMPUTER SCIENCE & ENGINEERING",
    "IIT BHILAI COMPUTER SCIENCE AND ENGINEERING"]
def loop(df):
    Max=0
    weights=[1,2,3,4,5,6,7]
    for a in range(5):
        print(f"a={a}")
        for b in range(5):
            print(f"b={b}")
            for c in range(5):
                #print(f"c={c}")
                for d in range(5):
                    #print(f"d={d}")
                    for e in range(5):
                        #print(e)
                        for f in range(5):
                            for g in range(5):
                                calculated=Value(df,10,10,10,'y',10,10,10,a,b,c,d,e,f,g)
                                temp=correctness(calculated,Known)
                                if temp >Max:
                                    Max=temp
                                    weights=[a,b,c,d,e,f,g]

            print(f"max= {Max}%")
            print(*weights)
    return weights
                            
                            
def main():
    file_path = 'static/List.csv'
    df = pd.read_csv(file_path)
    answer=loop(df)
    print(answer)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution time:", elapsed_time, "seconds")                                
    
if __name__=='__main__':
    main()                            

#for 0-5
#max= 69.56521739130434%
#3 0 0 0 4 0 3
#[3, 0, 0, 0, 4, 0, 3]
#Execution time: 141.98538327217102 seconds