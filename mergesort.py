import matplotlib.pyplot as plt

# Sortieren einer Liste durch Merchsort
def mergeSort(arr):
    # Wenn mehr als ein Element in der Liste ist
    if len(arr) > 1:
        # Mitte der Liste
        mid = len(arr) // 2
        
        # Liste in zwei Hälften teilen
        left = arr[:mid]
        right = arr[mid:]

        # Rekursives Sortieren der Hälften
        mergeSort(left)
        mergeSort(right)

        l = r = i = 0

        # Elemente aus left und right sortiert zusammenführen
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1

        # Übrige Elemente aus left einfügen (falls vorhanden)
        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1

        # Übrige Elemente aus right einfügen (falls vorhanden)
        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1

# Liste zum durchlaufen
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
original = my_list.copy()

# Liste vor dem Sortieren visualisieren
plt.figure(figsize=(10, 4))
plt.bar(range(len(original)), original, color='skyblue')
plt.title("Vor dem Sortieren")
plt.xlabel("Index")
plt.ylabel("Wert")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# mergeSort aufrufen
mergeSort(my_list)

# Liste nach dem Sortieren visualisieren
plt.figure(figsize=(10, 4))
plt.bar(range(len(my_list)), my_list, color='lightgreen')
plt.title("Nach dem Sortieren")
plt.xlabel("Index")
plt.ylabel("Wert")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
