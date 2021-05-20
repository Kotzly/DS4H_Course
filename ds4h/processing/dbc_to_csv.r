
# dir.create("./.Rlocal")
# install.packages('read.dbc', lib="./.Rlocal")
install.packages('read.dbc')
library('read.dbc')

args = commandArgs(trailingOnly=TRUE)
input_folder = args[1]
output_folder = args[2]

files = list.files(input_folder)
for (file in files){

    filename = strsplit(file, ".dbc")[1]
    
    dbc_filepath = paste(input_folder, file, sep="/")

    csv_filepath = paste(
        output_folder, paste(filename, ".csv", sep=""), sep="/"
    )
    
    print(dbc_filepath)
    df <- read.dbc(dbc_filepath)

    write.csv(df, csv_filepath)
}

#unlink("./.Rlocal", recursive=TRUE)
