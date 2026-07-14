string = input("Enter a sentence : ")
str_len = len(string)
short_str = ""
st = set()
for i in string :
    if i != " " :
        short_str += i
    else :
        st.add(short_str)
        short_str = ""
print(st)
print(len(st))