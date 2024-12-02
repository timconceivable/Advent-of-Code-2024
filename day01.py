# ADVENT OF CODE 2024 - DAY 1

def input_to_sorted_lists(filename):
  file = open(filename)
  data_list = file.read()
  file.close()
  data_list = list(map(int, data_list.split()))
  list1, list2 = [], []
  for i in range(len(data_list)):
    if i % 2 == 0:
      list1.append(data_list[i])
    else:
      list2.append(data_list[i])
  return sorted(list1), sorted(list2)


def get_total_distance(list1, list2):
  result = 0
  for i in range(len(list1)):
      result += abs(list1[i] - list2[i])
  return result


def get_similarity_score(list1, list2):
  result = 0
  for i in list1:
    result += list2.count(i)*i
  return result

def main():
  list1, list2 = input_to_sorted_lists(r'day01-input.txt')
  # PART ONE
  print(get_total_distance(list1, list2))
  # PART TWO
  print(get_similarity_score(list1,list2))


if __name__ == "__main__":
  main()