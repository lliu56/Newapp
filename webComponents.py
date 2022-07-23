
from psutil import getloadavg
import streamlit as st 
# from summary_page import getSummary
# from InputTextFile import TextModule
from time import sleep


## class sfxn##

class websiteComponents ():
    ## init fxn##
    
    def __init__ (self,pageName):
        self.pageName =pageName
        self.title = st.title
        self.write = st.write
        self.selectBox = st.selectbox
        self.textArea = st.text_area
        self.selectButton = st.button
        self.Container = st.container
    
        

        # self.types = types 
        # self.sButton = sButton 
        # self.text_area  = self.st.text_area (self.label, value="", height=None, \
        #                              max_chars=None, key=None, help=None, \
        #                              on_change=None, args=None, kwargs=None, \
        #                              placeholder=None, disabled=False)
    # not sure if i initiated this properly lmao 

    ### Heading ### 
    def showSummaryPage(self):
        self.title ('PEGASUS Text Summarization ')
        # self.write ("""### Enter/Paste your text here """)                 # writing text on page(can use markdaown syntax like in html)


    ### Selection box section ###

    def putSelectBox (self):
        modelType = ('Short Summary (xsum)','Long Summary (Large)')
        typesOfModel =  self.selectBox ("Summary Models", modelType,key='Select Box')
        return typesOfModel

    ##input box ## 
    def getInputText(self,label ='Input Box',placeholder='Type/Paste Text Here...' ):
        inputText = self.textArea(label,placeholder)
        return inputText


        
    ## botton press and running code 

    def buttonPress(self):
        sButton= self.selectButton ("Summarize",'Summarize Button')        # if not clicked then sBotton is false , vice versa 
        # if sButton is True:                          # run summary code if button is pressed 
        #     summary = str (getSummary())
        # return summary 
        return sButton
       
            
    ## outputbox fxn###
    def outputText(self,text):
        with self.Container ():
            self.write (text)






# #dummy code to see if it runs 
# def main ():                                             
#     waitText = 'Running Summary Model...'
#     webComponents = websiteComponents
#     webComponents.getLoadingSpinner (waitText)

# if __name__ == '__main__':
#     main()
