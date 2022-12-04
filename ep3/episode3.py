import pandas as pd
import matplotlib.pyplot as plt


group_faculty = []
group_out = []

data = pd.read_excel(r'students_info.xlsx', engine='openpyxl')
grades = pd.read_html(r'results_ejudge.html',header=0)


faculty = data['group_faculty'].unique()
out = data['group_out'].unique()

for i in faculty:
    group = data.loc[data["group_faculty"] == i]
    group_faculty.append(group)

for i in out:
    group = data.loc[data["group_out"] == i]
    group_out.append(group)

scores_faculty = []
scores_out = []
students_map = {}
for group in group_faculty:
    middle_grade = 0
    keys = group["login"].unique()
    for key in keys:
        if isinstance(key, str):
            score = grades[0].loc[(grades[0])["User"] == key, "Solved"].iloc[0]
            middle_grade += score
            G = grades[0].loc[(grades[0])["User"] == key, "G"].iloc[0]
            H = grades[0].loc[(grades[0])["User"] == key, "H"].iloc[0]
            if G > 1 or H > 1:
                students_map[key] = [group.loc[group["login"] == key, "group_faculty"].iloc[0],
                group.loc[group["login"] == key, "group_out"].iloc[0]]
        middle_grade /= len(group)
    scores_faculty.append(middle_grade)

for group in group_out:
    middle_grade = 0
    keys = group["login"].unique()
    for key in keys:
        if isinstance(key, str):
            score = grades[0].loc[(grades[0])["User"] == key, "Solved"].iloc[0]
            middle_grade += score
        middle_grade /= len(group)
    scores_out.append(middle_grade)

y1 = data["group_faculty"].unique()
y2 = data["group_out"].unique()

df1 = pd.DataFrame({"Faculty groups": scores_faculty}, index=y1)
df2 = pd.DataFrame({"Informatics groups" : scores_out}, index=y2)

ax1 = df1.plot.bar(rot=0)
plt.title("Mean of solved problems")
plt.savefig("faculty.png")
ax2 = df2.plot.bar(rot=0)
plt.title("Mean of solved problems")
plt.savefig("out.png")

print("Students who passed more than one test in one or both of the two last problems:")
for key in students_map:
    print("Login:", key,  "Group faculty:", students_map[key][0], "Group out:", students_map[key][1])
print("Number of students:" , len(students_map))
