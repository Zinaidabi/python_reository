# str (string) < methods

# 'Dorin'
# ' Dorin '
# ' dorin '
# ' dOrin '
def removeSpace( name ):
    name_ = name.strip()
    return name_

def fixCase( name ):
    name_ = name.capitalize()
    return name_

#################
#HW1: rewrite the code bellow so functions pass name throgh a variable

#correct_name = removeSpace(' Dorin')
randon_name = (' dOrIn')
free_space_name = removeSpace(randon_name)
correct_name = fixCase( free_space_name)
print(f'|{correct_name}|')