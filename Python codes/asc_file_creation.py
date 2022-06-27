# Creation of the asc files with their headers
# One file is created every 30s
# If you want to generate files at different times, change the increment of x

x = 0
header = "ncols 54" + "\n" + "nrows 38" + "\n" + "xllcorner    371238.05543283804" + "\n" + "yllcorner    4842053.323856434" + "\n" + "cellsize 70" + "\n" + "NODATA_value -9999.00" + "\n"
while x < 3600:
    x = x + 30
    fileName = str(x) + ".asc"
    print(fileName)
    file = open(fileName, "w+")
    file.write(header)
    file.close()



# Filling the files with the values from the gauges

rows = 54
x = 0
cpt = 1
while x <= 2051:
    value = []
    eta = []
    if x < 10: 
        nom = "gauge0000" + str(x) + ".txt"
    elif x < 100:
        nom = "gauge000" + str(x) + ".txt"
    elif x < 1000:
        nom = "gauge00" + str(x) + ".txt"
    else:
        nom = "gauge0" + str(x) + ".txt"
    print(nom)
    with open(nom,'r') as data_file:
        for line in data_file:
            data = line.split()
            value.append(data[1])
            eta.append(float(data[2]))

    x = x + 1
    i = 0
    j = 0
    while i < 3600:
        name_asc = str(i) + ".asc"
        file_asc = open(name_asc,"a")
        
        if float(value[j]) == 0:								# gauge on land
            height = value[j]
        elif (float(value[j]) > 10) and (float(eta[j]) <10):	# gauge in the sea
            height = str(eta[j])
        elif (float(value[j]) > 1) and (float(eta[j]) <10):		# gauge at the border of the sea
            height = str(eta[j])
        else:
            height = value[j]

        if cpt%rows ==0:							# end of the row
            height = height +" \n"
        else:										# middle of the row
            height = height +" "
        file_asc.write(height)
        file_asc.close()
        i = i + 30
        j = j + 1
    cpt = cpt + 1
    data_file.close()