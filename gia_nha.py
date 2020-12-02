import csv
import matplotlib.pyplot as plt


with open('gianha.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow([30, 448.524])
    writer.writerow([32.4138, 509.248])
    writer.writerow([34.8276, 535.104])
    writer.writerow([37.2414, 551.432])
    writer.writerow([39.6552, 623.418])
    writer.writerow([42.069, 625.992])
    writer.writerow([44.4828, 655.248])
    writer.writerow([46.8966, 701.377])
    writer.writerow([49.3103, 748.918])
    writer.writerow([51.7241, 757.881])
    writer.writerow([54.1739, 831.004])
    writer.writerow([56.5517, 855.409])
    writer.writerow([58.9655, 866.707])


dien_tich = []
gia = []
with open('gianha.csv', mode='r') as file:
    plots = csv.reader(file, delimiter=',')
    for row in plots:

        dien_tich.append(float(row[0]))
        gia.append(float(row[1]))


plt.plot(dien_tich, gia, label = 'S_fee')
plt.xlabel("diện tích")
plt.ylabel("giá nhà")
plt.title('Đồ thị quan hệ diện tích _ giá nhà')
# plt.legend()
plt.show()
