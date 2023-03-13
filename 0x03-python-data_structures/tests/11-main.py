#!/usr/bin/python3
  2 delete_at = __import__('11-delete_at').delete_at
  3
  4 my_list = [1, 2, 3, 4, 5]
  5 idx = 3
  6 new_list = delete_at(my_list, idx)
  7 print(new_list)
  8 print(my_list)
