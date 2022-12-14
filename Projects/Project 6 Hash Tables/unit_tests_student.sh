#!/bin/bash

#test_hash
python3.9 -m unittest tests.TestProject1.test_hash





if [ $? -ne 0 ]
then
   echo "test_hash fails "
   
else
   echo "test_hash passes  "
   
  
fi
#test_insert
python3.9 -m unittest tests.TestProject1.test_insert
if [ $? -ne 0 ]
then
   echo "test_insert fails "
   
   
else
   echo "test_insert passes " 
  
fi

#test_get
python3.9 -m unittest tests.TestProject1.test_get
if [ $? -ne 0 ]
then
   echo "test_get fails "
   
else
  echo "test_get passes "
fi


#test_delete
python3.9 -m unittest tests.TestProject1.test_delete
if [ $? -ne 0 ]
then
   echo "test_delete fails "
   
else
  echo "test_delete passes "
fi

#test_len
python3.9 -m unittest tests.TestProject1.test_len
if [ $? -ne 0 ]
then
   echo "test_len fails "
   
else
  echo "test_len passes "
fi


#test_setitem
python3.9 -m unittest tests.TestProject1.test_setitem
if [ $? -ne 0 ]
then
   echo "test_setitem fails "
   
else
  echo "test_setitem passes "
fi

#test_getitem
python3.9 -m unittest tests.TestProject1.test_getitem
if [ $? -ne 0 ]
then
   echo "test_getitem fails "
   
else
  echo "test_getitem passes "
fi

#test_delitem
python3.9 -m unittest tests.TestProject1.test_delitem
if [ $? -ne 0 ]
then
   echo "test_delitem fails "
   
else
  echo "test_delitem passes "
fi

#test_contains
python3.9 -m unittest tests.TestProject1.test_contains
if [ $? -ne 0 ]
then
   echo "test_contains fails "
   
else
  echo "test_contains passes "
fi


#test_update
python3.9 -m unittest tests.TestProject1.test_update
if [ $? -ne 0 ]
then
   echo "test_update fails "
   
else
  echo "test_update passes "
fi

#test_keys_values_items
python3.9 -m unittest tests.TestProject1.test_keys_values_items
if [ $? -ne 0 ]
then
   echo "test_keys_values_items fails "
   
else
  echo "test_keys_values_items passes "
fi

#test_clear
python3.9 -m unittest tests.TestProject1.test_clear
if [ $? -ne 0 ]
then
   echo "test_clear fails "
   
else
  echo "test_clear passes "
fi

#test_setitem_and_delitem
python3.9 -m unittest tests.TestProject1.test_setitem_and_delitem
if [ $? -ne 0 ]
then
   echo "test_setitem_and_delitem fails "
   
else
  echo "test_setitem_and_delitem passes "
fi


#test_display_duplicates
python3.9 -m unittest tests.TestProject1.test_display_duplicates
if [ $? -ne 0 ]
then
   echo "test_display_duplicates fails "
   
else
  echo "test_display_duplicates passes "
fi





