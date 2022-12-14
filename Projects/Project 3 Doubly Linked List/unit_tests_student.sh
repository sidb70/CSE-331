#!/bin/bash

#empty
python3.9 -m unittest tests.DLLTests.test_empty
if [ $? -ne 1 ]
then
   echo "Successful test_empty +5 points "
   
else
  echo "Failed test_empty -5 points"
  
fi
#push
python3.9 -m unittest tests.DLLTests.test_push
if [ $? -ne 1 ]
then
   echo "Successful test_push +5 points"
   
else
  echo "Failed on test_push -5 points"
fi

#test_pop
python3.9 -m unittest tests.DLLTests.test_pop
if [ $? -ne 1 ]
then
   echo "Successful test_pop +5 points"
   
else
  echo "Failed on test_pop -5 points"
fi


#test_list_to_dll
python3.9 -m unittest tests.DLLTests.test_list_to_dll
if [ $? -ne 1 ]
then
   echo "Successful test_list_to_dll +5 points"
   
else
  echo "Failed on test_list_to_dll -5 points"
fi

#test_dll_to_list
python3.9 -m unittest tests.DLLTests.test_dll_to_list
if [ $? -ne 1 ]
then
   echo "Successful test_dll_to_list +5 points"
   
else
  echo "Failed on test_dll_to_list -5 points"
fi


#test_find
python3.9 -m unittest tests.DLLTests.test_find
if [ $? -ne 1 ]
then
   echo "Successful test_find +7 points +"
   
else
  echo "Failed on test_find -7 points"
fi

#test_find_all
python3.9 -m unittest tests.DLLTests.test_find_all
if [ $? -ne 1 ]
then
   echo "Successful test_find_all  +7 points"
   
else
  echo "Failed on test_find_all  -7 points"
fi


#test_remove
python3.9 -m unittest tests.DLLTests.test_remove
if [ $? -ne 1 ]
then
   echo "Successful test_remove +7 points"
   
else
  echo "Failed on test_remove -7 points"
fi



#test_remove_all
python3.9 -m unittest tests.DLLTests.test_remove_all
if [ $? -ne 1 ]
then
   echo "Successful test_remove_all +7 points"
   
else
  echo "Failed on test_remove_all -7 points"
fi


#test_reverse
python3.9 -m unittest tests.DLLTests.test_reverse
if [ $? -ne 1 ]
then
   echo "Successful test_reverse +7 points"
   
else
  echo "Failed on test_reverse -7 points"
fi



#test_application
python3.9 -m unittest tests.DLLTests.test_application
if [ $? -ne 1 ]
then
   echo "Successful test_application +10 points"
   
else
  echo "Failed on test_application -10 points"
fi









