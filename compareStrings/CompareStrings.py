import csv

def percentage(part,whole):
    return 100 * float(part) / float(whole)

wav_csv = open("wav_out_clear.csv")
dedect_csv = open("wav_out_noisy.csv")

wav_reader = csv.reader(wav_csv)
dedect_reader = csv.reader(dedect_csv)

wav_header = next(wav_reader)
dedect_header = next(dedect_csv)
dedect_split = dedect_header.split(',')


print(dedect_split)
print(wav_header)

compared_array = []
true_number = 0

if(len(dedect_split) != len(wav_header)):
        print("lenght is not equal")
else:
    for i in range(0, len(dedect_split)-1):
        if(dedect_split[i] == wav_header[i]):
            compared_array.append('true')
            true_number += 1
        else:
            compared_array.append('false')
    print(compared_array)
    print("%",percentage(true_number,(len(dedect_split)-1)), "true ")


