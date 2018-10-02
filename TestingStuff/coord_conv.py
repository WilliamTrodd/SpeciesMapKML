def coord_convert(coords):
    try:
        coord_split = coords.split(" ")
        lat_deg = coord_split[:2] ## ['Nxx', 'xx.xxx']
        lon_deg = coord_split[2:] ## ['Wxx', 'xx.xxx']

        #print(lat_deg)
        #print(lon_deg)

        lat_deg[1] = float(lat_deg[1])/60
        #print(lat_deg)
        lat_coord = int(lat_deg[0][1:]) + lat_deg[1]
        if(lat_deg[0][0]=="S"):
            lat_coord*=-1
        #print(lat_coord)

        lon_deg[1] = float(lon_deg[1])/60
        #print(lon_deg)
        lon_coord = int(lon_deg[0][1:]) + lon_deg[1]
        if(lon_deg[0][0]=="W"):
            lon_coord*=-1
        #print(lon_coord)
        return lat_coord,lon_coord
    except:
        print("oops")
    

def in_out(file_in,file_out):
    file_in = open(file_in,"r")
    file_out = open(file_out,"w")
    for line in file_in:
        if line == "\n":
            file_out.write("\n")
        else:
            new_coords = coord_convert(line)
            #print(new_coords)
            file_out.write(str(new_coords)+"\n")
            #print line
        
#coord_convert("N50 45.020 W1 31.778")
in_out("all_coords.txt","all_conv_coords.txt")
