#######################################################################################################

import os

#######################################################################################################

def compare_files(directory):
    '''
    Compare '.cmp' and '.out' files in directory and record missing '.out' files
    '''

    missing_files = []

    for file in os.listdir(directory):

        if file.endswith('.cmp'):
            cmp_file = file
            out_file = os.path.basename(file).replace('.cmp', '.out')

            if os.path.exists(os.path.join(directory, out_file)):

                print(f'Comparing {cmp_file} and {out_file} at {directory}...')

                with open(os.path.join(directory, out_file)) as f_1:
                    out_file_content = f_1.readlines()

                with open(os.path.join(directory, cmp_file)) as f_2:
                    cmp_file_content = f_2.readlines()

                if out_file_content == cmp_file_content:
                    print('✅ Files are equal')
                else:
                    print('⛔️ Files are not equal')
            
            else:
                missing_files.append(out_file)

    print('>>> Currently missing:', ', '.join(missing_files))

if __name__ == '__main__':

    compare_files('./projects/01')