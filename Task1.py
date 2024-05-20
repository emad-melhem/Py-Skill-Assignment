         # 1
x = 25 #integer
y = 3.14 #float
z = "Advanced Python" #string
is_active = False #boolean

        # 2
# I added formatting to the numbers to make the output clearer.
print("{:.2f}".format(x / y))
new_string = str(x) + z
 # OR
 # new_string = "".join([str(x), z])
print(new_string)
 #OR
 # print(f"{x}{z}")
 #OR
 # print(x, z, sep="")
is_active = not is_active # toggle the bool variable.
print(is_active)