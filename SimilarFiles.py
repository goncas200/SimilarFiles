import os

def similarFiles(folder: str):
    files = []
    files_iterated = []
    percentage = 0
    os.chdir(folder)
    for file in os.listdir(folder):
        if os.path.isfile(file):
            files.append(file)
    for file in files:
        for file2 in files:
            if file2 in files_iterated:
                continue
            if file not in files_iterated:
                files_iterated.append(file)
            if file == file2:
                continue
            similar_chars = 0
            with open(file, 'r') as f:
                try:
                    f1 = f.read()
                except UnicodeDecodeError:
                    print(f"Couldn't decode file {file}")
            with open(file2, 'r') as f2:
                try:
                    f1 = f.read()
                except UnicodeDecodeError:
                    print(f"Couldn't decode file {file2}")
            if f1 == f2:
                percentage = 100
                print(f"{file}/{file2}: {percentage}% similar")
                print(f"Files {file} and {file2} are really similar")
                answer = input("Do you want to delete one of them? [Y/n]: ")
                if answer.lower() == 'y' or answer.lower() == 'yes' or answer == '':
                    if len(f1) > len(f2):
                        os.remove(file)
                        print(f"{file} removed")
                        files.remove(file)
                    else:
                        os.remove(file2)
                        print(f"{file2} removed")
                        files.remove(file2)
                continue
            if len(f1) > len(f2):
                for char in f1:
                    if char in f2:
                        similar_chars += 1
                if similar_chars != 0:
                    percentage = round(similar_chars / len(f1) * 100, 2)
                    print(f"{file}/{file2}: {percentage}% similar")
                else:
                    percentage = 0
                    print(f"{file}/{file2}: {percentage}%")
            else:
                for char in f2:
                    if char in f1:
                        similar_chars += 1
                if similar_chars != 0:
                    percentage = round(similar_chars / len(f2) * 100, 2)
                    print(f"{file}/{file2}: {percentage}% similar")
                else:
                    percentage = 0
                    print(f"{file}/{file2}: {percentage}%")
            if percentage > 90:
                print(f"Files {file} and {file2} are really similar")
                answer = input("Do you want to delete one of them? [Y/n]: ")
                if answer.lower() == 'y' or answer.lower() == 'yes' or answer == '':
                    if len(f1) > len(f2):
                        os.remove(file)
                        print(f"{file} removed")
                    else:
                        os.remove(file2)
                        print(f"{file2} removed")
if __name__ == '__main__':
    similarFiles(os.getcwd())
        
