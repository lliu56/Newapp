### import relavant modules ###
##website##
from lib2to3.pgen2 import token
from typing_extensions import runtime
from prometheus_client import Summary
import webComponents as wc
import streamlit as st 
import summary_page as sp
# import time
import tqdm
# from MarkDownModule import htmlMarkDown


# from multiprocessing import Process             # parallel running
# from InputTextFile import TextModules

##Summary##
from transformers import PegasusForConditionalGeneration,PegasusTokenizer
global y

tokenizer = []

### run website code###

# running the the show summary page and select box
website = wc.websiteComponents('Pegasus Text Summary')
target=website.showSummaryPage ()


## putting select box
selectedModel = website.putSelectBox()
# print (selectedModel)

#loading the rests of the components
text = website.getInputText()

## selecting models 
modelType = ('Short Summary (xsum)','Long Summary (Large)')

#loading models 
[xsumTokenizer , largeTokenizer] = sp.loadTokenizer()
[xsumModel, largeModel]= sp.loadModel()


### select tokenizer and model based on user dropbox
if selectedModel == modelType[0]:
    tokenizer= xsumTokenizer
    model = xsumModel
if selectedModel == modelType[1]:
    tokenizer = largeTokenizer
    model = largeModel
# print (tokenizer,model)



##generate tokins##
tokens = tokenizer (text,truncation = True, 
                    padding = 'longest', return_tensors='pt')





#defining getSummary() fxn
def getSummary():
    summaryCode = model.generate(**tokens)
    summary = tokenizer.decode (summaryCode[0])
    return summary 

# preparing to run summary code 
buttonPressList = {'Button Pressed': False}
summary = ''

### model code for running a spinner when the code is loading ###3
# running summary code    
sButton = website.buttonPress ()
temp = True
if sButton is True :                             # run summary code if button is pressed
    while temp is True:  
        with st.spinner ('Running Summary Model... '):
            summary = str (getSummary())
        # st.success ('Done')
        temp =False

    ## adding an output summary header 
    st.write ('### Output Summary')

    ## outputting text in a box 
    website.outputText(text=summary)   
    



##streamlit run c:\Users\lihua\PEGASUS\app.py#
