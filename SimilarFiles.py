import os

def similarFiles(folder: str):
    files = []
    for file in os.listdir(folder):
        if os.path.isfile(file):
            files.append(file)
    for file in files:
        for file2 in files:
            if file == file2:
                continue
            similar_chars = 0
            with open(file, 'r') as f:
                f1 = f.read()
            with open(file2, 'r') as f2:
                f2 = f2.read()
            if f1 == f2:
                print(f"{file}/{file2}: 100%")
                continue
            if len(f1) > len(f2):
                for char in f1:
                    if char in f2:
                        similar_chars += 1
                if similar_chars != 0:
                    print(f"{file}/{file2}: {round(similar_chars / len(f1) * 100, 2)}%")
                else:
                    print(f"{file}/{file2}: 0%")
            else:
                for char in f2:
                    if char in f1:
                        similar_chars += 1
                if similar_chars != 0:
                    print(f"{file}/{file2}: {round(similar_chars / len(f2) * 100, 2)}%")
                else:
                    print(f"{file}/{file2}: 0%")

if __name__ == '__main__':
    similarFiles(os.getcwd())