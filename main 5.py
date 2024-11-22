def tri_selection(lst):
  for i in range(0, len(lst) - 1):
    mini = i
    for j in range(i + 1, len(lst)):
      if lst[j] < lst[mini]:
        mini = j
    tmp = lst[i]
    lst[i] = lst[mini]
    lst[mini] = tmp

lst = [ 9, 5, 8, 54]
tri_selection(lst)
print(lst)