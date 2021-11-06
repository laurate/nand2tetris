#######################################################################################################

import os

#######################################################################################################

def compare_files(directory):

    for file in os.listdir(directory):

        if file.endswith('.out'):
            out_file = file
            cmp_file = os.path.basename(file).replace('.out', '.cmp')

            print(f'Comparing {cmp_file} and {out_file} at {directory}...')

            with open(os.path.join(directory, out_file)) as f_1:
                out_file_content = f_1.readlines()

            with open(os.path.join(directory, cmp_file)) as f_2:
                cmp_file_content = f_2.readlines()

            if out_file_content == cmp_file_content:
                print('✅ Files are equal')
            else:
                print('⛔️ Files are not equal')

if __name__ == '__main__':

    compare_files('./projects/01')