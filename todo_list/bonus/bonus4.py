filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

for i, filename in enumerate(filenames):
    filename = filename.replace('.', '-', 1)
    filenames[i] = filename

print(filenames)