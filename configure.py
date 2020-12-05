#Here we put plot configurations
target_lumi = 35.9  #fb^{-1}

#gamma Pt bins
gPtBins  = array('d', [float(x) for x in range(60,85,25)\
                                        +range(85,105,20)\
                                        +range(105,130,25)\
                                        +range(130,190,60)\
                                        +range(190,220,30)\
                                        +range(220,250,30)\
                                        +range(250,300,50)\
                                        +range(300,350,50)\
                                        +range(350,400,50)\
                                        +range(400,500,100)\
                                        +range(500,700,200)\
                                        +range(700,1000,300)\
                                        ])


