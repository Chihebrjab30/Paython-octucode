import random

# خلي الشخص يدخل الأسماء مفصولة بمسافة
names_string = input("أدخل أسماء الأشخاص الذين سيتعشون معك (افصل بينهم بمسافة): ")

# نفصل الأسماء ونحولها لقائمة
names = names_string.split(",")

# نختار رقم عشوائي من 0 لآخر فهرس
index = random.randint(0, len(names)-1)

# نجيب الاسم حسب الرقم
payer = names[index]

print(payer, "هو اللي رح يدفع العشاء اليوم 🍽️😂")