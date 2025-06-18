# 📊 Habit Tracker Generator

أداة ذكية وسهلة الاستخدام لتوليد تقارير تتبع العادات اليومية باستخدام ملفات CSV وقالب Jinja2.

---

## ⚙️ الوظيفة الأساسية

يقوم هذا المشروع بقراءة ملفين:
- `habits.csv`: يحتوي على معلومات العادات الشخصية (مثل العادات والأشهر).
- `daily_tracker.csv`: يحتوي على تتبع يومي لتلك العادات.

ثم يستخدم قالب `habit_tracker_template.txt` لتوليد تقرير Markdown جذاب يحتوي على بيانات التتبع اليومية بشكل منظم.

---

## 📁 بنية الملفات

```
📂 المشروع
│
├── main.py                        # الكود الأساسي لتوليد التقرير
├── habits.csv                    # نموذج بيانات العادات (مدخل)
├── daily_tracker.csv            # نموذج تتبع يومي (مدخل)
├── habit_tracker_template.txt   # قالب Jinja2 للتقرير
├── habit_tracker_output.md      # الناتج النهائي (تقرير Markdown)
└── README.md                    # ملف التوثيق (أنت تقرأه الآن)
```

---

## ✅ كيفية الاستخدام

1. تأكد من وجود الملفات التالية في نفس المجلد:
   - `habits.csv`
   - `daily_tracker.csv`
   - `habit_tracker_template.txt`

2. شغّل الملف `main.py`:

```bash
python main.py
```

3. سيتم إنشاء تقرير باسم `habit_tracker_output.md`.

---

## 📝 ملاحظات هامة

- يجب أن يحتوي `habits.csv` على عمود باسم `month`.
- يجب أن يحتوي `daily_tracker.csv` على الأعمدة التالية:  
  `date`, `habit1`, `habit2`, `habit3`, `notes`
- في حالة وجود بيانات ناقصة أو تنسيق غير صحيح، سيتم عرض رسائل خطأ توضيحية.

---

## 🌟 مثال عملي

```csv
# habits.csv
month,habit1,habit2,habit3
June,Reading,Meditation,Workout

# daily_tracker.csv
date,habit1,habit2,habit3,notes
2025-06-01,✔️,❌,✔️,Good start
2025-06-02,✔️,✔️,❌,Need more focus
```

---

## 🧰 المتطلبات

- Python 3.7+
- المكتبات:
  - `pandas`
  - `jinja2`

لتثبيتها:

```bash
pip install pandas jinja2
```

---

## 🧠 الفائدة من الأداة

هذه الأداة مثالية لرواد الإنتاجية، والطلاب، والمدربين، وكل من يسعى لمتابعة عاداته اليومية بطريقة منظمة وتلقائية، مع إمكانية تعديل القالب ليظهر التقرير بشكل شخصي واحترافي.

---

## ✨ الترخيص

مشروع مفتوح المصدر لاستخدامك الشخصي أو التجاري. يمكنك تعديله بحرية.
