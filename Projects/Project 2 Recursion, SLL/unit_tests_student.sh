#!/bin/bash


python3.9 -m unittest tests.MyTestCase.test_to_string
if [ $? -ne 1 ]
then
   echo "Successful to_string"
   
else
  echo "Failed on to_string"
  
fi
#Length
python3.9 -m unittest tests.MyTestCase.test_length
if [ $? -ne 1 ]
then
   echo "Successful test_length"
   
else
  echo "Failed on test_length"
fi

#sum_list
python3.9 -m unittest tests.MyTestCase.test_sum_list
if [ $? -ne 1 ]
then
   echo "Successful test_sum_list"
   
else
  echo "Failed on test_sum_list"
fi


#test_push
python3.9 -m unittest tests.MyTestCase.test_push
if [ $? -ne 1 ]
then
   echo "Successful test_push"
   
else
  echo "Failed on test_push"
fi

#test_remove
python3.9 -m unittest tests.MyTestCase.test_remove
if [ $? -ne 1 ]
then
   echo "Successful test_remove"
   
else
  echo "Failed on test_remove"
fi


#test_remove_all
python3.9 -m unittest tests.MyTestCase.test_remove_all
if [ $? -ne 1 ]
then
   echo "Successful test_remove_all"
   
else
  echo "Failed on test_remove_all"
fi

#test_search
python3.9 -m unittest tests.MyTestCase.test_search
if [ $? -ne 1 ]
then
   echo "Successful test_search"
   
else
  echo "Failed on test_search"
fi


##test_count
python3.9 -m unittest tests.MyTestCase.test_count
if [ $? -ne 1 ]
then
   echo "Successful test_count"
   
else
  echo "Failed on test_count"
fi



##test_reverse
python3.9 -m unittest tests.MyTestCase.test_reverse
if [ $? -ne 1 ]
then
   echo "Successful test_reverse"
   
else
  echo "Failed on test_reverse"
fi









