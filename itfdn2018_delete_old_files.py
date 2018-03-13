'''ITFDN2018 Final Project - by Gail YamadaThis script will search through specific data directories and delete any directories and files that \are older than a designated time period. e.g only keep 3 years of dataRequirements:Include a function that takes at least two user arguments from the command line (not the input function)Contain at least one if/else statementPerform a calculation on a listUse at least one dictionaryHave one try/except statementWrite either output or a graph to a fileMust include docstrings telling us how to run your scriptEach function must be documented with comments telling us what the purpose of the function is, and what it's inputs and outputs areEither create a class to contain the related functions OR output a simple graphUpload your final python script or jupyter notebook to Github, turn in the link on Canvas---------------Possible ideasimport os  -  to be able to search by pathnameimport datetime  -  to use the 'now' function and other datetime formatsmake a class that can be used with each type of data e.g. sst or ssthr filesattributes directory location data type, date structure prefix file format date to determine what to removefunctions find files create a list of files to remove remove files create a log file'''#!/usr/bin/env python3# to be able to search by pathname and other os functionsimport osimport datetime'''class Datatype:    def __init__(self, name, no_days):    self.name = name    self.no_days = no_days    def location(self, pathname):        self.pathname = pathname    def delete_older(self, filename, datetime):        open with ("Users/gailyamada/data/logfile", a) as logfile        self.filename = filename        self.datetime = datetime        if filename in location < datetime(now) - no_days:           rm filename           logfile.append(filename)                                              ''''''dtypes = ["sst", "ssthr"]num_days_save = [7, 14]dtype_days = list(zip(dtypes, num_days_save))dtype_days_dict = dict(dtype_days)print(dtype_days_dict)'''# find the date time for nowdtnow = datetime.datetime.utcnow()print(dtnow)# find date to starting deleting after 7 daysdate_delete = dtnow - datetime.timedelta(7)print(date_delete)date_del_format = date_delete.strftime('%Y%m%d%H')print(date_del_format)# convert date now into the yyyymmddhh of the fileformat# format yyyymmddhh# date-21 = dt - datetime.timedelta(21)# print(date-21)## date_only = date-21.split(" ")# print(date_only[0])# change into the directory where the data directories areos.chdir("/Users/gailyamada/data")# list the data subdirectoriesos.listdir()# change to a subdirectoryos.chdir("sst")# list the files in the subdirectoryfiles = os.listdir()print(files)# split out just the dates in each filename# create a file to store filename date namesfile_dates = []for f in files:    file_dates = float(f.split(".")[1])    if file_dates < date_del_format:        print(f)# print file_dates#print(file_dates)# if file_dates < 2018022600:#     print(f)'''# list files one file per line without quotesprint("\n".join(os.listdir()))# how many seconds are in 7 daysdelta = datetime.delta(7)print(delta)# what is the date for 7 days ago#days_7_ago = datetime.now() - relativedelta(days = 7)dt7 = dt - days_7_agoprint(dt7)# enter the path to the directorybase_sst = path('/Users/gailyamada/data/sst')# search for a file older than seven days agofor afile in base_sst.walkfiles():    if afile.mtime < dt7:        print(afile)'''