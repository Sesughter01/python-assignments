# 1. Join the items of this list to a string sentence. Print the result on the terminal. 
    # my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
my_str = " "
my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
new_str = my_str.join(my_list)
print(new_str)

# 2. Change the value of True in this list to False. Print the result on the terminal
    # new_list = ['this', "brown", 55, "oxen", True, 0.85]

new_list = ['this', "brown", 55, "oxen", True, 0.85]
new_list[4] = False
print(new_list)

# 3. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output = ['Green', 'White', 'Black']

def print_list(sample_list) :
      
      sample_list.pop(0)
      sample_list.pop(3)
      sample_list.pop(-1)
      print(sample_list)
      return sample_list

#    print(Sample_List)
new_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


print_list(new_list) 


# 4. Write a program that takes in the user input of his favourite colour and adds it to an existing list of colours.
# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
def store_my_color(sample_list2):
    my_color = input("Enter your favorite color:  ")
    sample_list2.append(my_color)
    print(sample_list2)
    return sample_list2
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']  
store_my_color(color_list)
