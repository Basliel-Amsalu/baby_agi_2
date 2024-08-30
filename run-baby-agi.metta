! (import! &self babyagi)
 ;run sentiment analyzer
! (sntmnt "I am very happy with your service, but a bit concerned about the delivery time.")
 ;run response generator
! (rspgen "{\"compound\": 0.2, \"pos\": 0.5, \"neu\": 0.4, \"neg\": 0.1}")
 ; ! (rspgen (sntmnt "I am very happy with your service, but a bit concerned about the delivery time."))
 ;; Add sentiment analysis and response to running space
! (add-reduct &self (sntmnt "This is a challenging situation."))
! (add-reduct &self (rspgen "{\"compound\": -0.3, \"pos\": 0.1, \"neu\": 0.3, \"neg\": 0.6}"))

 ;; Retrieve all knowledge present in the running space
! (match &self $x $x)