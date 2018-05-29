# keyword
A keyword in context program written in python


Given an input of the form:

  2 
  :: 
  of 
  and 
  the 
  too 
  on 
  who 
  to 
  that 
  :: 
  that fortune 
  sense and sensibility 
  life of robert browning 
  the man who knew too much 
  legend of montrose 
  visit to iceland 
  orthodoxy 
  the mountains 
  on the track 
  ward of king canute


kwic2 takes the input and formats it to look like:

              life of robert BROWNING
                ward of king CANUTE
                        that FORTUNE
                    visit to ICELAND
                     ward of KING canute
                 the man who KNEW too much
                             LEGEND of montrose
                             LIFE of robert browning
                         the MAN who knew too much
                   legend of MONTROSE
                         the MOUNTAINS
            man who knew too MUCH
                             ORTHODOXY
                     life of ROBERT browning
                             SENSE and sensibility
                   sense and SENSIBILITY
                      on the TRACK
                             VISIT to iceland
                             WARD of king canute
                             
the input is a list of words to be excluded (not get capitalized) and a list of sentences, kwic2 finds and capitalizes the keywords, and the output is formatted in a way where the keyword starts at column 30. the formatted output is sorted alphabetically by the keywords.
