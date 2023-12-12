"""
Please write your name
@author: Miles Blackwood

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath) -> None:
        try:
            with open(filepath, "r") as file:
                data = csv.reader(file)
                self.headers = next(data)
                self.records = list(data)
        except FileNotFoundError:
            raise FileNotFoundError("FIle not found")

    def get_dimension(self) -> list:
        print([len(self.headers), len(self.records)])
        

    def web_summary(self, filepath: str) -> None:
        headerArray = []
        totalArrayPosYes = []
        totalPosYes = 0
        totalArrayPosNo = []
        totalPosNo = 0
        totalArrayNegYes = []
        totalNegYes = 0
        totalArrayNegNo = []
        totalNegNo = 0
        for i in range(len(self.headers)):
            if self.headers[i] == "Age" or self.headers[i] == "Gender" or self.headers[i] == "class":
                next
            for record in self.records:
                if record[16] == "Positive":
                    if record[i] == "Yes":
                        totalPosYes += 1
                    else:
                        totalPosNo += 1
                
                if record[16] == "Negative":
                    if record[i] == "Yes":
                        totalNegYes += 1
                    else:
                        totalNegNo += 1
            headerArray.append(self.headers[i])
            totalArrayPosYes.append(totalPosYes)
            totalArrayNegYes.append(totalNegYes)
            totalArrayPosNo.append(totalPosNo)
            totalArrayNegNo.append(totalNegNo)
            totalPosYes = 0
            totalNegYes = 0
            totalPosNo = 0
            totalNegNo = 0
        try:
            with open(filepath, "w") as file:
                i = 0
                file.write("<!DOCTYPE html>\n")
                file.write("<html>\n")
                file.write("<head>\n")
                file.write("<style>\n")
                file.write("table, th, td {\n")
                file.write("border: 1px solid black;\n")
                file.write("border-collapse: collapse;}\n")
                file.write("</style>\n")
                file.write("<body>\n")
                file.write("""<table style="width:100%">\n""")
                file.write("<tr>\n")
                file.write("""<th rowspan="3">Attributes</th>\n""")
                file.write("""<th colspan="4">Class</th>\n""")
                file.write("</tr>\n")
                file.write("<tr>\n")
                file.write("""<th colspan="2">Positive</th>\n""")
                file.write("""<th colspan="2">Negative</th>\n""")
                file.write("</tr>\n")
                file.write("<tr>\n")
                file.write("<td>Yes</td>\n")
                file.write("<td>No</td>\n")
                file.write("<td>Yes</td>\n")
                file.write("<td>No</td>\n")
                file.write("</tr>\n")
                for header in headerArray:
                    file.write("<tr>\n")
                    file.write(f"<td>{header}</td>\n")
                    file.write(f"<td>{totalArrayPosYes[i]}</td>\n")
                    file.write(f"<td>{totalArrayPosNo[i]}</td>\n")
                    file.write(f"<td>{totalArrayNegYes[i]}</td>\n")
                    file.write(f"<td>{totalArrayNegNo[i]}</td>\n")
                    file.write("</tr>\n")
                    i += 1
                file.write("</table>\n")
                file.write("</body>\n")
                file.write("</html>")
        except FileNotFoundError:
            raise FileNotFoundError("file not Found")


    def count_instances(self, criteria) -> int:
        # delete pass and this line to write your code
        # you can change the parameter criteria or the number of parameters
        # as you want, provided they are explained in doctring for this
        # method
        pass


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    # d1.count_instances() # change according to your criteria
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    # d2.count_instances()  # change according to your criteria
