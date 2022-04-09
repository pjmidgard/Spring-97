                                    Spin=0

                                    ei=0

                                    while ei<=lenf6:
                                            number_predict=Equal_info_between_of_the_cirlce_of_the_file2[ei:ei+8]
                                            
                                            

                                            if number_predict[0:1]!="1" and Spin==0:
                                                    Equal_info_between_of_the_cirlce_of_the_file_11=Equal_info_between_of_the_cirlce_of_the_file_11+number_predict


                                            else:
                                                    number_predict1="0"+number_predict[2:8]
                                                    if number_predict1[0:2]=="01":
                                                            Spin==1
                                                            
                                                            number_predict1="00"+number_predict[2:8]
                                                                    
                                                    Equal_info_between_of_the_cirlce_of_the_file_11=Equal_info_between_of_the_cirlce_of_the_file_11+number_predict1
                                                    
                                            ei=ei+8
