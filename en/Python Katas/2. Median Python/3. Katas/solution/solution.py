# -*- coding: utf-8 -*
''' Search for products in a file  '''

# First function - Get list with properties from file:
def from_file_to_list(f):
  '''
  Input: f - file name.
  Return: list_of_products - list with data from file.
  '''

  read_file = open(f,'r') # file open

  # help variables:
  list_of_products = [] # list for products
  list_of_product_properties = [] # list for product properties

  # Get around all line in file:
  for line in read_file:
    list_of_product_properties = line.split() # add one line to list
    list_of_products.append(list_of_product_properties) # add list with line to list

  read_file.close() # file close

  return list_of_products

# Second function - Search name of product in file:
def search_product_by_name(search,f):
  '''
  Input: name - name of product, f - file name
  Return: tuple with: name, countries, value
  '''

  # get data from file as list:
  list_with_products = from_file_to_list(f)

  # help variables:
  name = '' # name of product
  countries = [] # list of export country
  value = 0 # value of all export

  for index,element in enumerate(list_with_products):  # use enumerate(, start[o]) fot search name of product
    if element[0] == search:
        name = element[0]
        countries.append(element[1])
        value = value + int(element[2])

  return (name, countries, value)

# file variable:
data_file = 'data.txt' # file with data

# Main part:
search = str(input("Enter product name: ")) # input search product name
variables_for_print = search_product_by_name(search, data_file) # get variable for final print

# Print part:
countries_as_str = ' '.join(variables_for_print[1]) # get all countries for print
print("Product: %s; Country for export: %s; Volume: %s;" % (variables_for_print[0],countries_as_str,variables_for_print[2])) # Final print
