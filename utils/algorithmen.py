def insertion_sort(liste):
    """Sortiert eine Liste mit Insertion Sort — O(n²)"""
    liste = liste.copy()
    for i in range(1, len(liste)):
        schluessel = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > schluessel:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = schluessel
    return liste


def quicksort(liste):
    """Sortiert eine Liste mit Quicksort — O(n log n)"""
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste) // 2]
    links  = [x for x in liste if x < pivot]
    mitte  = [x for x in liste if x == pivot]
    rechts = [x for x in liste if x > pivot]
    return quicksort(links) + mitte + quicksort(rechts)


# Test
if __name__ == "__main__":
    test = [5, 2, 8, 1, 9, 3]
    print("Original:       ", test)
    print("Insertion Sort: ", insertion_sort(test))
    print("Quicksort:      ", quicksort(test))
    print("Python sorted(): ", sorted(test))
