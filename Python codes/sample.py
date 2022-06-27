
entete = "ncols 54" + "\n" + "nrows 38" + "\n" + "xllcorner    371238.05543283804" + "\n" + "yllcorner    4842053.323856434" + "\n" + "cellsize 70" + "\n" + "NODATA_value -9999.00" + "\n"


file = open("sample.asc", "a")
file.write(entete)
for i in range(38):
    for j in range(54):
        file.write("0.0 ")
    file.write("\n ")



file.close()