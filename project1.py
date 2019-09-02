def formats(lists) :
    row_labels = ['Student','Name','Midterm','Final','Average','Grade'] 
    print(" {0:9} {1:>15}   {2:^7}   {3:^5}   {4:^7}   {5:^4}".format(*row_labels))
    print("-"*62)
    for i in range(0,len(lists)):
        print("{0:<9}  {1:>15}    {2:^7}   {3:^5}   {4:^7.1f}   {5:^4}"
              .format(lists[i][0],lists[i][1],
                      lists[i][2],lists[i][3],
                      lists[i][4],lists[i][5]))
        
def score_cal(lists) :
    for i in range (0, len(lists)) :
        lists[i][4] = ((int(lists[i][2]) + int(lists[i][3]))/2)
        if lists[i][4] >= 90:
            lists[i][5] = "A"

        elif lists[i][4] >= 80:
            lists[i][5] = "B"

        elif lists[i][4] >= 70:
            lists[i][5] = "C"

        elif lists[i][4] >= 60:
            lists[i][5] = "D"

        else :
            lists[i][5] = "F"        


def SHOW(lists) :
    lists.sort(key=lambda e:e[4], reverse = True)
    return formats(lists)
    
    
def SEARCH() :
    stu_id = input("Student ID:")
    j = 0
    value = 0

    for i in range (0,len(stu_list)) :         
        if stu_id in stu_list[i][0] :
            j += 1
            value = i

    if j == 0 :
        b = print("NO SUCH PERSON.")
        return b
    
    else : 
        a = [stu_list[value]]
    
    return formats(a)
    
def CHANGESCORE() :
    stu_id = input("Student ID:")
    j = 0
    value = 0
    mid_final = ""
    new_score = 0
    global stu_list


    for i in range (0,len(stu_list)) :         
        if stu_id in stu_list[i][0] :
            j += 1
            value = i

    if j == 0 :
        b = print("NO SUCH PERSON.")
        return b
    
    else : 
        mid_final = (input("Mid/Final?").upper())
        
        if mid_final == "MID" :

            new_score = int(input("Input new score:"))
            if new_score > 100 :
                return;
                
            elif new_score < 0 :
                return;
            
            else :
                formats([stu_list[value]])
                print("Score changed.")
                stu_list[value][2] = new_score
                score_cal(stu_list)
                formats([stu_list[value]])

        elif mid_final == 'FINAL' :
            new_score = int(input("Input new score:"))
            if new_score > 100 :
                return;
                
            elif new_score < 0 :
                return;
            
            else :
                formats([stu_list[value]])
                print("Score changed.")
                stu_list[j][3] = new_score
                score_cal(stu_list)
                formats([stu_list[value]])
                
                
def ADD(stu_list) :
    stu_id = input("Student ID:")
    j = 0
    value = 0
    mid_final = ""
    mid = 0
    final = 0
    new_score = 0


    for i in range (0,len(stu_list)) :         
        if stu_id in stu_list[i][0] :
            j += 1
            value = i

    if j == 0 :
        stu_list.append([])
        stu_list[len(stu_list)-1].append(stu_id)
        stu_list[len(stu_list)-1].append(input("Name:"))
        mid = int(input("Midterm Score:"))
        if mid > 100 :
            del(stu_list[len(stu_list)-1])
            return ;
        elif mid < 0 :
            del(stu_list[len(stu_list)-1])
            return ;
        else :
            stu_list[len(stu_list)-1].append(mid)
        final = int(input("Final Score:"))
        if final > 100 :
            del(stu_list[len(stu_list)-1])
            return ;
        elif final < 0 :
            del(stu_list[len(stu_list)-1])
            return ;
        else :
            stu_list[len(stu_list)-1].append(final)
        stu_list[len(stu_list)-1].append(float())
        stu_list[len(stu_list)-1].append("")
        score_cal(stu_list)
        print ("Student added.")
    
    else :
        b = print("ALREADY EXISTS")
        return b
    
    
def SEARCHGRADE() :
    grade = input("Grade to search:").upper()
    global stu_list
    j = 0
    value = []
    stu_listt = []
    
    if (grade == "A" or grade == "B"or grade == "C"or grade == "D"or grade == "F"):
        for i in range (0, len(stu_list)) :
            if stu_list[i][5] == grade :
                j += 1
                value.append(i)
            
        if j == 0 :
            print("NO RESULTS.")
            
        else :
            for i in value :
                stu_listt.append(stu_list[i])
            formats(stu_listt)
    
    else :
        return;
        
    
def REMOVE() :
    global stu_list
    j = 0
    value = 0
    
    if stu_list == [] :
        print("List is empty.")
    
    else :
        stu_id = input("Student ID:")
        
        for i in range (0,len(stu_list)) :         
            if stu_id in stu_list[i][0] :
                j += 1
                value = i

        if j == 0 :
            b = print("NO SUCH PERSON.")
            return b
    
        else : 
            stu_list.pop(value)
            print("Student removed.")
            
            
def QUIT(lists) :
    quit = input("Save data?[yes/no]").upper()
    
    if quit == "YES":
        file_name = input("File name:")
        
        f =  open(file_name, "w")
        lists.sort(key=lambda e:e[4], reverse = True)
        for i in range(0,len(lists)):
            data = (lists[i][0]+"\t"+lists[i][1]+"\t"+lists[i][2]+"\t"+lists[i][3]+"\t"+str(lists[i][4])+"\t"+lists[i][5]+"\n")
            f.write(data)
        
        f.close()
        return True    
    
    else :
        return;

    
    
### 파일 불러오기
import sys

file_name = "students.txt"

try : 
    file_name = sys.argv[1]

except :
    file = open(file_name, "r")
    
file = open(file_name, "r")

data = file.read()

### 데이터 가공하기
raw = []; student = []; name = []; midterm = []; final = []; info =[]; stu_list =[]

raw = data.split("\n")

for i in range(0, len(raw)-1) :
    a,b,c,d = raw[i].split("\t")
    student.append(a), name.append(b), midterm.append(c), final.append(d)

for i in range(0, len(student)):
    info.append([student[i], name[i], midterm[i],final[i]])
    stu_list.append(info[i])
    
stu_list.sort(key=lambda e:e[3], reverse = True)

### 평균점수 매기기

for i in range(0, len(stu_list)):
    stu_list[i].append((((int(stu_list[i][2])) + int(stu_list[i][3]))/2))
    
for i in range(0, len(stu_list)):
    if stu_list[i][4] >= 90 :
        stu_list[i].append("A")

    elif stu_list[i][4] >= 80 :
        stu_list[i].append("B")

    elif stu_list[i][4] >= 70 :
        stu_list[i].append("C")
        
    elif stu_list[i][4] >= 60 :
        stu_list[i].append("D")
        
    else :
        stu_list[i].append("F")
    
### 메인함수

def main() :
    formats(stu_list)

    while True :
        function = input("#(show,search,changescore,add,searchgrade,remove,search,quit):").upper()
    
        if function == "SHOW" :
            SHOW(stu_list)
    
        elif function == "SEARCH" :
            SEARCH()
    
        elif function == "CHANGESCORE" :
            CHANGESCORE()

        elif function == "ADD" :
            ADD(stu_list)

        elif function =="SEARCHGRADE" :
            SEARCHGRADE()

        elif function == "REMOVE" :
            REMOVE()

        elif function == "SEARCH" :
            SEARCH()

        elif function == "QUIT" :
            QUIT(stu_list)
            break
            
            
if __name__ == '__main__' :
    main()