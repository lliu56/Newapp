## importing relavant libraies ##
from lib2to3.pgen2 import token
# from this import d
import streamlit as st 
import numpy  as np
import tokenizers
from transformers import PegasusForConditionalGeneration,PegasusTokenizer
import webComponents as wc

## initializing variables ##
xsumTokenizer = []
largeTokenizer= []
xsumModel = []
largeModel = []
website = wc.websiteComponents('PEGASUS Text Summary')
# creating a variable for data set 

dataSet ='google/pegasus-xsum','google/pegasus-large'

##downloading models from huggingface + caching ##
@st.cache(allow_output_mutation= True)              #caching while allowing output mutations
def loadTokenizer ():
    xsumTokenizer=PegasusTokenizer.from_pretrained('google/pegasus-xsum')
    largeTokenizer=PegasusTokenizer.from_pretrained('google/pegasus-large')
    return xsumTokenizer,largeTokenizer

@st.cache(allow_output_mutation= True)
def loadModel ():
    xsumModel = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
    #largeModel = PegasusForConditionalGeneration.from_pretrained('google/pegasus-large')
    return xsumModel,largeModel

## summary fxn ## 
# def choseModTok():
#     if website.putSelectBox == 'Short Summary (xsum)':
#         tokens = xsumTokenizer (text,truncation = True, \
#                             padding = 'longest', return_tensors='pt')
#     elif website.putSelectBox == 'Long Summary (Large)':
#         tokens = largeTokenizer (text,truncation = True, \
#                             padding = 'longest', return_tensors='pt')

#     if website.putSelectBox == 'Short Summary (xsum)':
#         model = xsumModel.loadModel.largeModel

#     elif website.putSelectBox == 'Long Summary (Large)':
#         model  = largeModel.loadModel.largeModel
#     return model,tokens
    



[xsumTokenizer , largeTokenizer] = loadTokenizer()
[xsumModel, largeModel]= loadModel()


## call fxn ##
text = """The Big Bang theory is the prevailing cosmological model explaining the existence of the observable universe from the earliest known periods through its subsequent large-scale evolution.[1][2][3] The model describes how the universe expanded from an initial state of high density and temperature,[4] and offers a comprehensive explanation for a broad range of observed phenomena, including the abundance of light elements, the cosmic microwave background (CMB) radiation, and large-scale structure.

Crucially, the theory is compatible with Hubble–Lemaître law—the observation that the farther away a galaxy is, the faster it is moving away from Earth. Extrapolating this cosmic expansion backwards in time using the known laws of physics, the theory describes an increasingly concentrated cosmos preceded by a singularity in which space and time lose meaning (typically named "the Big Bang singularity").[5] Detailed measurements of the expansion rate of the universe place the Big Bang singularity at around 13.8 billion years ago, which is thus considered the age of the universe.[6]

After its initial expansion, an event that is by itself often called "the Big Bang", the universe cooled sufficiently to allow the formation of subatomic particles, and later atoms. Giant clouds of these primordial elements—mostly hydrogen, with some helium and lithium—later coalesced through gravity, forming early stars and galaxies, the descendants of which are visible today. Besides these primordial building materials, astronomers observe the gravitational effects of an unknown dark matter surrounding galaxies. Most of the gravitational potential in the universe seems to be in this form, and the Big Bang theory and various observations indicate that this excess gravitational potential is not created by baryonic matter, such as normal atoms. Measurements of the redshifts of supernovae indicate that the expansion of the universe is accelerating, an observation attributed to dark energy's existence.[7]

# Georges Lemaître first noted in 1927 that an expanding universe could be traced back in time to an originating single point, which he called the "primeval atom". Edwin Hubble confirmed through analysis of galactic redshifts in 1929 that galaxies are indeed drifting apart; this is important observational evidence for an expanding universe. For several decades, the scientific community was divided between supporters of the Big Bang and the rival steady-state model which both offered explanations for the observed expansion, but the steady-state model stipulated an eternal universe in contrast to the Big Bang's finite age. In 1964, the CMB was discovered, which convinced many cosmologists that the steady-state theory was falsified,[8] since, unlike the steady-state theory, the hot Big Bang predicted a uniform background radiation throughout the universe caused by the high temperatures and densities in the distant past. A wide range of empirical evidence strongly favors the Big Bang, which is now essentially universally accepted.[9] """
# loadTokenizer()
# loadModel()
# summary= getSummary ()
# print (summary)



    
