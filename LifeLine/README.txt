All the patients who suffered heart attacks at some point in the past are still alive and some are not. 
The problem addressed by past researchers was to predict from the other variables whether or not the patient will survive at least one year. The most difficult part of this problem is correctly predicting that the patient will NOT survive.
Therefore LifeLine takes several inputs like(Days that patient has already survived , age , pericardial effusion , fraction shortening , E-Point septal separation, Left ventricular end-diastolic dimension etc.) and classifies if patients requires special observation/care in the following one year of heart attack using k-nearest neighbors (KNN) algorithm which is a supervised machine learning algorithm.
The KNN algorithm assumes that similar things exist in close proximity. In other words, similar things are near to each other.
We first split the training data in ratio of 75 : 25 where the 75% was training data with corresponding labels and remaining 25% was test data without labels. 
The Algorithm used the training data to predict the test data’s appropriate labels. 
The Algorithm was required to predict the labels(status)of the remaining 25% data and the labels of this data were stored separately in order to check the accuracy of the algorithm
Once the algorithm provided labels to all the data-points they  were compared with actual labels for those data points in order predict how accurately the algorithm predicted the labels of test data.
Our Software’s Algorithm performed positively and gave an outstanding Test Score of 92% over the Training Set
Information regarding dataset :
  -- All the patients suffered heart attacks at some point in the past.
     Some are still alive and some are not.  The survival and still-alive
     variables, when taken together, indicate whether a patient survived
     for at least one year following the heart attack.  

     The problem addressed by past researchers was to predict from the 
     other variables whether or not the patient will survive at least
     one year.  The most difficult part of this problem is correctly
     predicting that the patient will NOT survive.  (Part of the difficulty
     seems to be the size of the data set.)

Number of Instances: 132

Number of Attributes: 13 (all numeric-valued)

Attribute Information:
   1. survival -- the number of months patient survived (has survived,
                  if patient is still alive).  Because all the patients
                  had their heart attacks at different times, it is 
                  possible that some patients have survived less than
                  one year but they are still alive.  Check the second
                  variable to confirm this.  Such patients cannot be 
                  used for the prediction task mentioned above.
 
   2. age-at-heart-attack -- age in years when heart attack occurred

   3. pericardial-effusion -- binary. Pericardial effusion is fluid
                              around the heart.  0=no fluid, 1=fluid
   4. fractional-shortening -- a measure of contracility around the heart
                               lower numbers are increasingly abnormal
   5. epss -- E-point septal separation, another measure of contractility.  
              Larger numbers are increasingly abnormal.
   6. lvdd -- left ventricular end-diastolic dimension.  This is
              a measure of the size of the heart at end-diastole.
              Large hearts tend to be sick hearts.
   7. wall-motion-score -- a measure of how the segments of the left
                           ventricle are moving
   8. wall-motion-index -- equals wall-motion-score divided b