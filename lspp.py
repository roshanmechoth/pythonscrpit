def filessearch():
    import bpdb
    import os
    #Import math and time module
    
    #Set listing start location
    start_path = "/home/roshan/test"
    dir_count = 0
    file_count = 0   
    #Traverse directory tree
    for (path,dirs,files) in os.walk(start_path):
        print('Directory: {:s}'.format(path))
        dir_count += 1
        #Repeat for each file in directory
        for file in files:
            fstat = os.stat(os.path.join(path,file))
            
            # Print file attributes
            print('File Name :\t{:15.15s}'.format(file))
            # first_line =open(file).readline()
            # bpdb.set_trace()
            with open(file) as f:
                line = f.readline()
                print line
            file_count += 1
    # Print total files and directory count
    print('\nFound {} files in {} directories.'.format(file_count,dir_count))  

if __name__ == "__main__":
    filessearch()