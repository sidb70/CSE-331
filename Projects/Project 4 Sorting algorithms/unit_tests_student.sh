#!/bin/bash

#selection sort
python3.9 -m unittest tests.Project4Tests.test_selection_sort
if [ $? -ne 1 ]
then
   echo "Successful test_selection_sort +2 points "
   
else
  echo "Failed test_empty -2 points"
  
fi
#test_selection_comparator
python3.9 -m unittest tests.Project4Tests.test_selection_comparator
if [ $? -ne 1 ]
then
   echo "Successful test_selection_comparator +4 points"
  
else
  echo "Failed on test_selection_comparator -4 points"
fi

#test_selection_descending
python3.9 -m unittest tests.Project4Tests.test_selection_descending
if [ $? -ne 1 ]
then
   echo "Successful test_selection_descending +4 points"
   
else
  echo "Failed on test_selection_descending -4 points"
fi


#test_bubble_sort
python3.9 -m unittest tests.Project4Tests.test_bubble_sort
if [ $? -ne 1 ]
then
   echo "Successful test_bubble_sort +2 points"
   
else
  echo "Failed on test_bubble_sort -2 points"
fi

#test_bubble_comparator
python3.9 -m unittest tests.Project4Tests.test_bubble_comparator
if [ $? -ne 1 ]
then
   echo "Successful test_bubble_comparator +4 points"
   
else
  echo "Failed on test_bubble_comparator -4 points"
fi


#test_bubble_descending
python3.9 -m unittest tests.Project4Tests.test_bubble_descending
if [ $? -ne 1 ]
then
   echo "Successful test_bubble_descending +4 points +"
   
else
  echo "Failed on test_bubble_descending -4 points"
fi

#test_insertion_sort
python3.9 -m unittest tests.Project4Tests.test_insertion_sort
if [ $? -ne 1 ]
then
   echo "Successful test_insertion_sort  +2 points"
   
else
  echo "Failed on test_insertion_sort  -2 points"
fi


#test_insertion_comparator
python3.9 -m unittest tests.Project4Tests.test_insertion_comparator
if [ $? -ne 1 ]
then
   echo "Successful test_insertion_comparator +4 points"
   
else
  echo "Failed on test_insertion_comparator -4 points"
fi



#test_insertion_descending
python3.9 -m unittest tests.Project4Tests.test_insertion_descending
if [ $? -ne 1 ]
then
   echo "Successful test_insertion_descending +4 points"
   
else
  echo "Failed on test_insertion_descending -4 points"
fi


#test_hybrid_merge_sort
python3.9 -m unittest tests.Project4Tests.test_hybrid_merge_sort
if [ $? -ne 1 ]
then
   echo "Successful test_hybrid_merge_sort +4 points"
   
else
  echo "Failed on test_hybrid_merge_sort -4 points"
fi



#test_hybrid_merge_comparator
python3.9 -m unittest tests.Project4Tests.test_hybrid_merge_comparator
if [ $? -ne 1 ]
then
   echo "Successful test_hybrid_merge_comparator +8 points"
   
else
  echo "Failed on test_hybrid_merge_comparator -8 points"
fi



#test_hybrid_merge_descending
python3.9 -m unittest tests.Project4Tests.test_hybrid_merge_descending
if [ $? -ne 1 ]
then
   echo "Successful test_hybrid_merge_descending +8 points"
   
else
  echo "Failed on test_hybrid_merge_descending -8 points"
fi


#test_sort_sushi
python3.9 -m unittest tests.Project4Tests.test_sort_sushi
if [ $? -ne 1 ]
then
   echo "Successful test_sort_sushi +20 points"
   
else
  echo "Failed on test_sort_sushi -20 points"
fi














