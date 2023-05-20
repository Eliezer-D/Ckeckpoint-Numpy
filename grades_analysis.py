
import numpy as np

grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Moyenne
mean_grade = np.mean(grades)
print("Moyenne des notes :", mean_grade)

# Médiane
median_grade = np.median(grades)
print("Médiane des notes :", median_grade)

# Écart type
std_grade = np.std(grades)
print("Écart type des notes :", std_grade)

# Maximum et minimum
max_grade = np.max(grades)
min_grade = np.min(grades)
print("Note maximale :", max_grade)
print("Note minimale :", min_grade)

# Trier les notes par ordre croissant
sorted_grades = np.sort(grades)
print("Notes triées par ordre croissant :", sorted_grades)

# Index de la note la plus élevée
max_index = np.argmax(grades)
print("Index de la note la plus élevée :", max_index)

# Nombre d'étudiants avec une note supérieure à 90
num_high_grades = np.sum(grades > 90)
print("Nombre d'étudiants avec une note supérieure à 90 :", num_high_grades)

# Pourcentage d'étudiants avec une note supérieure à 90
percentage_high_grades = np.mean(grades > 90) * 100
print("Pourcentage d'étudiants avec une note supérieure à 90 :", percentage_high_grades)

# Pourcentage d'étudiants avec une note inférieure à 75
percentage_low_grades = np.mean(grades < 75) * 100
print("Pourcentage d'étudiants avec une note inférieure à 75 :", percentage_low_grades)

# Extraction des notes supérieures à 90
high_performers = grades[grades > 90]
print("Notes supérieures à 90 :", high_performers)

# Notes supérieures à 75
passing_grades = grades[grades > 75]
print("Notes supérieures à 75 :", passing_grades)

