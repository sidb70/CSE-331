#!/bin/bash

#len
python3.9 -m unittest tests.CircularDequeTests.test_len
if [ $? -ne 1 ]
then
   echo "test_len passes. "
  
else
  echo "test_len fails. "
  
fi
#test_is_empty
python3.9 -m unittest tests.CircularDequeTests.test_is_empty
if [ $? -ne 1 ]
then
   echo "test_is_empty passes."
   
else
  echo "test_is_empty fails ."
fi

#test_front_element
python3.9 -m unittest tests.CircularDequeTests.test_front_element
if [ $? -ne 1 ]
then
   echo "test_front_element passes."
   
else
  echo "test_front_element fails."
fi


#test_back_element
python3.9 -m unittest tests.CircularDequeTests.test_back_element
if [ $? -ne 1 ]
then
   echo "test_back_element passes."
   
else
  echo "test_back_element fails."
fi

#test_grow
python3.9 -m unittest tests.CircularDequeTests.test_grow
if [ $? -ne 1 ]
then
   echo "test_grow passes."
   
else
  echo "test_grow fails."
fi


#test_shrink
python3.9 -m unittest tests.CircularDequeTests.test_shrink
if [ $? -ne 1 ]
then
   echo "test_shrink passes."
   
else
  echo "test_shrink fails."
fi

#test_front_enqueue_basic
python3.9 -m unittest tests.CircularDequeTests.test_front_enqueue_basic
if [ $? -ne 1 ]
then
   echo "test_front_enqueue_basic passes."
   
else
  echo "test_front_enqueue_basic fails."
fi

#test_back_enqueue_basic
python3.9 -m unittest tests.CircularDequeTests.test_back_enqueue_basic
if [ $? -ne 1 ]
then
   echo "test_back_enqueue_basic passes."
   
else
  echo "test_back_enqueue_basic fails."
fi

#test_front_enqueue
python3.9 -m unittest tests.CircularDequeTests.test_front_enqueue
if [ $? -ne 1 ]
then
   echo "test_front_enqueue passes."
   
else
  echo "test_front_enqueue fails."
fi


#test_back_enqueue
python3.9 -m unittest tests.CircularDequeTests.test_back_enqueue
if [ $? -ne 1 ]
then
   echo "test_back_enqueue passes."
   
else
  echo "test_back_enqueue fails."
fi

#test_front_dequeue_basic
python3.9 -m unittest tests.CircularDequeTests.test_front_dequeue_basic
if [ $? -ne 1 ]
then
   echo "test_front_dequeue_basic passes."
   
else
  echo "test_front_dequeue_basic fails."
fi

#test_back_dequeue_basic
python3.9 -m unittest tests.CircularDequeTests.test_back_dequeue_basic
if [ $? -ne 1 ]
then
   echo "test_back_dequeue_basic passes."
   
else
  echo "test_back_dequeue_basic fails."
fi


#test_back_dequeue
python3.9 -m unittest tests.CircularDequeTests.test_back_dequeue
if [ $? -ne 1 ]
then
   echo "test_back_dequeue passes."
   
else
  echo "test_back_dequeue fails."
fi


#test_front_dequeue
python3.9 -m unittest tests.CircularDequeTests.test_front_dequeue
if [ $? -ne 1 ]
then
   echo "test_front_dequeue passes."
   
else
  echo "test_front_dequeue fails."
fi


#test_application
python3.9 -m unittest tests.CircularDequeTests.test_application
if [ $? -ne 1 ]
then
   echo "test_application passes."
   
else
  echo "test_application fails."
fi





