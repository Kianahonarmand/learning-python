# Exercise 1
1-a: print("Hello, World!")
1-b: my_text = "Hello, world!"    print(my_text) ====> Hello, world!
1-c: print("Dog", "Kitten", "moon") =====> Dog Kitten moon
# Exercise 2
2-a: glass_of_water=3     print("I drank", glass_of_water, "glasses of water.")   ====> I drank 3 glasses of water.
2-b: glass_of_water = glass_of_water + 1        print(glass_of_water) ===> 4
# Exercise 3
3-a: men_stepped_on_the_moon=8  print(men_stepped_on_the_moon) =========> 8
3-b: my_reason_for_coding="I need it"      print(my_reason_for_coding)   =======> 'I need it'
3-c: global_mean_sea_level_2018=21.36       print(global_mean_sea_level_2018)  ========> 21.36
# Exercise 4
4-a: men_stepped_on_the_moon= 88    answer_1= type(men_stepped_on_the_moon=12)        print(answer_1)  ====> class 'int'
4-b: my_reason_for_coding="intergalactic travel"  answer_2 = type(my_reason_for_coding)  print(answer_2) ====> class 'str'
4-c: global_mean_sea_level_delta_2018=21.36  answer_3 = type(global_mean_sea_level_delta_2018)  print(answer_3) ===>class 'float'
4-d: staying_alive=True     answer_4 = type(staying_alive)      print(answer_4)  ==========> class 'bool'
4-e: my_grade="20"     answer_5 = int(my_grade)      print(answer_5) ========> 20
4-f: my_temp=97.70     answer_6= int(my_temp)      print(answer_6)   ========> 97
4-g: shoe_price="69.99"    answer_ = float(shoe_price)         print(answer_7) =========> 69.99
4-h: gross_world_product=84.84   gwp_str=str(gross_world_product) answer_8="In 2018 gross product of the world (GWP) was " + gwp_str + " in trillion US dollars."     print(answer_8)  ====> In 2018 gross product of the world (GWP) was 84.84 in trillion US dollars.
# Exercise 6 
6-a: lst=[11, 100, 99, 1000, 999]   answer_1=lst[0]     print(answer_1)   ====> 11
6-b: lst=[11, 100, 99, 1000, 999]     print(lst[2])      =======> 99
6-c: lst=[11, 100, 101, 999, 1001]     answer_3 = lst[4]     print(answer_3)  =====> 1001
6-d: gift_list=['socks', '4K drone', 'wine', 'jam']   gift_list.append("pajamas") print(gift_list) =======> ['socks', '4K drone', 'wine', 'jam', 'pajamas']
6-e: gift_list=['socks', '4K drone', 'wine', 'jam']   gift_list.append(["socks","tshirt","pajamas"])  print(gift_list) =====> ['socks', '4K drone', 'wine', 'jam', 'socks', 'tshirt', 'pajamas']
6-f: gift_list=['socks', '4K drone', 'wine', 'jam']   gift_list.insert(2, "slippers")   print(gift_list) =====> ['socks', '4K drone', 'slippers', 'wine', 'jam']
6-g: lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]  answer_1= answer_1=lst.index(8679)   print(answer_1)   =====> 8
6-h: lst=["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]    lst.append(["Navigator", "Suburban"])    print(lst)  ====> ['CRV', 'Outback', 'XC90', 'GL', 'Cherokee', 'Escalade', ['Navigator', 'Suburban']]
6-i: lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]   lst.remove(99)  print(lst)  =====>  [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123]
6-j: lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]  lst.reverse()  print(lst)    =====>  [99, 123, 8679, 2, 1, 101, 76, 6, 54, 777, 55]
6-k: lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]  answer_1=lst.count(6)    print(answer_1) =====> 4
6-l: lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]   answer_1= sum(lst)   print(answer_1)  =======>  1090
6-m: lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]   answer_1= min(lst)   print(answer_1)  =======> 1
6-n: lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]   answer_1= max(lst)   print(answer_1)  =======> 777
# Execise 9
9-a: str = "It's always darkest before dawn."  print(str)  ====> It's always darkest before dawn
9-b: str="It's always darkest before dawn."   ans_1= str[0]+str[1]+str[-1]  print(ans_1) ======> It.
9-c: str="It's always darkest before dawn."  str = str.replace(".", "!")  print(str)   =====>  It's always darkest before dawn!
9-d: str="EVERY Strike Brings Me Closer to the Next Home run."   str = str.lower()  print(str)  =====> every strike brings me closer to the next home run. 
9-e: str="don't stop me now."   str = str.upper()  print(str)   ======> DON'T STOP ME NOW.
9-f: str="there are no traffic JamS Along The extra mile."  str = str.capitalize()  print(str)   ====> There are no traffic jams along the extra mile.
9-g: str="There are no traffic jams along the extra mile."   ans_1=str.startswith("A")  print(ans_1)  ====> False
9-h: str="There are no traffic jams along the extra mile." ans_1= str.endswith(".") print(ans_1) =====> True
9-i: str="The best revenge is massive success."  ans_1= str.index("v")  print(ans_1)   ===> 11
9-j: str="The best revenge is massive success."  ans_1= str.find("m")   print(ans_1)    ====> 20
9-k: str="The best revenge is massive success."  ans_1=str.find("X")  print(ans_1)  ====> -1
9-l: str="People often say that motivation doesn't last. Well, neither does bathing.  That's why we recommend it daily."  ans_1= str.count("a") ans_2= str.count("o") print("count of a is: ", ans_1, " count of o is: ", ans_2)  ====>count of a is:  7  count of o is:  7 
9-m: v_1="1" v_2=1 ans_1= type(v_1) ans_2= type(v_2)  print(ans_1)  print(ans_2) ====> class 'str' / class 'int'
9-n: str="1.975.000"  ans_1= len(str) print(ans_1) =======> 9
# Exercise 11
11-a: lst=[11, 100, 99, 1000, 999]  lst.sort() print(lst)  ====> [11, 99, 100, 999, 1000]
11-b: lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]   lst.sort(reverse = False)   print(lst) =====> ['Belize', 'Canada', 'India', 'Japan', 'Kazakhstan', 'Taiwan', 'Ukraine'] 
11-c: lst=[11, 100, 101, 999, 1001]   lst.sort(reverse = True)  print(lst)  =====> [1001, 999, 101, 100, 11]
11-d: gift_list=['socks', '4K drone', 'wine', 'jam']   gift_list.sort(reverse = True)   print(gift_list)  =====>  ['wine', 'socks', 'jam', '4K drone']
11-e: NFL=["Panthers", "Bears", "Dolphins" "Patriots", "Saints", "Giants"]  NFL.sort(reverse = True)   answer_1= NFL[-1]  print(answer_1)  =====> Bears
11-f: muni=["Melbourne", "Shanghai", "Delhi", "Atlanta", "Moscow", "Montreal"]  muni.sort(reverse = True)  print(muni) =====> ['Shanghai', 'Moscow', 'Montreal', 'Melbourne', 'Delhi', 'Atlanta']
11-g: ict={"tiramisu":5, "chocolate":2, "pudding":3, "cheesecake":4}  key_list = list(dict.keys())  key_list.sort()  print(key_list) =====> ['cheesecake', 'chocolate', 'pudding', 'tiramisu'] 
# Exercise 12
12-a: lst=[11, 100, 99, 1000, 999]  popped_item= lst.pop()  print(popped_item)  print(lst) ====>  999 [11, 100, 99, 1000]
12-b: lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]  a=lst.index("broccoli")  item= lst.pop(a) print(lst, item) ====> ['milk', 'banana', 'eggs', 'bread', 'lemons'] broccoli 
12-c: GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}  italy_gdp= GDP_2018.pop("Italy")  print(GDP_2018)  print(italy_gdp, "trillion USD") ======> {'US': 21, 'China': 16, 'Japan': 5, 'Germany': 4, 'India': 3, 'France': 3, 'UK': 3}
2 trillion USD
# Exercise 17
17-a: wrd="Toscana" ans_1= wrd[0:4]  print(ans_1)  =====> Tosc
17-b: wrd="Toscana"  ans_1= wrd[3:] print(ans_1)   =====> cana
17-c: wrd="Toscana"  ans_1= wrd[3:6]  print(ans_1)  =====> can
17-d: wrd="Toscana"  ans_1= wrd[::2]  print (ans_1)  =====> Tsaa
17-e: wrd="Toscana"  ans_1= wrd[1:-1:2]   print(ans_1) =====> ocn
17-f: lst=[0,1,2,3,4]  ans_1= lst[::-1]  print(ans_1)   ======> [4, 3, 2, 1, 0]
17-g: lst=[0,1,2,3,4]  ans_1= lst[-2:]   print(ans_1)   ======> [3, 4]
17-h: lst=[40,50,20,30,90]  ans_1= lst[1:3]   print(ans_1)   ======> [50, 20]
 

