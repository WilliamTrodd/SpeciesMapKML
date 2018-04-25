import openpyxl

### Ver0.1, created 04/18
### To-Do: species colour dictionary     species_colour = {"P. pipistrellus":"yellow","P. pygmaeus":"red","Myotis sp.":"}
###                                     green, red, yellow, blue, purple, pink, orange, brown

### This function will run through a file and create a 2d list of locations
### and their associated recorded species

### This will create seperate kml files for each

##########################################
#                                        #
# mk_tbl() needs column numbers for:     #
#     species_id                         #
#     site                               #
#     recording time                     #
#     transect number                    #
#     image link                         #
#     latitude                           #
#     longitude                          #
#  where column "A" = 0                  #
# it assumes:                            #
#     the first row includes             #
#       column headings                  #
#     two species columns, adjacent      #
#       to one another                   #
##########################################

def mk_tbl(file_in,
           sheet,
           sp_col,
           site_col,
           time_col,
           tran_col,
           img_col,
           lat_col,
           lon_col):

    ### This is a temporary solution to deal with colours with my own dataset and will be changed in later versions
    species_colour = {"P. pipistrellus":"grn",
                      "P. pygmaeus":"red",
                      "Myotis nattereri":"ylw",
                      "Myotis sp.":"blue",
                      "Sp. 1":"purple",
                      "Sp. 2":"pink",
                      "Sp. 3":"ltblu",
                      "NSL":"wht"}
    ###
    
    ### Imports data from excel spreadsheet 
    wb = openpyxl.load_workbook(file_in, data_only=True)
    ### Imports the sheet
    data = wb[sheet]

    
    ########################
    #                      #
    # Loop through list to #
    # extract the relevant #
    # data for compiling   #
    # into a .kml file.    #
    #                      #
    ########################

    ### Setting up variables needed for the loop

    current_site = "" # this will help make seperate kml files
    current_transect = 0
    
    ### This will loop through each site, moving to a new path
    ### in the kml file each time
    for row in data.iter_rows(min_row=2,
                              max_col=max(sp_col,
                                          site_col,
                                          time_col,
                                          tran_col,
                                          img_col,
                                          lat_col,
                                          lon_col
                                          )+1
                              ):
        if row[site_col].value == None:
            break
        if current_transect != row[tran_col].value:
            try:
                output.write('\n    </Folder>\n  </Document>\n</kml>')
            except:
                print("whoops")
            current_site = row[site_col].value
            current_transect = row[tran_col].value
            marker_num = 0
            output = open(current_site +
                          "_" +
                          str(current_transect) +
                          ".kml","w"
                          )
            
            output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            output.write('<kml xmnls="http://www.opengis.net/kml/2.2">\n')
            output.write('  <Document>\n    <Folder>\n')
            ###output.write('      <Style id="
            output.write('        <name>' +
                         current_site +
                         '</name>\n')
            output.write('            <description>Recordings of species at ' +
                         current_site +
                         '</description>)')            

        


        if row[sp_col].value != "NONE":
            marker_num += 1
            if row[sp_col+1].value != "NONE":
                output.write('    <Placemark>\n    <name>' +
                             str(row[sp_col].value) +
                             ' and ' +
                             str(row[sp_col+1].value) +
                             '</name>\n')
            else:
                print(row[sp_col].value)
                output.write('    <Placemark>\n    <name>' +
                             str(row[sp_col].value)+
                             '</name>\n')
            output.write('        <Icon>\n        <href>http://maps.google.com/mapfiles/kml/pushpin/{0}-pushpin.png</href>\n       </Icon>'.format(species_colour[str(row[sp_col].value)]))
            output.write('      <description>Recording: ' +
                         str(marker_num) +
                         '\n')
            if row[img_col].value != 0:
                output.write('<img style="max-width:500px;" src="' +
                             str(row[img_col].value) +
                             '"></img>\n')
            output.write('\n    Time:' +
                         str(row[time_col].value) +
                         '\n      </description>\n')
            output.write('\n    <Point>\n       <coordinates>' +
                         str(row[lon_col].value) +
                         ',' +
                         str(row[lat_col].value) +
                         '</coordinates>\n    </Point>\n    </Placemark>\n\n')
        

    try:
        output.write('\n    </Folder>\n  </Document>\n</kml>')
        output.close()
        print("closing")
    except:
        print("nothing to close")
        
        

mk_tbl((input('What is the name of the excel spreadsheet? ')+'.xlsx'),
       (input('What is the name of the sheet? ')),
       (int(input('What column is the species ID? '))),
       (int(input('What column is the site name? '))),
       (int(input('What column is the recording time in? '))),
       (int(input('What column is the transect number? '))),
       (int(input('What column is the image link in? '))),
       (int(input('What column is the latitude in? '))),
       (int(input('What column is the longitude in? '))))
   
